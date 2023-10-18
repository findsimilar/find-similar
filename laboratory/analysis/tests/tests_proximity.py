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
)


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


class ProximitySimpleTestCase(SimpleTestCase):
    """
    Test proximity class
    """
    def setUp(self):
        self.a = 'a'
        self.known_data_1x1 = np.matrix([self.a], dtype=str)

        @dataclass
        class Token:
            text: str
            cos: float

        def find_similar_1x1(text, texts):
            return [
                Token(text=self.a, cos=1.0)
            ]

        # self.find_similar_1x1 = find_similar_1x1
        self.find_similar_1x1 = settings.FIND_SIMILAR


    def test_calc_value_position_1x1(self):
        proximity = calc_value_position(self.known_data_1x1, find_similar=self.find_similar_1x1, value=self.a)
        self.assertEqual(proximity, 0)


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
