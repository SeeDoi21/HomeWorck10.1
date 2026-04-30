import pytest

from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number(card_str):
    """ Функция тестирования сценариев ввода функции get_mask_card_number
     из модуля masks.py"""
    assert get_mask_card_number(1234567890123456) == "1234 56** **** 3456"
    assert get_mask_card_number(1234567891234567) == "1234 56** **** 4567"
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    with pytest.raises(ValueError):
        get_mask_card_number("=+-_&*^")


def test_get_mask_account(account_str):
    """Функция тестирования сценариев ввода функции get_mask_account
    из модуля masks.py"""
    assert get_mask_account(12345600007890123456) == "**3456"
    assert get_mask_account(12345670000891234567) == "**4567"
    if len(account_str) != 20:
        raise ValueError("Номер счёта должен содержать 20 цифр")

    with pytest.raises(ValueError):
        get_mask_account("=+-_&*^")
