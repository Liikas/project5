from datetime import datetime
from typing import Dict, List


def filter_by_state(info_list: List[Dict], state: str = 'EXECUTED') -> List[Dict]:
    filtered_list = [item for item in info_list if item.get("state") == state]
    if not filtered_list:
        raise ValueError(f"No items found with state: {state}")
    return filtered_list


def sort_by_date(info_list: List[Dict], reverse: bool = True) -> List[Dict]:
    """The function returns a new list sorted by date"""
    dates = [item["date"] for item in info_list]
    if len(set(dates)) == 1:  # Проверяем, все ли даты одинаковы
        raise ValueError("All dates are the same")
    return sorted(info_list, key=lambda x: x["date"], reverse=reverse)