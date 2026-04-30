def get_mask_card_number(card_number: int | str) -> str:
    """
    Маскирует номер банковской карты
    """
    card_str = str(card_number)

    # Проверяем длину номера карты
    if len(card_str) != 16:
        raise ValueError("Номер карты должен содержать 16 цифр")

    # Формируем маску номера карты
    masked = f"{card_str[:4]} {card_str[4:6]}** **** {card_str[-4:]}"
    return masked


def get_mask_account(account_number: int | str) -> str:
    """
    Маскирует номер счёта
    """
    account_str = str(account_number)

    if len(account_str) != 20:
        raise ValueError("Номер счёта должен содержать 20 цифр")

    # Маскируем номер счёта
    masker = f"**{account_str[-4:]}"
    return masker
