import pytest

from src.widget import get_date, mask_account_card


def test_mask_account_card():
    """Функция тестирования сценариев ввода функции mask_account_card
    из модуля widget.py"""
    assert mask_account_card("Visa Platinum 7000792289606361") == "Visa Platinum 7000 79** **** 6361"
    assert mask_account_card("Счет 73654108430135874305") == "Счет **4305"
    assert mask_account_card("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"


#  Тест на обработку некорректных данных
def test_mask_account_card_invalid_input(input_data):
    with pytest.raises(ValueError):
        mask_account_card(input_data)


def test_get_date():
    """Функция тестирования сценариев ввода функции get_date
    из модуля widget.py"""
    assert get_date("2024-03-11T02:26:18.671407") == "11.03.2024"
    assert get_date("2024-01-01T00:00:00.000000") == "01.01.2024"
    assert get_date("2024-12-31T23:59:59.999999") == "31.12.2024"
    assert get_date("2024-03-11") == "11.03.2024"
    with pytest.raises(ValueError):
        get_date("")
