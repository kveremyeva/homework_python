from typing import List, Dict, Any


state_filter = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(state_filter: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """Функция возвращает новый список, отфильтрованный по указанному значению"""
    return [item for item in state_filter if item.get("state") == state]


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


print(sort_by_date(sort_data))
