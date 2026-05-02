import pytest


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


@pytest.fixture
def valid_card_numbers():
    return [
        "1234567812345678",
        1234567812345678,
    ]


@pytest.fixture
def invalid_card_numbers():
    return [
        "12345",
        "12345678901234567",
        "",
        12345,
    ]


@pytest.fixture
def invalid_inputs():
    return [
        None,
        "not a number",
    ]


@pytest.fixture
def valid_account_number():
    return "12345678901234567890"
