"""
Tests form views
"""
from django.test import SimpleTestCase
from analysis.forms import OneTextForm


class TestTokenizeOneView(SimpleTestCase):
    """
    Test TokenizeOneView
    """

    def setUp(self):
        """
        Setup test data
        """
        url = '/analysis/tokenize-one/'
        self.response = self.client.get(url)

    def test_status_code(self):
        """
        check available
        """
        self.assertEqual(self.response.status_code, 200)

    def test_form_in_context(self):
        """
        check context
        """
        context = self.response.context
        form = 'form'
        self.assertIn(form, context)
        self.assertTrue(isinstance(context[form], OneTextForm))

    def test_form_in_page(self):
        """
        check form on page
        """
        count = 1
        element = 'form'
        self.assertContains(self.response, f'<{element} method="post">', count)
        self.assertContains(self.response, f'</{element}>', count)
