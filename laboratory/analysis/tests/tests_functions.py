"""
Tests for Analysis functions
"""
from django.test import SimpleTestCase

from analysis.functions import (
    Printer,
    analyze_one_item,
    analyze_two_items,
    example_frequency_analysis,
    total_rating,
)


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

    def test_printer_function_without_printer(self):
        """
        Test printer when function hasn't got params
        """
        @Printer(printer=self.testing_printer)
        def some_func():
            """
            Do something usefull
            """

        result = some_func()
        expected_prints = [
            'Start',
            'Done:',
            f'{result}',
            'End'
        ]
        self.assertEqual(self.testing_printer.results, expected_prints)

    def test_printer_function_with_printer_kwargs(self):
        """
        Test printer when send printer dirrectly in function
        """
        @Printer()
        def some_func(printer=print):  # pylint: disable=unused-argument
            """
            Do something usefull
            """

        result = some_func(printer=self.testing_printer)
        expected_prints = [
            'Start',
            'Done:',
            f'{result}',
            'End'
        ]
        self.assertEqual(self.testing_printer.results, expected_prints)

    def test_printer_simple_title(self):
        """
        Test printer then we sent simple str title
        """
        simple_title = 'Simple title'

        @Printer(title=lambda **kwargs: simple_title, printer=self.testing_printer)
        def some_func():
            """
            Do something usefull
            """

        result = some_func()
        expected_prints = [
            'Start',
            simple_title,
            'Done:',
            f'{result}',
            'End'
        ]
        self.assertEqual(self.testing_printer.results, expected_prints)

    def test_printer_param_title(self):
        """
        Test wen we sent title and function has a param
        """
        @Printer(title=lambda param, **kwargs: f'Title {param}')
        def some_func(param, printer=print):  # pylint: disable=unused-argument
            """
            Do something usefull
            """


        result = some_func('A', printer=self.testing_printer)
        expected_prints = [
            'Start',
            'Title A',
            'Done:',
            f'{result}',
            'End'
        ]
        self.assertEqual(self.testing_printer.results, expected_prints)

    def test_analyze_one_item(self):
        """
        Test for analyze one item
        """
        tokens = analyze_one_item(  # pylint: disable=unexpected-keyword-arg
            self.one_two,
            printer=self.testing_printer
        )
        expected_tokens = {self.one, self.two}
        self.assertEqual(tokens, expected_tokens)

    def test_analyze_two_items(self):
        """
        Test for analyze_two_items
        """
        similar_cos = 1.0
        different_cos = 0
        self.assertEqual(
            analyze_two_items(  # pylint: disable=unexpected-keyword-arg
                self.one,
                self.one,
                printer=self.mock_printer,
                is_pass_printer=True,
            ),
            similar_cos
        )
        self.assertEqual(
            analyze_two_items(  # pylint: disable=unexpected-keyword-arg
                self.one,
                self.two,
                printer=self.testing_printer,
                is_pass_printer=True,
            ),
            different_cos)
        one_tokens = {self.one}
        two_tokens = {self.two}
        # prints
        expected_prints = [
            'Start',
            f'Get cos between '
            f'"{self.one}" and "{self.two}"',
            'Start',
            f'Get tokens for {self.one}...',
            'Done:',
            f'{one_tokens}',
            'End',
            'Start',
            f'Get tokens for {self.two}...',
            'Done:',
            f'{two_tokens}',
            'End',
            'Done:',
            f'{different_cos}',
            'End',
        ]
        self.assertEqual(self.testing_printer.results, expected_prints)

    def test_example_frequency_analysis(self):
        """
        Test for example_frequency_analysis
        """
        example_name = 'mock'
        expected_result = (('mock', 2),
            ('example', 2),
            ('for', 2),
            ('tests', 2),
            ('this', 1),
            ('is', 1))
        self.assertEqual(example_frequency_analysis(  # pylint: disable=unexpected-keyword-arg
            example_name,
            printer=self.testing_printer
        ), expected_result)

    def test_use_match_list(self):
        match_list = [
            [
                'one', 'uno', 'one or uno',
            ],
            [
                'two', 'dos', 'two or dos'
            ]
        ]

        def find_similar_mock(  # pylint: disable=too-many-arguments
                text_to_check,
                texts,
                language="russian",
                count=5,
                dictionary=None,
                remove_stopwords=True,
                keywords=None,
        ):
            return [
                {'name': 'one', 'cos': 1.0},
                {'name': 'two', 'cos': 1.0},
                {'name': 'uno', 'cos': 0.9},
                {'name': 'one or uno', 'cos': 0.5},
                {'name': 'dos', 'cos': 0.0},
                {'name': 'two or dos', 'cos': 0.0},
            ]

        to_search = ['one', 'two']
        results = total_rating(to_search, match_list, find_similar_mock)
        excepted_results = {
            'one': '2/3',
            'two': '1/3',
        }
        self.assertEqual(results, excepted_results)