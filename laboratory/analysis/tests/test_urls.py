"""
Test urls module
"""
from django.test import SimpleTestCase
from django.urls import reverse


class TestUrls(SimpleTestCase):
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
            }
        ]
        for url in urls:
            app_url = f'{app_name}:{url["url"]}'
            current_reverse = reverse(app_url)
            true_reverse = f'/{app_name}/{url["reverse"]}'
            with self.subTest(msg=app_url):
                self.assertEqual(current_reverse, true_reverse)
