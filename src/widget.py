def mask_account_card(account_card: str) -> str:
    """Функция маскировки номера банковской карты"""
    text_1 = account_card.split()
    card = text_1[-1]
    if card == "" or not card.isdigit():
        return "Введены некорректные данные"
    if "Visa Platinum" in account_card or "Visa Classic" in account_card or "Visa Gold" in account_card:
        return f"{text_1[0]} {text_1[1]} {card[:4]} {card[4:6]}** **** {card[-4:]}"
    elif "Maestro" in account_card or "MasterCard" in account_card:
        return f"{text_1[0]} {card[:4]} {card[4:6]}** **** {card[-4:]}"
    elif "Счет" in account_card:
        mask = text_1[1]
        return f"Счет **{mask[-4:]}"


print(mask_account_card("MasterCard 984304398322130"))


def get_date(full_date: str) -> str:
    """Функция изменения даты"""
    if len(full_date) > 0 and "".join(full_date[:10].split("-")).isdigit():
        return ".".join(full_date[:10].split("-")[::-1])
    return "Вы ввели некорректную дату"


print(get_date("2024-03-11T02:26:18.671407"))
