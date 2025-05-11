import pytest


@pytest.fixture
def sample_state() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sample_state_without_state() -> list:
    return [
        {"id": 41428829, "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def sample_date() -> list:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 1, "state": "CANCELED", "date": "2025-03-26T17:37:18.419441"},
        {"id": 2, "state": "CANCELED", "date": "2020-10-14T03:14:25.412341"},
        {"id": 3, "state": "CANCELED", "date": "2019-02-26T15:17:33.568741"},
    ]


@pytest.fixture
def sample_filter() -> list:
    return [
        {
            'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount':
            {'amount': '9824.07', 'currency':
                {'name': 'USD', 'code': 'USD'}},
                'description': 'Перевод организации', 'from':
                'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
        {
            'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount':
            {'amount': '79114.93', 'currency':
                {'name': 'USD', 'code': 'USD'}},
                'description': 'Перевод со счета на счет', 'from':
                'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'},
        {
            'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount':
            {'amount': '79114.93', 'currency':
                {'name': 'RUB', 'code': 'RUB'}},
                'description': 'Перевод с карты на карту', 'from':
                'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'},
        {
            'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount':
            {'amount': '79114.93', 'currency':
                {'name': 'EUR', 'code': 'EUR'}},
                'description': 'Перевод со счета на счет', 'from':
                'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}]


@pytest.fixture
def sample_filter_without_code() -> list:
    return [
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount':
            {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
         'description': 'Перевод организации', 'from':
             'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount':
            {'amount': '79114.93', 'currency': {}},
         'description': 'Перевод со счета на счет', 'from':
             'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount':
            {'amount': '79114.93', 'currency': {'name': 'RUB', 'code': 'RUB'}},
         'description': 'Перевод с карты на карту', 'from':
             'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'},
        {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount':
            {'amount': '79114.93', 'currency': {}},
         'description': 'Перевод со счета на счет', 'from':
             'Visa Platinum 1246377376343588', 'to': 'Счет 14211924144426031657'}]
