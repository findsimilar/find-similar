import pandas as pd


def load_from_excel(filepath, sheet_name=0):
    pd_excel = pd.ExcelFile(filepath)
    loaded_frame = pd_excel.parse(sheet_name, dtype=str)
    return loaded_frame
