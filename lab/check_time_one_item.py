import sys
from settings import DICTIONARY

sys.path.append('../')

from database.db_functions import get_all_base_items, get_all_base_tokens
from analytics.functions import check_time

print('Load base items...')

base_list = get_all_base_items()
base_list_tokens = get_all_base_tokens(base_list)

print(f'{len(base_list)} items loaded')

count = 1
time = check_time(number_count=count, base_items_tokens=base_list_tokens, dictionary=DICTIONARY)

print(f'RESULT TIME FOR ONE ITEM (REPEAT {count} times) = {time}')
