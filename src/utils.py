import json
from typing import Any


def get_info_about_transactions(path: str) -> Any:
    """ Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open(path, encoding='utf-8') as file:
            utils_data = json.load(file)
            return utils_data
    except json.JSONDecodeError:
        print('Ошибка декодирования файла')
        return []
    except FileNotFoundError:
        print('Файл не найден')
        return []


if __name__ == '__main__':
    print(get_info_about_transactions(r'..\data\operations.json'))
