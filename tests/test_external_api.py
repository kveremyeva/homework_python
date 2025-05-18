from unittest.mock import Mock, patch

import pytest
import requests

from src.external_api import transaction_amount


@pytest.fixture
def get_mock_requests():
    with patch("requests.get") as mock_get:
        yield mock_get


def test_usd_transaction_success(get_mock_requests):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"success": True, "result": "7999.54"}
    get_mock_requests.return_value = mock_response

    result = transaction_amount({"operationAmount": {"amount": 100, "currency": {"code": "USD"}}})
    assert result == 7999.54
    get_mock_requests.assert_called_once()


@pytest.mark.parametrize(
    "to, from_, amount",
    [
        ("RUB", "USD", "100"),
        ("RUB", "EUR", "200")
    ]
)
def test_amount(to, from_, amount):
    response = requests.get(f"https://api.apilayer.com/exchangerates_data/convert?to={to}"
                            f"&from={from_}&amount={amount}")
    return response.json()


@patch('requests.get')
def test_amount_test(mock_get):
    mock_get.return_value.json.return_value = {"success": True, "result": "7999.54"}
    assert test_amount('RUB', 'USD', 100) == {'result': '7999.54', 'success': True}
    mock_get.assert_called_once_with('https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100')


def test_invalid_transaction(capsys):
    captured = capsys.readouterr()
    assert '' in captured.out


def test_empty_json():
    with patch('src.external_api.transaction_amount', return_value=[]):
        result = transaction_amount({})
        assert result == []
