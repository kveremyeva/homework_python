from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """Функция маскировки номера банковской карты"""
    name_card = ""
    number_card = ""
    list_card = account_card.split()
    for item in list_card:
        if item.isalpha():
            name_card += item + " "
        elif item.isdigit():
            number_card += item
        if len(number_card) == 16:
            result = get_mask_card_number(number_card)
            return name_card + result
        if len(number_card) == 20:
            result = get_mask_account(number_card)
            return name_card + result
    return


if __name__ == '__main__':
    print(mask_account_card("Mastercard 9843043983221303"))
    print(mask_account_card("Visa 9843043983221300"))
    print(mask_account_card("Счет 98430439832213089630"))
    print(mask_account_card("Visa Platinum 9843043983221300"))


def get_date(full_date: str) -> str:
    """Функция изменения даты"""
    if len(full_date) > 0 and "".join(full_date[:10].split("-")).isdigit():
        return ".".join(full_date[:10].split("-")[::-1])
    return "Вы ввели некорректную дату"


if __name__ == '__main__':
    print(get_date("2024-03-11T02:26:18.671407"))
