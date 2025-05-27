import pytest

from src.processing import (filter_by_state, sort_by_date,
                            search_banking_transactions_by_string, get_count_transactions_category)


def test_state_default(sample_state: list) -> None:
    assert filter_by_state(sample_state) == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_state_canceled(sample_state: list) -> None:
    assert filter_by_state(sample_state, "CANCELED") == [
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


def test_state_executed(sample_state: list) -> None:
    assert filter_by_state(sample_state, "EXECUTED") == [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_state_empty() -> None:
    assert filter_by_state([]) == []


def test_filter_by_state_without_state(sample_state_without_state: list) -> None:
    assert filter_by_state(sample_state_without_state) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"}
    ]
    assert filter_by_state(sample_state_without_state, "CANCELED") == [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]


def test_date_default(sample_date: list) -> None:
    assert sort_by_date(sample_date) == [
        {"id": 1, "state": "CANCELED", "date": "2025-03-26T17:37:18.419441"},
        {"id": 2, "state": "CANCELED", "date": "2020-10-14T03:14:25.412341"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 3, "state": "CANCELED", "date": "2019-02-26T15:17:33.568741"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_date_increasing(sample_date: list) -> None:
    assert sort_by_date(sample_date, False) == [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 3, "state": "CANCELED", "date": "2019-02-26T15:17:33.568741"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "CANCELED", "date": "2020-10-14T03:14:25.412341"},
        {"id": 1, "state": "CANCELED", "date": "2025-03-26T17:37:18.419441"},
    ]


def test_date_decreasing(sample_date: list) -> None:
    assert sort_by_date(sample_date, True) == [
        {"id": 1, "state": "CANCELED", "date": "2025-03-26T17:37:18.419441"},
        {"id": 2, "state": "CANCELED", "date": "2020-10-14T03:14:25.412341"},
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 3, "state": "CANCELED", "date": "2019-02-26T15:17:33.568741"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


def test_empty_date() -> None:
    assert sort_by_date([], False) == []


@pytest.fixture
def sample_transactions_by_search_string() -> list:
    return [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
    ]


@pytest.fixture
def sample_transactions_count_category() -> list:
    return [
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
        {"description": "Перевод организации"},
    ]


@pytest.fixture
def sample_category() -> list:
    return ["Перевод организации", "Открытие вклада", "Перевод со счета на счет", "Перевод с карты на карту"]


def test_search_banking_trans_empty() -> None:
    assert search_banking_transactions_by_string([], "вклад") == []


def test_search_banking_trans_with_uppercase_string(sample_transactions_by_search_string: list) -> None:
    result = search_banking_transactions_by_string(sample_transactions_by_search_string, "ПЕРЕВОД")
    assert len(result) == 5
    assert all("перевод" in trans["description"].lower() for trans in result)


def test_search_banking_trans_no_match(sample_transactions_by_search_string: list) -> None:
    result = search_banking_transactions_by_string(sample_transactions_by_search_string, "карта")
    assert result == []


def test_get_count_empty_transactions(sample_category: list) -> None:
    result = get_count_transactions_category([], sample_category)
    assert result == {}


def test_get_count_empty_categories(sample_transactions_count_category: list) -> None:
    result = get_count_transactions_category(sample_transactions_count_category, [])
    assert result == {}


def test_get_count_match_category(sample_transactions_count_category: list, sample_category: list) -> None:
    result = get_count_transactions_category(sample_transactions_count_category, sample_category)
    assert result == {
        "Перевод организации": 5,
        "Открытие вклада": 3,
        "Перевод с карты на карту": 2,
        "Перевод со счета на счет": 1,
    }
