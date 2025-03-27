from datetime import datetime

from masks import get_mask_account, get_mask_card_number


def mask_account_or_card(account_or_card: str) -> str:
    """The function that returns the card number
     with its type and account number"""
    account_or_card_list = account_or_card.split()
    if "Счет" in account_or_card_list:
        return f"Счет {get_mask_account(account_or_card_list[1])}"
    elif ("MasterCard" in account_or_card_list
          or "Maestro" in account_or_card_list):
        return (f"{account_or_card_list[0]}"
                f" {get_mask_card_number(account_or_card_list[1])}")
    elif "Visa" in account_or_card_list:
        card_numbers = []
        card_name = []
        for i in account_or_card_list:
            if i.isdigit():
                card_numbers.append(i)
            if i.isalpha():
                card_name.append(i)
        str_card_numbers = "".join(card_numbers)
        return (f"{card_name[0]} {card_name[1]} "
                f"{get_mask_card_number(str_card_numbers)}")
    else:
        return "Unknown format"


def get_date(the_date: str) -> str:
    """Date conversion function"""
    date_info = datetime.strptime(the_date, "%Y-%m-%dT%H:%M:%S.f")
    return date_info.strftime("%d.%m.%Y")


print(get_date("2024-03-11T02:26:18.671407"))
print(mask_account_or_card("Visa Gold 5999414228426353"))
