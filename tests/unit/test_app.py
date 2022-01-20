from kvikshaug.app import app


def test_mode():
    """Ensure that the app is in testing mode."""
    assert app.testing
