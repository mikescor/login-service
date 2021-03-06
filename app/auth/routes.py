from flask import render_template, flash, redirect, url_for, request, session
from flask_login import current_user, login_user, login_required, logout_user
from werkzeug.urls import url_parse

from app import create_app, db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm
from app.models import User, Post

app = create_app()


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password!')
            return redirect(url_for('auth.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('main.index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)


@bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('main.index'))


@bp.route('/registration', methods=['GET', 'POST'])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Congratulations, you are now a registered user!")
        return redirect(url_for('auth.login'))
    return render_template('registration.html', title='Registration', form=form)


@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = Post.query.filter_by(user_id=user.id).all()
    return render_template('user.html', user=user, posts=posts)


@bp.route('/delete-users/<int:page>', methods=["GET", "POST"])
@login_required
def delete_users(page=1):
    if request.method == "POST":
        username = request.form['username']
        requested_user = User.query.filter_by(username=username).first()
        if int(session['user_id']) == requested_user.id:
            flash('You cannot delete yourself!;)')
            return redirect(url_for('auth.delete_users', page=1))
        db.session.delete(requested_user)
        db.session.commit()
        flash('User {} deleted successfully!'.format(username))
        return redirect(url_for('auth.user', username=current_user.username))
    users = User.query.order_by(User.id.desc()).paginate(page,
                                      app.config['USERS_PER_PAGE'], False)
    next_url = url_for('auth.delete_users', page=users.next_num) \
        if users.has_next else None
    prev_url = url_for('auth.delete_users', page=users.prev_num) \
        if users.has_prev else None
    return render_template('delete.html', users=users.items,
                           next_url=next_url, prev_url=prev_url)
