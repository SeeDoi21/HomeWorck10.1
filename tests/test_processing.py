import pytest

from src.processing import filter_by_state, sort_by_date

sample_data = [
    {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
    {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
    {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
    {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
]


@pytest.mark.parametrize("state, expected", [
    ('EXECUTED', [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}
    ]),
    ('CANCELED', [
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]),
    ('PENDING', []),  # Сценарий, когда нет данных с таким статусом
    ('', [])  # Сценарий с пустым статусом
])
def test_filter_by_state(state, expected):
    """Тесты проверяют, что функция filter_by_state возвращает корректные результаты для разных значений state,
     включая случаи, когда таких значений в данных нет. """
    assert filter_by_state(sample_data, state) == expected


def test_sort_by_date_descending(data):
    """Тестирование сортировки в порядке убывания"""

    sorted_data = sort_by_date(data, descending=True)
    assert sorted_data[0]['date'] == '2019-07-03T18:35:29.512364'


def test_sort_by_date_ascending(data):
    """Тестирование сортировки в порядке возрастания"""

    sorted_data = sort_by_date(data, descending=False)
    assert sorted_data[0]['date'] == '2018-06-30T02:08:58.425572'


def test_sort_with_same_dates(data):
    """Проверка корректности сортировки при одинаковых датах"""

    sorted_data = sort_by_date(data)
    assert sorted_data == data


def test_sort_with_invalid_date_format(invalid_date):
    """Тесты на работу с некорректными форматами дат"""

    with pytest.raises(ValueError):
        sort_by_date(invalid_date)
