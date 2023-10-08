"""
Tests
"""
from django.test import SimpleTestCase
from .models import check_find_similar


class FirstTest(SimpleTestCase):
    """
    FirstTest
    """
    def test_check_find_similar(self):
        """
        Test true
        """
        self.assertTrue(check_find_similar())
