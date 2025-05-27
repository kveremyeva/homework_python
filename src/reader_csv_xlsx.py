import csv

import pandas as pd


def reader_transactions_csv(csv_file: str) -> list:
    """ Считывание финансовых операций из CSV файла"""
    try:
        with open(r'..\data\transactions.csv', encoding='utf-8') as file:
            """ Открытие файла CSV"""
            reader_csv = csv.DictReader(file, delimiter=";")
            result = list(reader_csv)
            return result
    except (FileNotFoundError, Exception):
        return []


def reader_transactions_xlsx(xlsx_file: str) -> list:
    """ Считывание финансовых операций из EXCEL файла"""
    try:
        df_excel = pd.read_excel(r'..\data\transactions_excel.xlsx', dtype=str, engine="openpyxl")
        result = df_excel.to_dict(orient="records")
        return result
    except (FileNotFoundError, Exception):
        return []


if __name__ == '__main__':
    print(reader_transactions_csv(r'..\data\transactions.csv'))
    print(reader_transactions_xlsx(r'..\data\transactions_excel.xlsx'))
