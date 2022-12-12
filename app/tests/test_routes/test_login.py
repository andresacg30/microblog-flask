import pytest


def test__login_route__redirects_to_index__when_user_fill_the_login_form(test_client, login_uri, index_uri, fake_user):
    username = fake_user.get('user').username
    password = fake_user.get('password')
    data = {'user': username, 'password': password}

    response = test_client.post(login_uri, data=data, follow_redirects=True)

    pytest.assume(response.status_code == 200)
    pytest.assume(response.request.path == index_uri)


def test__login_route__shows_error__when_user_doesnt_fill_the_login_form(test_client, login_uri):

    response = response = test_client.post(login_uri, data=None, follow_redirects=True)

    pytest.assume(response.status_code == 200)
    pytest.assume(response.request.path == login_uri)
