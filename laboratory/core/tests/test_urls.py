"""
Test urls module
"""
from django.test import SimpleTestCase
from django.urls import reverse


class TestUrls(SimpleTestCase):
    """
    Test for urls
    """

    def test_reverse(self):
        """
        Test correct reverce
        """
        app_name = 'core'
        urls = [
            {
                'url': 'index',
                'reverse': ''
            },
        ]
        for url in urls:
            app_url = f'{app_name}:{url["url"]}'
            print("waF")
            print(app_url)
            current_reverse = reverse(app_url)
            print(current_reverse)
            true_reverse = f'/{url["reverse"]}'
            self.assertEqual(current_reverse, true_reverse)
