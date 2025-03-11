"""Integration tests for the application."""
import pytest
import requests
from src.app import app

@pytest.fixture(scope="module")
def test_client():
    """Create a test client for the entire test module."""
    with app.test_client() as client:
        yield client

class TestApplicationFlow:
    """Integration tests for the application workflow."""

    def test_health_and_sum_flow(self, test_client):
        """Test a complete flow checking health and performing calculations."""
        # First check health
        health_response = test_client.get('/health')
        assert health_response.status_code == 200
        assert health_response.json == {"status": "healthy"}

        # Then perform calculations
        test_cases = [
            (1, 2, 3),
            (-1, 1, 0),
            (100, 200, 300)
        ]

        for a, b, expected in test_cases:
            sum_response = test_client.get(f'/sum/{a}/{b}')
            assert sum_response.status_code == 200
            assert sum_response.json == {"result": expected}

    def test_concurrent_requests(self, test_client):
        """Test handling multiple requests concurrently."""
        import concurrent.futures

        def make_request(params):
            a, b = params
            return test_client.get(f'/sum/{a}/{b}').json

        # Create a list of parameter pairs
        params_list = [(i, i+1) for i in range(10)]

        with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
            results = list(executor.map(make_request, params_list))

        # Verify results
        for i, result in enumerate(results):
            assert result == {"result": 2*i + 1}

    @pytest.mark.slow
    def test_load_handling(self, test_client):
        """Test application behavior under load."""
        num_requests = 100
        responses = []

        # Make multiple requests in quick succession
        for _ in range(num_requests):
            response = test_client.get('/sum/1/1')
            responses.append(response)

        # Verify all responses
        for response in responses:
            assert response.status_code == 200
            assert response.json == {"result": 2}

    def test_error_recovery(self, test_client):
        """Test application's ability to recover from errors."""
        # Make an invalid request
        invalid_response = test_client.get('/sum/invalid/1')
        assert invalid_response.status_code == 404

        # Verify service still works after error
        valid_response = test_client.get('/sum/1/1')
        assert valid_response.status_code == 200
        assert valid_response.json == {"result": 2}

    @pytest.mark.parametrize("endpoint", [
        '/health',
        '/sum/1/2',
        '/nonexistent',
    ])
    def test_response_headers(self, test_client, endpoint):
        """Test response headers for various endpoints."""
        response = test_client.get(endpoint)
        
        # Check common headers
        assert 'Content-Type' in response.headers
        if response.status_code == 200:
            assert response.headers['Content-Type'] == 'application/json' 