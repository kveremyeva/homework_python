from typing import Generator, Iterator

transactions = [
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572', 'operationAmount':
        {'amount': '9824.07', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Перевод организации', 'from':
         'Счет 75106830613657916952', 'to': 'Счет 11776614605963066702'},
    {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount':
        {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}},
     'description': 'Перевод со счета на счет', 'from':
         'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'},
    {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount':
        {'amount': '79114.93', 'currency': {'name': 'RUB', 'code': 'RUB'}},
     'description': 'Перевод с карты на карту', 'from':
         'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'},
    {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount':
        {'amount': '79114.93', 'currency': {'name': 'EUR', 'code': 'EUR'}},
     'description': 'Перевод со счета на счет', 'from':
         'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}]


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Функция которая выдает транзакции с заданной валютой (например USD)"""
    transactions_code = []
    for item in transactions:
        if item.get('operationAmount', {}).get('currency', {}).get('code', {}) == currency:
            transactions_code.append(item)
        elif item.get('currency_code') == currency:
            transactions_code.append(item)
    return transactions_code


if __name__ == '__main__':
    filter = filter_by_currency(transactions, "USD")
    print(filter)


def transaction_descriptions(transactions: list) -> Generator:
    """Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди"""
    for item_descriptions in transactions:
        yield item_descriptions['description']


if __name__ == '__main__':
    descriptions = transaction_descriptions(transactions)
    print(next(descriptions))


def card_number_generator(start: int, stop: int) -> Generator:
    """Генератор, выдает номера банковских карт в формате ХХХХ ХХХХ ХХХХ ХХХХ, где Х - цифра номера карты."""
    for item in range(start, stop+1):
        number = "0" * (16 - len(str(item))) + str(item)
        card_number = " ".join(number[i: i+4] for i in range(0, 16, 4))
        yield card_number


if __name__ == '__main__':
    num = card_number_generator(1, 10)
    print(next(num))
