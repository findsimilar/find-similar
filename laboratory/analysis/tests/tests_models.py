import pandas as pd
from django.test import TestCase, SimpleTestCase
from analysis.models import TrainingData, to_list
from analysis.tests.data import get_2x2_expected_data


class TrainingDataTestCase(TestCase):

    def setUp(self):
        self.dataframe = get_2x2_expected_data()
        self.unique_id = 'some unique id'
        self.training_data = TrainingData(
            name=self.unique_id,
            data=self.dataframe.to_json(),
        )

    def test_save(self):
        self.assertEqual(self.training_data.name, self.unique_id)
        get_data = pd.read_json(self.training_data.data, dtype=str)

        self.assertTrue(self.dataframe.equals(get_data))

    def test_data_from_json(self):
        self.assertTrue(self.dataframe.equals(self.training_data.get_dataframe()))

    def test_count(self):
        self.assertEqual(len(self.training_data.get_dataframe().columns), 2)
        self.assertEqual(len(self.training_data.get_dataframe().index), 2)
        self.assertEqual(self.training_data.columns_count, 2)
        self.assertEqual(self.training_data.rows_count, 2)


class FunctionsSimpleTestCase(SimpleTestCase):

    def test_to_list(self):
        dataframe = pd.DataFrame(
            [
                [1, 2],
                [3, 4],
            ]
        )
        self.assertEqual(to_list(dataframe), [1, 3, 2, 4])
