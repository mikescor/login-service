from flask import g, url_for, current_app, render_template, request
from flask_login import current_user, login_required

from app import db
from app.main import bp
from app.main.forms import SearchForm
from app.models import Post


@bp.before_app_request
def before_request():
    if current_user.is_authenticated:
        db.session.commit()
        g.search_form = SearchForm()


@bp.route('/search')
@login_required
def search():
    page = request.args.get('page', 1, type=int)
    posts, total = Post.search(g.search_form.q.data, page,
                               current_app.config['POSTS_PER_PAGE'])
    next_url = url_for('main.search', q=g.search_form.q.data, page=page + 1) \
        if total > page * current_app.config['POSTS_PER_PAGE'] else None
    prev_url = url_for('main.search', q=g.search_form.q.data, page=page - 1) \
        if page > 1 else None
    return render_template('search.html', title='Search', posts=posts,
                           next_url=next_url, prev_url=prev_url)
