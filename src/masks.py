from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """The function of masking card number"""
    card_number_str = str(card_number)
    if len(card_number_str) != 16:
        return "Enter 16-digit card number"
    elif not card_number_str.isdigit():
        return "The card number must be digits only"
    else:
        return f"{card_number_str[:4]} {card_number_str[4:6]}** **** {card_number_str[-4:]}"


def get_mask_account(account_info: Union[str, int]) -> str:
    """The function of masking account number"""
    account_info_str = str(account_info)
    if len(account_info_str) != 20:
        return "Enter 20-digit account number"
    elif not account_info_str.isdigit():
        return "The account number must be digits only"
    else:
        return f"**{account_info_str[-4:]}"
