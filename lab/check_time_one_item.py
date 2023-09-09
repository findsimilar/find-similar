"""
Check time one item loaded
"""
import sys
from settings import DICTIONARY  # pylint: disable=import-error

sys.path.append("../")

from database.db_functions import get_all_base_items, get_all_base_tokens  # pylint: disable=wrong-import-position
from analytics.functions import check_time  # pylint: disable=wrong-import-position

print("Load base items...")

base_list = get_all_base_items()
base_list_tokens = get_all_base_tokens(base_list)

print(f"{len(base_list)} items loaded")

COUNT = 1
time = check_time(
    number_count=COUNT, base_items_tokens=base_list_tokens, dictionary=DICTIONARY
)

print(f"RESULT TIME FOR ONE ITEM (REPEAT {COUNT} times) = {time}")
