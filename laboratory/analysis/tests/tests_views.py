"""
Tests form views
"""
from django.test import SimpleTestCase
from analysis.forms import OneTextForm

URL = '/analysis/tokenize-one/'


class TestTokenizeOneViewGet(SimpleTestCase):
    """
    Test TokenizeOneView GET
    """

    def setUp(self):
        """
        Setup test data
        """
        # self.response = self.client.get(URL)
        self.one = 'oneincdjm2283'
        self.two = 'uekemee68'
        self.text = f'{self.one} {self.two}'

        def get_empty_params():
            return self.client.get(URL)

        def get_with_params():
            return self.client.get(f'{URL}?text={self.text}&token={self.one}&token={self.two}')

        self.response = get_empty_params
        self.param_response = get_with_params

    def test_status_code(self):
        """
        check available
        """
        self.assertEqual(self.response().status_code, 200)

    def test_form_in_context(self):
        """
        check context
        """
        context = self.response().context
        form = 'form'
        self.assertIn(form, context)
        self.assertTrue(isinstance(context[form], OneTextForm))

    def test_form_in_page(self):
        """
        check form on page
        """
        count = 1
        element = 'form'
        self.assertContains(self.response(), f'<{element} method="post">', count)
        self.assertContains(self.response(), f'</{element}>', count)

    def test_response_params(self):
        """
        Test response with params
        And without
        """
        response = self.param_response()
        self.assertContains(response, self.text, 1)
        count = 2  # one in text
        self.assertContains(response, self.one, count)
        self.assertContains(response, self.two, count)
        # without params
        response = self.response()
        self.assertNotContains(response, self.one)
        self.assertNotContains(response, self.text)

    def test_context_params(self):
        """
        Test response context with params
        And without
        """
        # with params
        tokens = 'tokens'
        text = 'text'
        context = self.param_response().context
        # text
        self.assertIn(text, context)
        self.assertEqual(context[text], self.text)
        # tokens
        self.assertIn(tokens, context)
        self.assertEqual(context[tokens], [self.one, self.two])
        # without params
        context = self.response().context
        self.assertNotIn(context[tokens], [])
        self.assertEqual(context[text], '')


class TestTokenizeOneViewPost(SimpleTestCase):
    """
    Test TokenizeOneView POST
    """

    def setUp(self):
        """
        Setup test data
        """
        data = {
            'text': 'one two'
        }
        self.response = self.client.post(URL, data=data)

    def test_valid_redirect(self):
        """
        Test redirect with valid data
        """
        expected_url_params = '?text=one two&token=one&token=two'
        self.assertRedirects(self.response, f'{URL}{expected_url_params}')
