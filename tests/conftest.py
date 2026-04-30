import pytest


@pytest.fixture
def card_str():
    return "1234567890123456"


@pytest.fixture
def account_str():
    return "12345678901234567890"


@pytest.fixture
def data():
    return [
        {'date': '2019-07-03T18:35:29.512364'},
        {'date': '2018-06-30T02:08:58.425572'}
    ]


@pytest.fixture
def invalid_date():
    return [
        {'date': 'invalid-date-format'}
    ]


@pytest.fixture
def input_data():
    return [[
        "",  # пустая строка
        None,  # None как входное значение
        1234567890123456,  # числовое значение
        "Карта",  # слишком короткая строка
    ]]
