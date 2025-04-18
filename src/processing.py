from typing import List, Dict

dict_list = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


def filter_by_state(dict_list: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    """Функция выозвращает новый список, отфильтрованный по указанному значению"""
    return [item for item in dict_list if item.get("state") == state]


print(filter_by_state(dict_list, "EXECUTED"))


data_list = [
            {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
            {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        ]


def sort_by_date(data_list: list, reverse: bool = True) -> list:
    """Функция должна возвращает новый список, отсортированный по дате"""
    return sorted(data_list, key=lambda x: x.get("date"), reverse=reverse)


print(sort_by_date(data_list))
