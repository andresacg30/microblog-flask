import os
import tempfile

import pytest
from app import app

from .fixtures import *  # noqa F401, F403


@pytest.fixture
def create_app():
    db_fd, dbpath = tempfile.mkstemp()

    class Config:
        SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(dbpath)
        TESTING = True
        SQLALCHEMY_TRACK_MODIFICATIONS = False

    flask_app = app.config.from_object(Config)
    app.app_context().push()
    yield flask_app

    os.close(db_fd)
    os.remove(dbpath)


@pytest.fixture
def test_client(create_app):
    client = app.test_client()
    return client
