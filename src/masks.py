import logging
from typing import Union

logger = logging.getLogger('masks')
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(r'E:\Python\PythonProject3\logs\masks.log', 'w', encoding='utf-8')
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(mask_card: Union[str]) -> str:
    """Функция маскировки номера банковской карты"""
    logger.warning("Функция %s запущена с данными: %s", get_mask_card_number.__name__, mask_card)
    logger.info(f"Выполняем маскировку карты {mask_card}")
    if mask_card == "" or mask_card.isalpha() or len(mask_card) != 16:
        logger.error(f"Неправильно введены данные {mask_card}")
        return "Введены некорректные данные"
    logger.info(f"Карта замаскирована {mask_card[:4]} {mask_card[4:6]}** **** {mask_card[-4:]}")
    return f"{mask_card[:4]} {mask_card[4:6]}** **** {mask_card[-4:]}"


def get_mask_account(mask: Union[str]) -> str:
    """Функция маскировки номера банковского счета"""
    logger.warning("Функция %s запущена с данными: %s", get_mask_account.__name__, mask)
    logger.info(f"Выполняем маскировку счета {mask}")
    if mask == "" or mask.isalpha() or len(mask) != 20:
        logger.error(f"Неправильно введены данные {mask}")
        return "Введены некорректные данные"
    logger.info(f"Счет замаскирован **{mask[-4:]}")
    return f"**{mask[-4:]}"


# if __name__ == '__main__':
#     print(get_mask_card_number("7000792089606361"))
#     print(get_mask_account("73654108430135874305"))
