from typing import Dict, List


def filter_by_state(info_list: List[Dict],
                    state: str = 'EXECUTED') -> List[Dict]:
    """The function returns the list of dictionaries
    with 'EXECUTED' key state"""
    return [item for item in info_list if item.get("state") == state]


def sort_by_date(info_list: List[Dict], reverse: bool = True) -> List[Dict]:
    """The function returns a new list sorted by date"""
    return sorted(info_list, key=lambda x: x["date"], reverse=True)
