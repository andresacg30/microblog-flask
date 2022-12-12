import pytest
from faker import Faker

from app.models import User

faker = Faker()


@pytest.fixture
def login_uri():
    return '/login/'


@pytest.fixture
def index_uri():
    return '/index/'


@pytest.fixture
def fake_user():
    user = User(
        username=faker.name().lower().replace(' ', '_'),
        email=faker.email(),
    )
    password = faker.password()
    user.set_password(password)
    return {'user': user, 'password': password}


@pytest.fixture
def fake_post(fake_user):
    post = [
        {
            'author': fake_user,
            'body': faker.sentence,
        },
    ]
    return post
