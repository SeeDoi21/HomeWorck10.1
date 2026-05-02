import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тестирование правильности маскирования номера карты
@pytest.mark.parametrize("expected", [
    "1234 56** **** 5678",
])
def test_get_mask_card_number_masking(valid_card_numbers, expected):
    for card_number in valid_card_numbers:
        assert get_mask_card_number(card_number) == expected


# Проверка выброса исключения для номера карты неправильной длины
@pytest.mark.parametrize("expected_exception", [ValueError])
def test_get_mask_card_number_invalid_length(invalid_card_numbers, expected_exception):
    for card_number in invalid_card_numbers:
        with pytest.raises(expected_exception, match="Номер карты должен содержать 16 цифр"):
            get_mask_card_number(card_number)


# Проверка некорректного ввода
@pytest.mark.parametrize("expected_exception", [ValueError])
def test_get_mask_card_number_invalid_input(invalid_inputs, expected_exception):
    for card_number in invalid_inputs:
        with pytest.raises(expected_exception):
            get_mask_card_number(card_number)


# Тест на возврат валидного номера счёта
def test_mask_account_with_valid_number(valid_account_number):
    masked = get_mask_account(valid_account_number)
    assert masked == "**7890"


# Проверка обработки некорректных данных
def test_mask_account_invalid_length():
    with pytest.raises(ValueError, match="Номер счёта должен содержать 20 цифр"):
        get_mask_account("123")
