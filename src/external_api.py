import json
import os
from typing import Any

import requests
from dotenv import load_dotenv

load_dotenv(r'..\.env')

API_KEY = os.getenv('API_KEY')

headers = {"apikey": API_KEY}

with open(r'E:\Python\PythonProject3\data\operations.json', encoding='utf-8') as file:
    transaction_json = json.load(file)

results = []


def transaction_amount(conversion: dict) -> Any:
    """Функция ковертирует из USD в RUB используя файл JSON и возвращает ответ через API запрос"""
    try:
        for transaction in transaction_json:

            if (transaction['operationAmount']['currency']['code'] == "EUR"
                    or transaction['operationAmount']['currency']['code'] == "USD"):
                to = "RUB"
                from_ = transaction['operationAmount']['currency']['code']
                amount = transaction['operationAmount']['amount']
                url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from_}&amount={amount}"
                response = requests.request("GET", url, headers=headers)
                status_code = response.status_code
                if status_code == 200:
                    result = response.json().get("result")
                    results.append((result))
                else:
                    return f"Не успешный запрос, код ошибки: {status_code}"
        return float(results)

    except KeyError:
        print("Ошибка")


print(transaction_amount(transaction_json))
