import pytest
from app.models import User


@pytest.fixture
def fake_password(faker):
    yield faker.unique.password()


@pytest.fixture
def avatar_uri(faker):
    return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'


@pytest.fixture
def user_factory(faker):
    def factory():
        return User(
            username=faker.unique.name().lower().replace(' ', '_'),
            email=faker.email(),
        )
    return factory
