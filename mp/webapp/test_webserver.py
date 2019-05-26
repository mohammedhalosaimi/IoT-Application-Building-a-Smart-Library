import os
import pytest
import app

@pytest.fixture
def client():
    app.app.config['TESTING'] = True
    client = app.app.test_client()

    yield client

def test_index(client):
    result = client.get('/')
    assert b'login' in result.data

def login(client, username, password):
    return client.post('/login', data=dict(
        username=username,
        password=password
    ), follow_redirects=True)

def logout(client):
    return client.get('/logout', follow_redirects=True)

def test_login_logout(client):
    incorrect_username = "incorrect"
    incorrect_password = "incorrect"
    correct_username = "jaqen"
    correct_password = "hgar"

    # Log in with correct details
    result = login(client,correct_username, correct_password)
    # If logged in, the logout option should appear
    assert b'logout' in result.data

    rv = logout(client)
    # When logged out, the log in option should appear
    assert b'login' in rv.data

    rv = login(client, incorrect_username, incorrect_password)
    # Login should fail with the message Invalid credentials
    assert b'Invalid' in rv.data

def test_test_no_access(client):
    rv = logout(client)
    # Logout incase logged in
    assert b'You must be logged in to log out' in rv.data
    rv = client.get('/booklist', follow_redirects=True)
    # The user should be taken back to the index, with login as an option
    assert b'login' in rv.data

    rv = client.get('/datavis', follow_redirects=True)
    # The user should be taken back to the index, with login as an option
    assert b'login' in rv.data