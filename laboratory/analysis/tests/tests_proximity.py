"""
Test for proximity calculation module
"""
from dataclasses import dataclass
import numpy as np
from django.test import SimpleTestCase
from django.conf import settings
from analysis.proximity import (
    calc_proximity,
    calc_value_position,
    calc_values_position,
    # calc_positions_for_column,
    array_to_row_list,
)
from analysis.tests.data import Token


class NumpyTestCase(SimpleTestCase):

    def test_shape(self):
        np1x2 = np.matrix([1, 2])
        self.assertEqual(np1x2.shape, (1, 2))

    def test_to_list_one_row(self):
        np2x2 = np.matrix([[1, 2], [3, 4]])
        self.assertEqual(np2x2.shape, (2, 2))
        self.assertEqual(np2x2.size, 4)
        one_row_list = np2x2.reshape(1, np2x2.size).tolist()[0]
        self.assertEqual(one_row_list, [1, 2, 3, 4])

    def test_get_column(self):
        np2x2 = np.matrix([[1, 2], [3, 4]])
        zero_column = np2x2[:, 0]
        self.assertEqual(array_to_row_list(zero_column),[1, 3])



class ProximitySimpleTestCase(SimpleTestCase):
    """
    Test proximity class
    """
    def setUp(self):
        self.a = 'a'
        self.b = 'b'
        self.known_data_1x1 = np.matrix([self.a], dtype=str)
        self.known_data_2x1 = np.matrix([self.a, self.b], dtype=str)
        self.known_data_1x2 = np.matrix([[self.a], [self.b]], dtype=str)

        # @dataclass
        # class Token:
        #     text: str
        #     cos: float

        def find_similar_1x1(text, texts):
            return [
                Token(text=self.a, cos=1.0)
            ]

        def find_similar_2x1(text, texts):
            return [
                Token(text=self.a, cos=1.0),
                Token(text=self.b, cos=0.0),
            ]


        self.find_similar_1x1 = find_similar_1x1
        self.find_similar_2x1 = find_similar_2x1
        # self.find_similar_1x1 = settings.FIND_SIMILAR


    def test_calc_value_position_1x1(self):
        proximity = calc_value_position(self.known_data_1x1, find_similar=self.find_similar_1x1, value=self.a)
        # 0 - position of sorted element
        self.assertEqual(proximity, 0)

    def test_calc_value_position_2x1(self):
        # a
        proximity = calc_value_position(self.known_data_2x1, find_similar=self.find_similar_2x1, value=self.a)
        # 0 - position of sorted element
        self.assertEqual(proximity, 0)
        # b
        proximity = calc_value_position(self.known_data_2x1, find_similar=self.find_similar_2x1, value=self.b)
        # 0 - position of sorted element
        self.assertEqual(proximity, 1)
        # 1x2
        proximity = calc_value_position(self.known_data_1x2, find_similar=self.find_similar_2x1, value=self.b)
        # No matter size of matrix
        self.assertEqual(proximity, 1)

    def test_calc_values_position(self):
        proximities = calc_values_position(self.known_data_1x1, find_similar=self.find_similar_1x1, values=[self.a])
        self.assertEqual(proximities, [0])
        proximities = calc_values_position(self.known_data_2x1, find_similar=self.find_similar_2x1, values=[self.a])
        self.assertEqual(proximities, [0])
        proximities = calc_values_position(self.known_data_2x1, find_similar=self.find_similar_2x1, values=[self.a, self.b])
        self.assertEqual(proximities, [0, 1])
        proximities = calc_values_position(self.known_data_2x1, find_similar=self.find_similar_2x1,
                                          values=[self.b, self.a])
        self.assertEqual(proximities, [1, 0])

    # def test_calc_position_for_column(self):
    #     positions = calc_positions_for_column(self.known_data_1x1, find_similar=self.find_similar_1x1, column=0)
    #     self.assertEqual(positions, [0])
    #     positions = calc_positions_for_column(self.known_data_2x1, find_similar=self.find_similar_2x1, column=0)
    #     self.assertEqual(positions, [1, 0])

    # def test_calc_values_position(self):
    #     proximities = calc_positions_for_column(self.known_data_1x1, find_similar=self.find_similar_1x1, column=1)


    def test_1x1(self):
        """
        test 1 x 1 matrix
        """
        proximity = calc_proximity(self.known_data_1x1, find_similar=self.find_similar_1x1)
        self.assertTrue(np.array_equal(proximity, [np.matrix([1])]))

    # def test_1x2(self):
    #     known_data = np.matrix(['a', 'b'])
    #     proximity = calc_proximity(known_data, find_similar=lambda x: None)
    #     result = np.matrix([1, 1])
    #
    #     self.assertEqual(result.shape, proximity.shape)
    #     self.assertTrue(np.array_equal(proximity, result))
