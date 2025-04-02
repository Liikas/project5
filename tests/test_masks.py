import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def number():
    return ["7003715386629301",
            "7008236771526363",
            "7003236771526253",
            "7006563454328432"]


@pytest.mark.parametrize("number, expected",
                         [("7003715386629301",
                           "7003 71** **** 9301"),
                          ("7008236771526363",
                           "7008 23** **** 6363"),
                          ("7003236771526253",
                           "7003 23** **** 6253"),
                          ("7006563454328432",
                           "7006 56** **** 8432")])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


def test_get_mask_card_number_below_16(number):
    with pytest.raises(ValueError):
        get_mask_card_number("700656345432843")


def test_get_mask_card_number_below_14(number):
    with pytest.raises(ValueError):
        get_mask_card_number("7008236771526")


def test_get_mask_card_number_after_16(number):
    with pytest.raises(ValueError):
        get_mask_card_number("7008236771526363483")


def test_get_mask_card_number_if_empty(number):
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_card_number_if_not_digit(number):
    with pytest.raises(ValueError):
        get_mask_card_number("Visa Gold")


@pytest.fixture
def account():
    return ["64686473678894779589",
            "35383033474447895560",
            "73654108430135874305"]


@pytest.mark.parametrize("account, expected",
                         [("64686473678894779589",
                           "**9589"),
                          ("35383033474447895560",
                           "**5560"),
                          ("73654108430135874305",
                           "**4305")])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


def test_get_mask_account_below_20(account):
    with pytest.raises(ValueError):
        get_mask_account("7365410843013587430")


def test_get_mask_account_after_20(account):
    with pytest.raises(ValueError):
        get_mask_account("646864736788947795893")


def test_get_mask_account_if_not_digit(account):
    with pytest.raises(TypeError):
        get_mask_account("шесть четыре восемь ")


def test_get_mask_account_if_empty(account):
    with pytest.raises(ValueError):
        get_mask_account("")


def test_get_mask_account_if_additional_symbols(account):
    with pytest.raises(ValueError):
        get_mask_account("3538-3033-4744-4789-5560")

