import pytest
from faker import Faker

faker = Faker()


@pytest.fixture
def login_uri():
    return '/login/'


@pytest.fixture
def index_uri():
    return '/index/'


@pytest.fixture
def fake_user_login():
    user = faker.name()
    password = faker.password()
    return {'username': user, 'password': password}


@pytest.fixture
def fake_post(fake_user):
    post = [
        {
            'author': fake_user,
            'body': faker.sentence,
        },
    ]
    return post
