"""
Tests for forms
"""
from django.test import SimpleTestCase
from analysis.forms import (
    OneTextForm,
    TwoTextForm,
)


class TestOneTextForm(SimpleTestCase):
    """
    One text form test
    """

    def test_fields(self):
        """
        Test available fields
        """
        form = OneTextForm()
        self.assertEqual(len(form.fields), 1)
        self.assertIn('text', form.fields)


class TestTwoTextForm(SimpleTestCase):
    """
    One text form test
    """

    def test_fields(self):
        """
        Test available fields
        """
        form = TwoTextForm()
        self.assertEqual(len(form.fields), 2)
        self.assertIn('one_text', form.fields)
        self.assertIn('two_text', form.fields)
