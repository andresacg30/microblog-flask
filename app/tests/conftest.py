import os
import tempfile
import pytest

from app import app, db, migrate

from .fixtures import *  # noqa F401, F403


@pytest.fixture
def test_app():
    db_fd, dbpath = tempfile.mkstemp()

    class Config:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(dbpath)
        TESTING = True
        SQLALCHEMY_TRACK_MODIFICATIONS = False
        WTF_CSRF_ENABLED = False

    flask_app = app
    flask_app.app_context().push()
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    db.create_all()

    yield flask_app

    db.session.remove()
    db.drop_all()
    os.close(db_fd)
    os.remove(dbpath)


@pytest.fixture
def test_client(test_app):
    client = test_app.test_client()
    return client
