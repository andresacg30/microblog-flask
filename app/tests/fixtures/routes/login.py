import pytest
from faker import Faker


faker = Faker()


@pytest.fixture
def login_uri():
    return '/login/'


@pytest.fixture
def index_uri():
    return '/index/'
