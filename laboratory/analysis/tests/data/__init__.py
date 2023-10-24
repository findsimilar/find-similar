import os
import pandas as pd
from django.conf import settings

from analysis.functions import load_training_data


def get_2x2_filepath():
    filepath = os.path.join(settings.BASE_DIR, 'analysis', 'tests', 'data', '2x2.xlsx')
    return filepath


def get_2x2_expected_data():
    data = [
        ['1', '2'],
        ['3', '4'],
    ]
    columns = ['one', 'two']
    expected = pd.DataFrame(data=data, columns=columns)
    return expected


def get_2x2_training_data(name='first'):
    filepath = get_2x2_filepath()
    training_data = load_training_data(name=name, filepath=filepath, sheet_name=0)
    return training_data
