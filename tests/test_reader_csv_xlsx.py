import csv
from unittest.mock import mock_open, patch

import pytest


# Функция для чтения CSV-файла (тестируемая)
def reader_file_transactions_csv(file_path):
    result = []
    with open(file_path, newline='', encoding="UTF-8") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        for row in reader:
            result.append(dict(row))
    return result


# Пример содержимого файла
CSV_CONTENT = """id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN
;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP
;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту
"""
# Ожидаемый результат
# Ожидаемый результат
EXPECTED_RES = [
    {
        'id': '650703',
        'state': 'EXECUTED',
        'date': '2023-09-05T11:30:32Z',
        'amount': '16210',
        'currency_name': 'Sol',
        'currency_code': 'PEN',
        'from': 'Счет 58803664561298323391',
        'to': 'Счет 39745660563456619397',
        'description': 'Перевод организации'
    },
    {
        'id': '3598919',
        'state': 'EXECUTED',
        'date': '2020-12-06T23:00:58Z',
        'amount': '29740',
        'currency_name': 'Peso',
        'currency_code': 'COP',
        'from': 'Discover 3172601889670065',
        'to': 'Discover 0720428384694643',
        'description': 'Перевод с карты на карту'
    }
]


# Тест на успешный парсинг
def test_success_reader_file_transactions_csv():
    """Тест на успешные просмотр файла"""
    with patch("builtins.open", mock_open(read_data=CSV_CONTENT)):
        result = reader_file_transactions_csv("test_path.csv")
        assert isinstance(result, list), "Результат должен быть списком"
        assert all(isinstance(item, dict) for item in result), "Все элементы должны быть словарями"


def test_empty_file():
    """ Тест на пустой список"""
    EMPTY_CSV_CONTENT = "id;state;date;amount;currency_name;currency_code;from;to;description"

    with patch("builtins.open", mock_open(read_data=EMPTY_CSV_CONTENT)):
        result = reader_file_transactions_csv("empty_file.csv")

        # Проверяем, что результат - пустой список
        assert result == [], "Результат должен быть пустым списком"
        assert len(result) == 0, "Список должен быть пустым"
        assert isinstance(result, list), "Результат должен быть списком"


# Тест на отсутствующий файл
def test_missing_file():
    """ Проверка отсуствующего файла"""
    with patch("builtins.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            reader_file_transactions_csv("missing_file.csv")
