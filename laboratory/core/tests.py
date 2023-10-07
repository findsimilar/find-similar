"""
Tests
"""
from django.test import TestCase
from .models import check_find_similar


class FirstTest(TestCase):
    """
    FirstTest
    """
    def test_check_find_similar(self):
        """
        Test true
        """
        self.assertTrue(check_find_similar())
