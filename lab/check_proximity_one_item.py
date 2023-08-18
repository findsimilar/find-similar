"""
Читает текст из файла и создает токены
"""
import sys

sys.path.append('../')

from database.db_functions import get_all_base_tokens, get_analog_token_by_name, get_base_token_by_id, \
    get_all_base_items
from settings import DICTIONARY, TOP_ELEMENT

from analytics.functions import get_item_find_list

filename = 'tokenize_one.txt'

print('Read data from file...')
with open(filename, 'r', encoding='utf-8') as f:
    line = f.read()

print('Load base items...')
base_list = get_all_base_items()
base_list_tokens = get_all_base_tokens(base_list)
print(f'{len(base_list_tokens)} items loaded')

one = line.strip()
print(f'{one} has been loaded')
one_item = get_analog_token_by_name(one, id_shop=1)
for item in one_item:
    find_list = get_item_find_list(item, base_list_tokens, DICTIONARY)
    print('found:', find_list[TOP_ELEMENT].text)
    item_must_be = get_base_token_by_id(base_list, item.id_base_item)
    print('must be:', item_must_be.text)
    print('one_rating:', find_list.index(item) + 1)