def test__register_route__redirects_to_login__when_user_fills_the_register_form(test_client, register_url, login_uri, fake_user_login):
    app, db = test_client
    response = app.post(register_url, data=fake_user_login)

    assert response.status_code == 302
    assert response.location == login_uri


def test__login_route__redirects_to_index__when_user_fill_the_login_form(test_client, login_uri, index_uri, before):
    app, db = test_client

    response = app.post(login_uri, data={'username': 'test_user', 'password': 'test_password'})

    assert response.status_code == 302
    assert response.location == index_uri


def test__login_route__shows_error__when_user_doesnt_fill_the_login_form(test_client, login_uri):
    app, db = test_client

    response = response = app.post(login_uri, data=None, follow_redirects=True)

    assert response.status_code == 200
    assert response.request.path == login_uri
