from typing import Union

mask_card = input()
mask_account = input()


def get_mask_card_number(mask_card: Union[str]) -> str:
    """Функция маскировки номера банковской карты"""
    return f"{mask_card[:4]} {mask_card[4:6]}** **** {mask_card[-4:]}"


def get_mask_account(mask: Union[str]) -> str:
    """Функция маскировки номера банковского счета"""
    return f"**{mask[-4:]}"


print(get_mask_card_number(mask_card))
print(get_mask_account(mask_account))
