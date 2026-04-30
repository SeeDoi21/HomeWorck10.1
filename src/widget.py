# Импортируем функции get_mask_card_number и get_mask_account из модуля masks.py
# Импорт модуля re
import re
# Импорт модуля datetime
from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card: str) -> str:
    """
    Принимает один аргумент — строку, содержащую тип и номер карты или счета,
     и возвращает строку с замаскированным номером.
    """
    if not isinstance(account_card, str):
        raise ValueError("Введите строку")

    if "Счет" in account_card:
        letters_count = "".join(re.findall(r"\D+", account_card))
        numbers_count = "".join(re.findall(r"\d+", account_card))
        return f"{letters_count}{get_mask_account(numbers_count)}"
    else:
        letters_card = "".join(re.findall(r"\D+", account_card))
        numbers_card = "".join(re.findall(r"\d+", account_card))
        return f"{letters_card}{get_mask_card_number(numbers_card)}"


def get_date(date_str: str) -> str:
    try:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%S.%f")
    except ValueError:
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
    return parsed_date.strftime("%d.%m.%Y")
