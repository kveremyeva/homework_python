import pytest

from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "number, expected",
    [
        ("Visa Classic 8984304398322130", "Visa Classic 8984 30** **** 2130"),
        ("Счет 73654108430135874305", "Счет **4305"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Visa Classic a8984304398322130", "Введены некорректные данные"),
    ],
)
def test_numbers(number: str, expected: str) -> None:
    assert mask_account_card(number) == expected


@pytest.mark.parametrize(
    "test_input, expected",
    [
        ("2024-03-11T02:26:18.671407", "11.03.2024"),
        ("2019-10-26T14:06:85.312078", "26.10.2019"),
        ("2002-02-26T15:17:03.984523", "26.02.2002"),
        ("1945-05-09T09:23:55.162547", "09.05.1945"),
    ],
)
def test_gate_date(test_input: str, expected: str) -> None:
    assert get_date(test_input) == expected
