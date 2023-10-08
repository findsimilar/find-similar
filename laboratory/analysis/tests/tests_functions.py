"""
Tests for Analysis functions
"""
from django.test import SimpleTestCase

from analysis.functions import analyze_one_item, analyze_two_items


class TestFunctions(SimpleTestCase):
    """
    Class for test all functions
    """
    def setUp(self):
        self.one = 'one'
        self.two = 'two'
        self.one_two = 'one two'
        self.printer = print

        def mock_printer(*args, **kwargs):  # pylint: disable=unused-argument
            """
            This is mock printer. This printer do nothing
            """

        self.mock_printer = mock_printer

        class TestingPrinter:
            """
            Save prints to variable. To check the results
            """

            def __init__(self):
                """
                Init printer
                """
                self.results = []

            def __call__(self, text, *args, **kwargs):
                self.results.append(str(text))

        self.testing_printer = TestingPrinter()

    def test_analyze_one_item(self):
        """
        Test for analyze one item
        """
        tokens = analyze_one_item(self.one_two, printer=self.testing_printer)
        expected_tokens = {self.one, self.two}
        self.assertEqual(tokens, expected_tokens)
        expected_prints = [
            f'Get tokens for {self.one_two}...',
            'Done:',
            f'{expected_tokens}',
            'End',
        ]
        self.assertEqual(self.testing_printer.results, expected_prints)

    def test_analyze_two_items(self):
        """
        Test for analyze_two_items
        """
        similar_cos = 1.0
        different_cos = 0.0
        self.assertEqual(
            analyze_two_items(self.one, self.one, printer=self.mock_printer),
            similar_cos
        )
        self.assertEqual(
            analyze_two_items(self.one, self.two, printer=self.testing_printer),
            different_cos)
        one_tokens = {self.one}
        two_tokens = {self.two}
        # prints
        expected_prints = [
            f'Get cos between "{self.one}" and "{self.two}"',
            f'Get tokens for {self.one}...',
            'Done:',
            f'{one_tokens}',
            'End',
            f'Get tokens for {self.two}...',
            'Done:',
            f'{two_tokens}',
            'End',
            'Done',
            f'cos = {different_cos}',
            'End',
        ]
        self.assertEqual(self.testing_printer.results, expected_prints)
