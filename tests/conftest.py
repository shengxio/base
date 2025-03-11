"""Shared pytest fixtures."""
import pytest
from src.app import app

@pytest.fixture
def client():
    """Create a test client fixture."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.fixture
def app_with_db():
    """Create a test app with test configuration."""
    app.config['TESTING'] = True
    return app 