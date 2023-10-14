"""
Tests for views
"""
from django.urls import reverse
from dry_tests import (
    SimpleTestCase,
    Request,
    TrueResponse,
)
from core.urls import app_name


class TestIndexView(SimpleTestCase):
    """
    Test Index View
    """

    def setUp(self):
        """
        Setup test data
        """
        self.url = reverse(f'{app_name}:index')

    def test_view(self):
        """
        Test main view
        """
        request = Request(
            url=self.url
        )
        true_response = TrueResponse(
            status_code=200,
            content_values=[
                '<h1>Still just main Page...</h1>'
            ]
        )
        current_response = request.get_url_response(self.client)
        self.assertTrueResponse(current_response, true_response)
