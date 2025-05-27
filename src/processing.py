import re
from collections import Counter
from typing import Any, Dict, List

state_filter = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(state_filter: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отфильтрованный по указанному значению"""
    return [item for item in state_filter if item.get("state") == state]


if __name__ == '__main__':
    print(filter_by_state(state_filter, "EXECUTED"))


sort_data = [
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]


def sort_by_date(sort_data: List[Dict[str, Any]], reverse: bool = True) -> List[Dict[str, Any]]:
    """Функция должна возвращать новый список, отсортированный по дате"""
    return sorted(sort_data, key=lambda x: str(x.get("date")), reverse=reverse)


if __name__ == '__main__':
    print(sort_by_date(sort_data))


def search_banking_transactions_by_string(transactions: list, search_string=None) -> list:
    """Функция принимает список словарей с данными о банковских операциях и строку поиска,
    а возвращает список словарей, у которых в описании есть данная строка."""
    try:
        if search_string is None:
            return transactions
        pattern = search_string
        if len(transactions) > 0:
            result = []
            for trans in transactions:
                if re.search(pattern, trans.get("description", ""), re.IGNORECASE) is not None:
                    result.append(trans)
            return result
        return []
    except Exception:
        return []


def get_count_transactions_category(transactions: list, list_categories: list) -> dict:
    """Функция принимает список словарей с данными о банковских операциях и список категорий операций, а возвращает
    словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории."""
    try:
        if len(list_categories) == 0:
            return {}

        if len(transactions) > 0:
            result_counter = Counter()
            for category in list_categories:
                pattern = category
                for trans in transactions:
                    if pattern in trans.get("description"):
                        result_counter[pattern] += 1
            return result_counter
        return {}
    except Exception:
        return {}
