import pytest
from faker import Faker
from datetime import datetime

from app.models import Post


faker = Faker()
now = datetime.utcnow()


@pytest.fixture
def post_factory(user_factory):
    def factory(user):
        return Post(
            body=faker.unique.sentence(),
            author=user,
            timestamp=now
        )
    return factory
