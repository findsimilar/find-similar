"""
Tests for Analysis functions
"""
from django.test import SimpleTestCase

from analysis.functions import analyze_one_item


class TestFunctions(SimpleTestCase):
    """
    Class for test all functions
    """
    def setUp(self):
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
        text = 'one two'
        tokens = analyze_one_item('one two', printer=self.testing_printer)
        expected_tokens = {'one', 'two'}
        self.assertEqual(tokens, expected_tokens)
        excepted_prints = [
            f'Get tokens for {text}...',
            'Done:',
            f'{expected_tokens}',
            'End',
        ]
        self.assertEqual(self.testing_printer.results, excepted_prints)
