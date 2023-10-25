"""
Test urls module
"""
from django.test import SimpleTestCase, TestCase
from django.urls import reverse

from analysis.tests.data import get_2x2_training_data


class TestUrlsSimpleTestCase(SimpleTestCase):
    """
    Test Urls Class
    """

    def test_reverse(self):
        """
        Test correct reverse
        """
        app_name = 'analysis'
        urls = [
            {
                'url': 'tokenize_one',
                'reverse': 'tokenize-one/'
            },
            {
                'url': 'compare_two',
                'reverse': 'compare-two/',
            },
            {
                'url': 'example_frequency',
                'reverse': 'example-frequency/',
            },
            {
                'url': 'load_training_data',
                'reverse': 'load-training-data/',
            },
            {
                'url': 'training_data_list',
                'reverse': 'training-data-list/',
            },
        ]
        for url in urls:
            app_url = f'{app_name}:{url["url"]}'
            current_reverse = reverse(app_url)
            true_reverse = f'/{app_name}/{url["reverse"]}'
            with self.subTest(msg=app_url):
                self.assertEqual(current_reverse, true_reverse)


class TestUrlsTestCase(TestCase):
    """
    Test Urls Class With DB
    """

    def test_reverse(self):
        """
        Test correct reverse
        """

        training_data = get_2x2_training_data()

        app_name = 'analysis'
        urls = [
            {
                'url': 'training_data',
                'kwargs': {
                    'pk': training_data.pk
                },
                'reverse': f'training-data/{training_data.pk}/',
            },
            {
                'url': 'delete_training_data',
                'kwargs': {
                    'pk': training_data.pk
                },
                'reverse': f'delete-training-data/{training_data.pk}/',
            },
            {
                'url': 'find_similar',
                'kwargs': {
                    'pk': training_data.pk
                },
                'reverse': f'find-similar/{training_data.pk}/',
            },
        ]
        for url in urls:
            app_url = f'{app_name}:{url["url"]}'
            current_reverse = reverse(app_url, kwargs=url['kwargs'])
            true_reverse = f'/{app_name}/{url["reverse"]}'
            with self.subTest(msg=app_url):
                self.assertEqual(current_reverse, true_reverse)
