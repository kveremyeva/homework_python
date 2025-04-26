import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize(
    "number, expected",
    [
        ("6546543123465748", "6546 54** **** 5748"),
        ("", "Введены некорректные данные"),
        ("Hello", "Введены некорректные данные"),
        ("123456789", "Введены некорректные данные"),
    ],
)
def test_numbers(number: str, expected: str) -> None:
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize(
    "number, expected",
    [
        ("73654108430135874305", "**4305"),
        ("", "Введены некорректные данные"),
        ("Hello", "Введены некорректные данные"),
        ("123456789", "Введены некорректные данные"),
    ],
)
def test_mask_account(number: str, expected: str) -> None:
    assert get_mask_account(number) == expected
