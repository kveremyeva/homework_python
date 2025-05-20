import json
import logging
from typing import Any

logger = logging.getLogger('utils')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r'E:\Python\PythonProject3\logs\utils.log', 'w', encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_info_about_transactions(path: str) -> Any:
    """ Принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    logger.warning("Функция %s запущена", get_info_about_transactions.__name__)
    logger.info("Принимаем на вход JSON-файл %s", path)
    try:
        with open(path, encoding='utf-8') as file:
            utils_data = json.load(file)
            logger.info("JSON-файл %s успешно открыт", path)
            if not isinstance(utils_data, list):
                logger.error("Файл пустой")
                return []
            else:
                logger.info("Возвращен список с данными о финансовых транзакциях")
                return utils_data
    except json.JSONDecodeError as ex:
        logger.error(f"Ошибка декодирования файла {ex}")
        print('Ошибка декодирования файла')
        return []
    except FileNotFoundError as ex:
        logger.error(f"Файл не найден {ex}")
        print('Файл не найден')
        return []
    except KeyError as ex:
        logger.error(f"Файл пустой {ex}")
        print('Пустой список')
        return []


if __name__ == '__main__':
    print(get_info_about_transactions(r'..\data\operations.json'))
