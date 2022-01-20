import pytest

from kvikshaug.app import app as app_


@pytest.fixture(scope="session")
def app():
    """Provide a Flask app with the app context."""
    with app_.app_context():
        yield app_


@pytest.fixture(scope="session")
def client(app):
    """Provide a Flask test client for endpoint tests."""
    with app.test_client() as client:
        yield client
