"""
Read text from file and create tokens
"""
import sys

from settings import DICTIONARY, TOP_ELEMENT  # pylint: disable=import-error

sys.path.append("../")

from database.db_functions import (  # pylint: disable=wrong-import-position
    get_all_base_tokens,
    get_analog_token_by_name,
    get_base_token_by_id,
    get_all_base_items,
)
from analytics.functions import get_item_find_list  # pylint: disable=wrong-import-position


SEPARATOR = "///"
FILENAME = "find_similar_one.txt"

print("Read data from file...")
with open(FILENAME, "r", encoding="utf-8") as f:
    line = f.read()

print("Load base items...")
base_list = get_all_base_items()
base_list_tokens = get_all_base_tokens(base_list)
print(f"{len(base_list_tokens)} items loaded")

one, two = line.split(SEPARATOR)
keywords_str = two.split()
keywords = dict(zip(keywords_str, [1]*len(keywords_str)))
print(keywords)
print(f"{one} has been loaded")
one_item = get_analog_token_by_name(one, id_shop=1)
for item in one_item:
    find_list = get_item_find_list(item, base_list_tokens, DICTIONARY, keywords=keywords)
    print(
        "found:",
        find_list[TOP_ELEMENT].text,
        find_list[TOP_ELEMENT].cos,
        find_list[TOP_ELEMENT].key
    )
    item_must_be = get_base_token_by_id(base_list, item.id_base_item)
    print("must be:", item_must_be.text)
    print("one_rating:", find_list.index(item) + 1)
