import pytest
from src.generators import filter_by_currency, transaction_descriptions, card_number_generator


@pytest.fixture
def transactions():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount":
            {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
         "description": "Перевод организации",
         "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
        {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount":
            {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
         "description": "Перевод со счета на счет",
         "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"},
        {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404", "operationAmount":
            {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод со счета на счет",
         "from": "Счет 44812258784861134719", "to": "Счет 74489636417521191160"},
        {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916", "operationAmount":
            {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
         "description": "Перевод с карты на карту",
         "from": "Visa Classic 6831982476737658",
         "to": "Visa Platinum 8990922113665229"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689", "operationAmount":
            {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод организации",
         "from": "Visa Platinum 1246377376343588", "to": "Счет 14211924144426031657"}
    ]


@pytest.mark.parametrize("transactions, code, expected", [
    (
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount":
                    {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод организации",
                 "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
                {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount":
                    {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод со счета на счет",
                 "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"},
                {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404", "operationAmount":
                    {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод со счета на счет",
                 "from": "Счет 44812258784861134719", "to": "Счет 74489636417521191160"},
                {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916", "operationAmount":
                    {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод с карты на карту",
                 "from": "Visa Classic 6831982476737658",
                 "to": "Visa Platinum 8990922113665229"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689", "operationAmount":
                    {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод организации",
                 "from": "Visa Platinum 1246377376343588", "to": "Счет 14211924144426031657"}
            ],
            "USD",
            [
                {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916", "operationAmount":
                    {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод с карты на карту", "from": "Visa Classic 6831982476737658",
                 "to": "Visa Platinum 8990922113665229"},
                {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount":
                    {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод со счета на счет", "from": "Счет 19708645243227258542",
                 "to": "Счет 75651667383060284188"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount":
                    {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод организации",
                 "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"}
            ]
    )
])
def test_filter_by_currency(transactions, code, expected):
    assert list(filter_by_currency(transactions, code)) == expected


def test_filter_by_currency_empty_list(transactions):
    assert list(filter_by_currency([], 'USD')) == []


def test_filter_by_currency_without_code(transactions):
    with pytest.raises(ValueError):
        list(filter_by_currency([{
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        }]))


@pytest.fixture
def transactions_for_description():
    return [
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount":
            {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
         "description": "Перевод организации",
         "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
        {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount":
            {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
         "description": "Перевод со счета на счет",
         "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"},
        {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404", "operationAmount":
            {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод со счета на счет",
         "from": "Счет 44812258784861134719", "to": "Счет 74489636417521191160"},
        {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916", "operationAmount":
            {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
         "description": "Перевод с карты на карту",
         "from": "Visa Classic 6831982476737658",
         "to": "Visa Platinum 8990922113665229"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689", "operationAmount":
            {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
         "description": "Перевод организации",
         "from": "Visa Platinum 1246377376343588", "to": "Счет 14211924144426031657"}
    ]


@pytest.mark.parametrize("transactions_for_description, expected", [
    (
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572", "operationAmount":
                    {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод организации",
                 "from": "Счет 75106830613657916952", "to": "Счет 11776614605963066702"},
                {"id": 142264268, "state": "EXECUTED", "date": "2019-04-04T23:20:05.206878", "operationAmount":
                    {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод со счета на счет",
                 "from": "Счет 19708645243227258542", "to": "Счет 75651667383060284188"},
                {"id": 873106923, "state": "EXECUTED", "date": "2019-03-23T01:09:46.296404", "operationAmount":
                    {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод со счета на счет",
                 "from": "Счет 44812258784861134719", "to": "Счет 74489636417521191160"},
                {"id": 895315941, "state": "EXECUTED", "date": "2018-08-19T04:27:37.904916", "operationAmount":
                    {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
                 "description": "Перевод с карты на карту",
                 "from": "Visa Classic 6831982476737658",
                 "to": "Visa Platinum 8990922113665229"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689", "operationAmount":
                    {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
                 "description": "Перевод организации",
                 "from": "Visa Platinum 1246377376343588", "to": "Счет 14211924144426031657"}
            ], ["Перевод организации", "Перевод со счета на счет", "Перевод со счета на счет",
                "Перевод с карты на карту", "Перевод организации"])])
def test_transaction_descriptions(transactions_for_description, expected):
    assert list(transaction_descriptions(transactions_for_description)) == expected


def test_transaction_descriptions_without_description():
    with pytest.raises(ValueError):
        list(transaction_descriptions([{
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }]))


@pytest.fixture
def number():
    return ["1322 8457 3463 6849",
            "4376 3874 2780 3084",
            "3930 5920 8472 5731"]


@pytest.mark.parametrize("expected", [
    "1322 8457 3463 6849",
    "4376 3874 2780 3084",
    "3930 5920 8472 5731"
])
def test_card_number_generator(expected):
    generator = card_number_generator(1322845734636849, 9999999999999999)
    for expected_number in expected:
        assert next(generator) == expected_number
