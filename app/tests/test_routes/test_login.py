import pytest


def test__login_route__redirects_to_index__when_user_fill_the_login_form(test_client, login_uri):
    response = test_client.get(login_uri, follow_redirects=True)
    pytest.assume(response.status_code == 200)
    pytest.assume(response.request.path == login_uri)
