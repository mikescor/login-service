import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    SECRET_KEY=os.environ.get('SECRET_KEY') or \
               '\xa8\x92+\xca\xb5\xd6)jX\x80\xd7]+\x031\xf7\xac\xed\xb4{t;\xa0'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    USERS_PER_PAGE = 5
