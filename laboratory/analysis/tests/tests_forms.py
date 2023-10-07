"""
Tests for forms
"""
from django.test import SimpleTestCase
from analysis.forms import OneTextForm


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
