"""
Load data to database from file
"""
import sys
import pandas as pd
from settings import DICTIONARY  # pylint: disable=import-error

# add parent folder to path to run script and make imports
sys.path.append("../")

from data.data_functions import pars_items_bulk, get_contractors  # pylint: disable=wrong-import-position
from database.db_functions import create_all, generate_tokens  # pylint: disable=wrong-import-position

# get path to file
try:
    _, filepath, contractor_name = sys.argv  # pylint: disable=unbalanced-tuple-unpacking
# TODO: except more concrete exception
except Exception:  # pylint: disable=broad-exception-caught
    print(
        "Please specify a path to file "
        "(python load_data_from_file /some_path/some_file.xlsx) "
        "AND contractor name"
    )
    sys.exit(0)

print("Create database tables from metadata...")
create_all()

print("Open xlsx file...")
xls = pd.ExcelFile(filepath)

contractor_selected = None  # pylint: disable=invalid-name
all_contractors = get_contractors({})
for contractor in all_contractors:
    if contractor_name == contractor.shop_name:
        contractor_selected = [contractor]

if contractor_selected is None:
    contractor_selected = all_contractors

print(f"Parse items for {[x.shop_name for x in contractor_selected]}...")
pars_items_bulk(xls, contractor_selected)
print("Generate tokens...")

generate_tokens(dictionary=DICTIONARY)
print("DONE")
