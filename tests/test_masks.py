import pytest
from src.masks import get_mask_card_number, get_mask_account


@pytest.fixture
def number():
    return ["Visa Classic 7003715386629301",
            "MasterCard 7008236771526363",
            "Visa Platinum 7003236771526253",
            "Visa Gold 7006563454328432"]


@pytest.mark.parametrize("number, expected",
                         [("Visa Classic 7003715386629301",
                           "Visa Classic 7003 71** **** 9301"),
                          ("MasterCard 7008236771526363",
                           "MasterCard 7008 23** **** 6363"),
                          ("Visa Platinum 7003236771526253",
                           "Visa Platinum 7003 23** **** 6253"),
                          ("Visa Gold 7006563454328432",
                           "Visa Gold 7006 56** **** 8432")])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


def test_get_mask_card_number_below_16(number):
    with pytest.raises(ValueError):
        get_mask_card_number("America Express 700656345432843")


def test_get_mask_card_number_below_14(number):
    with pytest.raises(ValueError):
        get_mask_card_number("Golden 7008236771526")


def test_get_mask_card_number_after_16(number):
    with pytest.raises(ValueError):
        get_mask_card_number("European 7008236771526363483")


def test_get_mask_card_number_if_empty(number):
    with pytest.raises(ValueError):
        get_mask_card_number("")


def test_get_mask_card_number_if_not_digit(number):
    with pytest.raises(ValueError):
        get_mask_card_number("Visa Gold")


@pytest.fixture
def account():
    return ["Счет 64686473678894779589",
            "Счет 35383033474447895560",
            "Счет 73654108430135874305"]


@pytest.mark.parametrize("account, expected",
                         [("Счет 64686473678894779589",
                           "Счет **9589"),
                          ("Счет 35383033474447895560",
                           "Счет **5560"),
                          ("Счет 73654108430135874305",
                           "Счет **4305")])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected


def test_get_mask_account_below_20(account):
    with pytest.raises(ValueError):
        get_mask_account("Счет 7365410843013587430")


def test_get_mask_account_after_20(account):
    with pytest.raises(ValueError):
        get_mask_account("Счет 646864736788947795893")


# p.s. я много раз пыталась переделать так чтобы здесь использовался
# TypeError, но что бы я ни делала он всегда слетал, поэтому тут ValueError
def test_get_mask_account_if_not_digit(account):
    with pytest.raises(ValueError):
        get_mask_account("Счет шесть четыре восемь ")


def test_get_mask_account_if_empty(account):
    with pytest.raises(ValueError):
        get_mask_account("")


def test_get_mask_account_if_additional_symbols(account):
    with pytest.raises(ValueError):
        get_mask_account("Счет 3538-3033-4744-4789-5560")

