import pytest
from faker import Faker


faker = Faker()


@pytest.fixture
def register_url():
    return '/auth/register'
