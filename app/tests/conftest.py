import pytest
from flask import Flask

from app import db, migrate

from .fixtures import *  # noqa F401, F403


@pytest.fixture
def test_app():

    class Config:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
        TESTING = True
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        WTF_CSRF_ENABLED = False

    flask_app = Flask(__name__)
    flask_app.config.from_object(Config)
    flask_app.app_context().push()
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    db.create_all()

    yield flask_app, db

    db.session.remove()
    db.drop_all()


@pytest.fixture
def test_client(test_app):
    app, db = test_app
    client = app.test_client()
    return client, db
