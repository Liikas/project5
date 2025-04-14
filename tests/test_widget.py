import pytest

from src.widget import get_date, mask_account_or_card


@pytest.fixture
def number():
    return ["Visa Classic 7003715386629301",
            "MasterCard 7008236771526363",
            "Счет 35383033474447895560"]


@pytest.mark.parametrize("number, expected",
                         [("Visa Classic 7003715386629301",
                           "Visa Classic 7003 71** **** 9301"),
                          ("MasterCard 7008236771526363",
                           "MasterCard 7008 23** **** 6363"),
                          ("Счет 35383033474447895560",
                           "Счет **5560")])
def test_mask_account_or_card(number, expected):
    assert mask_account_or_card(number) == expected


def test_mask_account_or_card_short_card_number(number):
    with pytest.raises(ValueError):
        mask_account_or_card("Visa Classic 700371538662301")


def test_mask_account_or_card_short_account_number(number):
    with pytest.raises(ValueError):
        mask_account_or_card("Счет 3538303347444789556")


def test_mask_account_or_card_wrong_account_name(number):
    with pytest.raises(ValueError):
        mask_account_or_card("Счт 35383033474447895560")


@pytest.fixture
def data():
    return ["2024-03-11T02:26:18.671407",
            "2016-05-31T05:58:16.345527"]


@pytest.mark.parametrize("data, expected",
                         [("2024-03-11T02:26:18.671407", "11.03.2024"),
                          ("2016-05-31T05:58:16.345527", "31.05.2016")])
def test_get_date(data, expected):
    assert get_date(data) == expected


def test_get_data_wrong_format(data):
    with pytest.raises(ValueError):
        get_date("02:26:18.671407T2024-03-11")


def test_get_data_without_data(data):
    with pytest.raises(ValueError):
        get_date("T05:58:16.345527")


def test_get_data_only_data(data):
    with pytest.raises(ValueError):
        get_date("2016-05-31")


def test_get_data_without_t(data):
    with pytest.raises(ValueError):
        get_date("2016-05-3105:58:16.345527")
