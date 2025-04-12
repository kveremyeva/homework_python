account_card = input()


def mask_account_card(account_card: str) -> str:
    """Функция маскировки номера банковской карты"""
    text_1 = account_card.split()
    if "Visa Platinum" in account_card or "Visa Classic" in account_card or "Visa Gold" in account_card:
        card = text_1[2]
        return f"{text_1[0]} {text_1[1]} {card[:4]} {card[4:6]}** **** {card[-4:]}"
    elif "Maestro" in account_card:
        card = text_1[1]
        return f"Maestro {card[:4]} {card[4:6]}** **** {card[-4:]}"
    elif "MasterCard" in account_card:
        card = text_1[1]
        return f"MasterCard {card[:4]} {card[4:6]}** **** {card[-4:]}"
    elif "Счет" in account_card:
        mask = text_1[1]
        return f"Счет **{mask[-4:]}"


print(mask_account_card(account_card))

full_date = input()


def get_date(full_date: str) -> str:
    """Функция изменения даты"""
    date = full_date[:10].split('-')
    date.reverse()
    return '.'.join(date)


print(get_date(full_date))
