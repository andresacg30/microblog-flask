import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "1234"
    ENV = os.environ.get('ENV')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') if not \
        ENV else 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = [os.environ.get('ADMIN_EMAIL')]
    POSTS_PER_PAGE = 25
    LANGUAGES = ['en', 'es']
    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')
    REDIS_URL = os.environ.get('REDIS_URL') or 'redis://'
