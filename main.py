import os
from src.generators import filter_by_currency
from src.processing import filter_by_state, search_banking_transactions_by_string, sort_by_date
from src.reader_csv_xlsx import reader_transactions_csv, reader_transactions_xlsx
from src.utils import get_info_about_transactions
from src.widget import get_date, mask_account_card


def main():
    """ Основная функция, которая связывает между собой все функциональности"""
    result_data = []
    json_file = 1
    csv_file = 2
    xlsx_file = 3
    user_answer = input(f"""Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
    {json_file}. Получить информацию о транзакциях из JSON-файла
    {csv_file}. Получить информацию о транзакциях из CSV-файла
    {xlsx_file}. Получить информацию о транзакциях из XLSX-файла \n""")
    while user_answer not in ["1", "2", "3"]:
        print("Вы выбрали не верный формат. Попробуйте ещё раз")
        user_answer = input().strip()
    else:
        if user_answer == "1":
            print("Для обработки выбран JSON-файл.")
            path_to_file = os.path.join(os.path.dirname(__file__), "data", "operations.json")
            trans = get_info_about_transactions(path_to_file)
        elif user_answer == "2":
            print("Для обработки выбран CSV-файл.")
            path = os.path.join(os.path.dirname(__file__), "data", "transactions.csv")
            trans = reader_transactions_csv(path)
        elif user_answer == "3":
            print("Для обработки выбран XLSX-файл.")
            path = os.path.join(os.path.dirname(__file__), "data", "transactions_excel.xlsx")
            trans = reader_transactions_xlsx(path)
    user_answer_status = input("Введите статус, по которому необходимо выполнить фильтрацию.\n"
                               "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").upper().strip()
    while user_answer_status not in ["EXECUTED", "CANCELED", "PENDING"]:
        print(f"Статус операции {user_answer_status} недоступен.")
        user_answer_status = input("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n").upper().strip()
    else:
        print(f"Операции отфильтрованы по статусу {user_answer_status}")
        result_state = filter_by_state(trans, user_answer_status)
    print("Отсортировать операции по дате? (Да/Нет)")
    user_answer_data = input().lower()
    while user_answer_data not in ["да", "нет"]:
        user_answer_data = input("Введите: Да/Нет\n").lower().strip()
    else:
        if user_answer_data == "да":
            user_choice_sort_reverse = input("Отсортировать по возрастанию или по убыванию\n").lower().strip()
            while user_choice_sort_reverse not in ["по возрастанию", "по убыванию"]:
                user_choice_sort_reverse = input("Введите: по возрастанию/по убыванию\n").lower().strip()
            else:
                if user_choice_sort_reverse == "по возрастанию":
                    result_data = sort_by_date(result_state, False)
                elif user_choice_sort_reverse == "по убыванию":
                    result_data = sort_by_date(result_state, True)
    user_answer_rub = input("Выводить только рублевые транзакции? (Да/Нет)\n").lower()
    while user_answer_rub not in ["да", "нет"]:
        user_answer_rub = input("Введите: Да/Нет\n").lower().strip()
    else:
        if user_answer_rub == "да":
            result_rub = [item for item in filter_by_currency(result_data, "RUB")]
    user_choice_word = input("Отфильтровать список транзакций по определенному слову в описании? (Да/Нет)\n").lower()
    while user_choice_word not in ["да", "нет"]:
        user_choice_word = input("Выберите Да/Нет\n").lower().strip()
    else:
        if user_choice_word == "да":
            search_string = input("Введите слово для поиска: ").lower()
            result_word = search_banking_transactions_by_string(result_rub, search_string)
            if len(result_word) == 0:
                print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
            else:
                print("Распечатываю итоговый список транзакций...")
                print(
                    f"Всего банковских операция в выборке: {len(result_word)}\n")
    if user_answer == "1":
        for trans_result in result_word:
            print(trans_result)
            if trans_result["description"] == "Открытие вклада":
                print(f"{get_date(trans_result['date'])} {trans_result['description']}")
                print(f"{mask_account_card(trans_result['to'])}")
                print(f"Сумма: {trans_result['operationAmount']['amount']} "
                      f"{trans_result['operationAmount']['currency']['code']}\n")
            else:
                print(f"{get_date(trans_result['date'])} {trans_result['description']}")
                print(f"{mask_account_card(trans_result['from'])} -> "
                      f"{mask_account_card(trans_result['to'])}")
                print(f"Сумма: {trans_result['operationAmount']['amount']} "
                      f"{trans_result['operationAmount']['currency']['code']}\n")
    else:
        for trans_result in result_word:
            if trans_result["description"] == "Открытие вклада":
                print(f"{get_date(trans_result['date'])} {trans_result['description']}")
                print(f"{mask_account_card(trans_result['to'])}")
                print(f"Сумма: {trans_result['amount']} {trans_result['currency_code']}\n")
            else:
                print(f"{get_date(trans_result['date'])} {trans_result['description']}")
                print(f"{mask_account_card(trans_result['from'])} -> {mask_account_card(trans_result['to'])}")
                print(f"Сумма: {trans_result['amount']} {trans_result['currency_code']}\n")


main()
