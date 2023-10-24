import os
import pandas as pd
from django.conf import settings


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