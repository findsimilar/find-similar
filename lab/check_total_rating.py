import os
import sys
from datetime import datetime

sys.path.append('../')

from analytics.functions import check_ratings_total, get_report_total
from analytics.db_functions import get_report_proximity
from database.db_functions import get_all_base_tokens, get_all_analog_tokens, get_all_base_items

from settings import DICTIONARY

print('Load base items...')
base_list = get_all_base_items()
base_list_tokens = get_all_base_tokens(base_list, dictionary=DICTIONARY)
print(f'{len(base_list_tokens)} items loaded')

print('Load analog items...')
analog_list_tokens = get_all_analog_tokens()
print(f'{len(analog_list_tokens)} items loaded')

print('CHECK RATING...')
start_time = datetime.now()
rating_total = check_ratings_total(base_list_tokens, analog_list_tokens, DICTIONARY)
end_time = datetime.now()
time_diff = end_time - start_time

try:
    _, is_save_file, *others = sys.argv
except:
    is_save_file = False
    output = print
else:
    filename = str(datetime.now()).replace(':', '-')
    path = os.path.join('reports', filename)
    f = open(path, 'w', encoding='utf-8')
    output = lambda s: f.write(f'{s}\n')

output('CREATE REPORT')
get_report_total(rating_total, output=output)

output(f'RATING CHECKED for {time_diff}')
if is_save_file:
    if others:
        get_report_proximity(base_list, rating_total, output, edge=5)
    f.close()

print('DONE')
