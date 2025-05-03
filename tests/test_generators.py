import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_empty_list() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_sample_filter(sample_filter: list) -> None:
    result = list(filter_by_currency(sample_filter, "USD"))
    expected = [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount': {
            'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}}, ''
            'description': 'Перевод организации', 'from':
            'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount':
            {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
            'description': 'Перевод со счета на счет', 'from':
            'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}
    ]
    assert result == expected


def test_sample_filter_rub(sample_filter: list) -> None:
    result = list(filter_by_currency(sample_filter, "RUB"))
    expected = [
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount':
            {'amount': '79114.93', 'currency': {'name': 'RUB', 'code': 'RUB'}},
         'description': 'Перевод с карты на карту', 'from':
             'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}
    ]
    assert result == expected


@pytest.mark.parametrize(
    "expected",
    {
        (
            'Перевод организации',
            'Перевод со счета на счет',
            'Перевод с карты на карту',
            'Перевод со счета на счет'),
    }
)
def test_sample_description(sample_filter: list, expected: str) -> None:
    result = list(transaction_descriptions(sample_filter))
    assert result == list(expected)


def test_empty_description() -> None:
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize(
    "start, stop, first_card, end_card", {
        (1, 4, "0000 0000 0000 0001", "0000 0000 0000 0004"),
        (15, 30, "0000 0000 0000 0015", "0000 0000 0000 0030"),
        (5956132884514579, 5956132884514589, "5956 1328 8451 4579", "5956 1328 8451 4589")
    }
)
def test_card_number(start: int, stop: int, first_card: str, end_card: str) -> None:
    result = list(card_number_generator(start, stop))
    assert result[0] == first_card
    assert result[-1] == end_card
    assert len(result) == stop - start + 1
