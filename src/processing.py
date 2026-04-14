# Импорт модуля datetime
from datetime import datetime
from typing import Any, Dict, List


# Фильтруем список словарей.
def filter_by_state(data: List[Dict[str, Any]], state: str = 'EXECUTED') -> List[Dict[str, Any]]:
    """
    Фильтрует список словарей по ключу `state`.

    :param data: Список словарей с данными о банковских операциях.
    :param state: Состояние для фильтрации (по умолчанию 'EXECUTED').
    :return: Новый список словарей, содержащий только те, у которых ключ `state` соответствует указанному значению.
    """
    return [item for item in data if item.get('state') == state]


# Сортируем список словарей.
def sort_by_date(data: List[Dict[str, Any]], descending: bool = True) -> List[Dict[str, Any]]:
    """
Сортирует список словарей по ключу `date`.

:param data: Список словарей с данными о банковских операциях.
:param descending: Порядок сортировки (по умолчанию убывающий).
:return: Новый список словарей, отсортированный по дате.
"""
    return sorted(
        data,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'),
        reverse=descending)
