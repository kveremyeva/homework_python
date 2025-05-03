from typing import Union


def get_mask_card_number(mask_card: Union[str]) -> str:
    """Функция маскировки номера банковской карты"""
    if mask_card == "" or mask_card.isalpha() or len(mask_card) != 16:
        return "Введены некорректные данные"
    return f"{mask_card[:4]} {mask_card[4:6]}** **** {mask_card[-4:]}"


def get_mask_account(mask: Union[str]) -> str:
    """Функция маскировки номера банковского счета"""
    if mask == "" or mask.isalpha() or len(mask) != 20:
        return "Введены некорректные данные"
    return f"**{mask[-4:]}"


print(get_mask_card_number("7000792089606361"))
print(get_mask_account("73654108430135874305"))
