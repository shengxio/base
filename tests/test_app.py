"""API endpoint tests."""
import pytest
from flask import url_for
from src.app import app

@pytest.fixture
def client():
    """Test client fixture."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_calculate_sum():
    """Test the calculate_sum function."""
    assert calculate_sum(1, 2) == 3
    assert calculate_sum(-1, 1) == 0
    assert calculate_sum(0, 0) == 0

class TestHealthEndpoint:
    """Tests for the health check endpoint."""

    def test_health_check_success(self, client):
        """Test successful health check."""
        response = client.get('/health')
        assert response.status_code == 200
        assert response.json == {"status": "healthy"}

    def test_health_check_method_not_allowed(self, client):
        """Test health check with invalid HTTP method."""
        response = client.post('/health')
        assert response.status_code == 405

class TestSumEndpoint:
    """Tests for the sum endpoint."""

    @pytest.mark.parametrize("a, b, expected", [
        (1, 2, 3),        # Positive numbers
        (-1, 1, 0),       # Mixed positive and negative
        (0, 0, 0),        # Zeros
        (-5, -3, -8),     # Negative numbers
        (999, 1, 1000),   # Large numbers
    ])
    def test_sum_valid_inputs(self, client, a, b, expected):
        """Test sum endpoint with valid inputs."""
        response = client.get(f'/sum/{a}/{b}')
        assert response.status_code == 200
        assert response.json == {"result": expected}

    def test_sum_invalid_url(self, client):
        """Test sum endpoint with invalid URL format."""
        response = client.get('/sum/abc/2')
        assert response.status_code == 404

    @pytest.mark.parametrize("path", [
        '/sum/',          # Missing both parameters
        '/sum/1',         # Missing one parameter
        '/sum/1/2/3',     # Too many parameters
    ])
    def test_sum_invalid_routes(self, client, path):
        """Test sum endpoint with invalid routes."""
        response = client.get(path)
        assert response.status_code == 404

    def test_sum_method_not_allowed(self, client):
        """Test sum endpoint with invalid HTTP method."""
        response = client.post('/sum/1/2')
        assert response.status_code == 405

    @pytest.mark.parametrize("a, b", [
        (2**31, 1),      # Number too large for 32-bit int
        (-2**31 - 1, 0), # Number too small for 32-bit int
    ])
    def test_sum_large_numbers(self, client, a, b):
        """Test sum endpoint with very large numbers."""
        response = client.get(f'/sum/{a}/{b}')
        assert response.status_code == 200
        assert "result" in response.json 