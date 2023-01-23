import pytest
from faker import Faker

from app.models import User


faker = Faker()


@pytest.fixture
def login_uri():
    return '/auth/login'


@pytest.fixture
def index_uri():
    return '/index'


@pytest.fixture
def fake_user_login(faker):
    user = faker.name().lower().replace(' ', "")
    email = faker.email()
    password = faker.password()
    return {'username': user, 'password': password, 'email': email, 'password2': password}


@pytest.fixture
def before(test_client):
    app, db = test_client
    user = User(username='test_user', email='test_user@example.com')
    user.set_password('test_password')
    db.session.add(user)
    db.session.commit()
