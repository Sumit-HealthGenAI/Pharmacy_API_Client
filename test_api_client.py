from unittest.mock import patch, Mock
from api_client import get_medicine, send_request, validate_medicine_id
import requests
import pytest


@patch("api_client.send_request")
def test_get_medicine(mock_send_request):
    fake_data = {"id": 1, "title": "Medicine A"}

    # Configure .json() directly on the mock returned by send_request
    mock_send_request.return_value.json.return_value = fake_data

    result = get_medicine(1)

    # Verify returned data
    assert result == fake_data

    # Verify exact call signature (method and full URL)
    mock_send_request.assert_called_once_with(
        "GET", "https://jsonplaceholder.typicode.com/posts/1"
    )


def test_send_request():
    mock_response = Mock()

    with patch(
        "api_client.requests.request", return_value=mock_response
    ) as mock_request:
        result = send_request("GET", "https://example.com")

        # Verify request call
        mock_request.assert_called_once_with("GET", "https://example.com", timeout=10)

        # Verify raise_for_status was called
        mock_response.raise_for_status.assert_called_once()

        # Verify returned object
        assert result is mock_response


def test_send_request_http_error():
    mock_response = Mock()

    # Configure raise_for_status() to raise an HTTPError
    mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError(
        "404 Not Found"
    )

    with patch("api_client.requests.request", return_value=mock_response):
        with pytest.raises(requests.exceptions.HTTPError):
            send_request("GET", "https://example.com")

        mock_response.raise_for_status.assert_called_once()


def test_validate_medicine_id():
    # Valid input
    assert validate_medicine_id("12") == 12

    # Invalid text
    with pytest.raises(ValueError):
        validate_medicine_id("abc")

    # Zero
    with pytest.raises(ValueError):
        validate_medicine_id("0")

    # Negative number
    with pytest.raises(ValueError):
        validate_medicine_id("-5")

    # Decimal value
    with pytest.raises(ValueError):
        validate_medicine_id("12.5")
