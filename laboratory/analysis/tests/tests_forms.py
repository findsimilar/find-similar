"""
Tests for forms
"""
from django import forms
from dry_tests.testcases import SimpleTestCase
from dry_tests.models import Fields, TrueForm
from analysis.forms import (
    OneTextForm,
    TwoTextForm,
    LoadTrainingDataForm,
)


class TestOneTextForm(SimpleTestCase):
    """
    One text form test
    """

    def test_fields(self):
        """
        Test available fields
        """

        true_form = TrueForm(
            fields=Fields(
                count=1,
                types={
                    'text': forms.CharField
                }
            )
        )

        current_form = OneTextForm()
        self.assertTrueForm(current_form, true_form)


class TestTwoTextForm(SimpleTestCase):
    """
    One text form test
    """

    def test_fields(self):
        """
        Test available fields
        """
        true_form = TrueForm(
            fields=Fields(
                count=2,
                types={
                    'one_text': forms.CharField,
                    'two_text': forms.CharField,
                }
            )
        )

        current_form = TwoTextForm()
        self.assertTrueForm(current_form, true_form)


class LoadTrainingDataFormSimpleTestCase(SimpleTestCase):
    """
    Load traning data test
    """

    def test_fields(self):
        """
        Test available fields
        """
        true_form = TrueForm(
            fields=Fields(
                count=2,
                types={
                    'name': forms.CharField,
                    'excel_file': forms.FileField,
                }
            )
        )

        current_form = LoadTrainingDataForm()
        self.assertTrueForm(current_form, true_form)