import logging

import pandas as pd
from pandas import ExcelFile

from data.data_settings import SHEET_NUMBER, START_ROW, BASE_VENDOR, ContractorInfo
from database.db_functions import insert_item_bulk, insert_shop
from database.db_models import AnalogItem, BaseItem

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO,
)
logger = logging.getLogger(__name__)


def xls_parse(pd_excel: ExcelFile) -> pd.DataFrame:
    pd_dataframe = pd_excel.parse(0)
    return pd_dataframe


def pars_items_bulk(pd_excel: ExcelFile, contractor_info: list[ContractorInfo]):
    pd_dataframe = pd_excel.parse(SHEET_NUMBER, dtype=str)
    values = pd_dataframe.to_numpy()

    items_data = values[START_ROW:]
    spare_parts = []
    spare_analog_parts = []
    special_id = 1
    for contractor in contractor_info:
        contractor.id_shop = insert_shop(contractor.shop_name)
    for item_row in items_data:
        item = BaseItem()
        item.label_text = str(item_row[BASE_VENDOR.label_column_num])
        item.part_number = str(item_row[BASE_VENDOR.part_column_num])
        item.id_shop = 0
        item.special_id = special_id
        spare_parts.append(item)

        for contractor in contractor_info:
            text = str(item_row[contractor.label_column_num])
            if text != 'nan':
                analog_item = AnalogItem()
                analog_item.label_text = text
                analog_item.part_number = str(item_row[contractor.part_column_num])
                analog_item.id_shop = contractor.id_shop
                analog_item.id_base_item = special_id
                spare_analog_parts.append(analog_item)
        special_id = special_id + 1
    insert_item_bulk(spare_parts)
    insert_item_bulk(spare_analog_parts)


def get_contractors(info: dict) -> list[ContractorInfo]:
    contractors_list = []
    for name, columns in info.items():
        contractors_list.append(ContractorInfo(columns[0], columns[1], name))
    return contractors_list