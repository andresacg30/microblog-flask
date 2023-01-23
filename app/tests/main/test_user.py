from hashlib import md5
from app.models import User
import pytest


def test__password_hashing__returns_true__when_checking_same_password(user_factory, fake_password):
    user: User = user_factory()
    user.set_password(fake_password)
    pytest.assume(user.check_password(fake_password) is True)


def test__password_hashing__returns_false__when_checking_different_password(user_factory, fake_password):
    user: User = user_factory()
    user.set_password("test")
    pytest.assume(user.check_password(fake_password) is False)


def test__avatar__returns_gravatar_endpoint__with_128b_image(user_factory, avatar_uri):
    user: User = user_factory()
    digest = md5(user.email.lower().encode('utf-8')).hexdigest()
    pytest.assume(user.avatar(128) == avatar_uri.format(digest, '128'))


def test__follow__returns_followed_user(user_factory, test_client):
    app, db = test_client
    user1: User = user_factory()
    user2: User = user_factory()
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    user1.follow(user2)

    pytest.assume(user1.is_following(user2) is True)
    pytest.assume(user1.followed.count() == 1)
    pytest.assume(user1.followed.first().username == user2.username)
    pytest.assume(user2.followers.count() == 1)
    pytest.assume(user2.followers.first().username == user1.username)


def test__unfollow__delete_follower_from_user(user_factory, test_client):
    app, db = test_client
    user1: User = user_factory()
    user2: User = user_factory()
    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    user1.follow(user2)
    user1.unfollow(user2)

    pytest.assume(user1.is_following(user2) is False)
    pytest.assume(user1.followed.count() == 0)
    pytest.assume(user2.followers.count() == 0)


def test__followed_post__returns_only_posts_by_following_users(user_factory, post_factory, test_client):
    app, db = test_client
    user1 = user_factory()
    user2 = user_factory()
    user3 = user_factory()
    user4 = user_factory()
    db.session.add_all([user1, user2, user3, user4])
    post1 = post_factory(user1)
    post2 = post_factory(user2)
    post3 = post_factory(user3)
    post4 = post_factory(user4)
    db.session.add_all([post1, post2, post3, post4])
    db.session.commit()

    user1.follow(user2)
    user1.follow(user4)
    user2.follow(user3)
    user3.follow(user4)
    db.session.commit()

    posts1 = user1.followed_posts().all()
    posts2 = user2.followed_posts().all()
    posts3 = user3.followed_posts().all()
    posts4 = user4.followed_posts().all()

    pytest.assume(posts1 == [post1, post2, post4])
    pytest.assume(posts2 == [post2, post3])
    pytest.assume(posts3 == [post3, post4])
    pytest.assume(posts4 == [post4])
