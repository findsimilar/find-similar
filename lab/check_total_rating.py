"""
Check total rating for all database data
"""
import os
import sys
from datetime import datetime
from settings import DICTIONARY  # pylint: disable=import-error

sys.path.append("../")

from analytics.functions import check_ratings_total, get_report_total  # pylint: disable=wrong-import-position
from analytics.db_functions import get_report_proximity  # pylint: disable=wrong-import-position
from database.db_functions import (  # pylint: disable=wrong-import-position
    get_all_base_tokens,
    get_all_analog_tokens,
    get_all_base_items,
)



print("Load base items...")
base_list = get_all_base_items()
base_list_tokens = get_all_base_tokens(base_list, dictionary=DICTIONARY)
print(f"{len(base_list_tokens)} items loaded")

print("Load analog items...")
analog_list_tokens = get_all_analog_tokens()
print(f"{len(analog_list_tokens)} items loaded")

print("CHECK RATING...")
start_time = datetime.now()
rating_total = check_ratings_total(base_list_tokens, analog_list_tokens, DICTIONARY)
end_time = datetime.now()
time_diff = end_time - start_time

try:
    _, is_save_file, *others = sys.argv
except ValueError:
    is_save_file = False  # pylint: disable=invalid-name
    output = print
else:
    filename = str(datetime.now()).replace(":", "-")  # pylint: disable=invalid-name
    path = os.path.join("reports", filename)
    f = open(path, 'w', encoding='utf-8')  # pylint: disable=consider-using-with
    output = lambda s: f.write(f'{s}\n')  # pylint: disable=unnecessary-lambda-assignment
    # with open(path, "w", encoding="utf-8") as f:
    #     output = lambda s: f.write(f"{s}\n")  # pylint: disable=unnecessary-lambda-assignment

output("CREATE REPORT")
get_report_total(rating_total, output=output)

output(f"RATING CHECKED for {time_diff}")
if is_save_file:
    if others:
        get_report_proximity(base_list, rating_total, output, edge=5)
    f.close()

print("DONE")
