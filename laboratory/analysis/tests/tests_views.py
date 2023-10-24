"""
Tests for views
"""
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from dry_tests import (
    TestCase,
    SimpleTestCase,
    Request,
    TrueResponse,
    ContentValue,
    Context,
    POST,
)
from analysis.forms import OneTextForm, TwoTextForm, LoadTrainingDataForm
from analysis.models import TrainingData
from analysis.tests.data import get_2x2_filepath, get_2x2_training_data
from analysis.urls import app_name
from analysis.functions import load_training_data


FORM_CONTENT_VALUES = [
                ContentValue(
                    value='<form method="post">',
                    count=1,
                ),
                ContentValue(
                    value='</form>',
                    count=1,
                ),
            ]


class TestTokenizeOneView(SimpleTestCase):
    """
    Test class for One View
    """
    def setUp(self):
        """
        Set Up Test Data
        """
        self.url = reverse(f'{app_name}:tokenize_one')
        self.one = 'one'
        self.two = 'two'
        self.text = f'{self.one} {self.two}'
        expected_url_params = f'?text={self.text}&token={self.one}&token={self.two}'
        self.redirect_url=f'{self.url}{expected_url_params}'

    def test_get(self):
        """
        Test Get
        """
        request = Request(
            url=self.url
        )
        true_response = TrueResponse(
            status_code=200,
            context=Context(
                types={'form': OneTextForm}
            ),
            content_values=FORM_CONTENT_VALUES
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)
        # extended check

        # With params
        request = Request(
            url=self.redirect_url
        )
        true_response = TrueResponse(
            context=Context(
                items={
                    'tokens': [self.one, self.two],
                    'text': self.text
                }
            ),
            content_values=[
                ContentValue(
                    value=self.one,
                ),
                ContentValue(
                    value=self.two,
                ),
            ]
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

    def test_post(self):
        """
        Test Post
        """
        data = {
            'text': self.text
        }
        request = Request(
            url=self.url,
            method=POST,
            data=data,
        )
        true_response = TrueResponse(
            status_code=302,
            redirect_url=self.redirect_url
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)


class TestCompareTwo(SimpleTestCase):
    """
    Test Compare Two
    """

    def setUp(self):
        """
        Set Up Test Data
        """
        self.url = reverse(f'{app_name}:compare_two')
        expected_url_params = '?one_text=one&two_text=one&cos=1.0'
        self.redirect_url=f'{self.url}{expected_url_params}'

    def test_get(self):
        """
        Test Get
        """
        request = Request(
            url=self.url
        )
        true_response = TrueResponse(
            status_code=200,
            context=Context(
                keys=['form'],
                types={
                    'form': TwoTextForm,
                }
            ),
            content_values=FORM_CONTENT_VALUES
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

        data_items = {
                    'one_text': 'one',
                    'two_text': 'one',
                    'cos': '1.0',
                }

        request = Request(
            url=self.redirect_url
        )
        true_response = TrueResponse(
            status_code=200,
            context=Context(
                items=data_items
            ),
            content_values=[
                'one', '1.0'
            ]
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

    def test_post(self):
        """
        Test Post
        """
        data = {
            'one_text': 'one',
            'two_text': 'one',
        }
        request = Request(
            url=self.url,
            method=POST,
            data=data,
        )
        true_response = TrueResponse(
            status_code=302,
            redirect_url=self.redirect_url
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)


class TestExampleFrequencyView(SimpleTestCase):
    """
    Test Example Frequency View
    """

    def setUp(self):
        """
        SetUp Test Data
        """
        self.text = 'mock'
        self.url = reverse('analysis:example_frequency')
        self.result = (('mock', 2), ('example', 2),
                       ('for', 2), ('tests', 2), ('this', 1), ('is', 1))
        expected_url_params = []
        for key, value in self.result:
            expected_url_params.append(f'{key}={value}')
        self.expected_url_params = f'?text={self.text}&{"&".join(expected_url_params)}'
        self.redirect_url=f'{self.url}{self.expected_url_params}'

    def test_get(self):
        """
        Test get
        """
        request = Request(
            url=self.url
        )
        true_response = TrueResponse(
            status_code=200,
            context=Context(
                keys=['form'],
                types={'form': OneTextForm},
            ),
            content_values=FORM_CONTENT_VALUES
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

        request = Request(
            url=self.redirect_url
        )

        content_values = [self.text]
        for key, value in self.result:
            content_values.append(key)
            content_values.append(value)

        true_response = TrueResponse(
            status_code=200,
            context=Context(
                items={
                    'text': self.text,
                    'result': self.result,
               }
            ),
            content_values=content_values
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

        # Error
        request = Request(
            url=f'{self.url}?text={self.text}&error=some error'
        )

        true_response = TrueResponse(
            status_code=200,
            context=Context(
                items={
                    'text': self.text,
                    'error': 'some error',
                }
            ),
            content_values=[
                'Some Error'
            ]
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

    def test_post(self):
        """
        Test post
        """
        data = {
            'text': self.text
        }
        request = Request(
            url=self.url,
            method=POST,
            data=data,
        )

        true_response = TrueResponse(
            status_code=302,
            redirect_url=self.redirect_url
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

    def test_post_error_example(self):
        """
        Test post with error example
        """
        data = {
            'text': 'unknown example value'
        }
        request = Request(
            url=self.url,
            method=POST,
            data=data,
        )

        true_response = TrueResponse(
            status_code=302,
            redirect_url=f'{self.url}?text=unknown example value&error=example not found'
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)


class LoadTrainingDataViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('analysis:load_training_data')

    def test_get(self):
        request = Request(
            url=self.url,
        )
        true_response = TrueResponse(
            status_code=200,
            context=Context(
                keys=['form'],
                types={
                    'form': LoadTrainingDataForm
                },
            ),
            content_values=[
                ContentValue(
                    value='<form method="post" enctype="multipart/form-data">',
                    count=1,
                ),
                ContentValue(
                    value='</form>',
                    count=1,
                ),
            ],
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

    def test_post(self):
        filepath = get_2x2_filepath()
        excel_file = SimpleUploadedFile(filepath, open(filepath, 'rb').read())
        name = 'first'
        data = {
            'name': name,
            'excel_file': excel_file,
        }
        request = Request(
            url=self.url,
            method=POST,
            data=data,
        )
        true_response = TrueResponse(
            status_code=302,
        )

        self.assertFalse(TrainingData.objects.filter(name=name).exists())

        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)
        # true model has been created

        self.assertTrue(TrainingData.objects.filter(name=name).exists())

        training_data = TrainingData.objects.get(name=name)
        redirect_url = reverse('analysis:training_data', kwargs={'pk': training_data.pk})
        true_response = TrueResponse(
            redirect_url=redirect_url,
        )
        self.assertTrueResponse(current_response, true_response)


class TrainingDataDetailViewTestCase(TestCase):

    def setUp(self):
        self.training_data = get_2x2_training_data()
        self.url = reverse('analysis:training_data', kwargs={'pk': self.training_data.pk})

    def test_get(self):
        request = Request(
            url=self.url,
        )

        content_values = [
            self.training_data.name,
        ]

        dataframe = self.training_data.get_dataframe()

        # add headers
        columns = dataframe.columns
        for column in columns:
            content_values.append(column)
            data_list = dataframe[column].values.tolist()
            content_values += data_list

        true_response = TrueResponse(
            status_code=200,
            context=Context(
                keys=['object'],
                items={
                    'object': self.training_data
                }
            ),
            content_values=content_values
        )

        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)


class TrainingDataListViewTestCase(TestCase):

    def setUp(self):
        self.url = reverse('analysis:training_data_list')
        self.training_data_list = [get_2x2_training_data('first'), get_2x2_training_data('second')]

    def test_get(self):
        request = Request(
            url=self.url
        )
        true_response = TrueResponse(
            status_code=200,
            context=Context(
                keys=['object_list'],
            ),
            content_values=[item.name for item in self.training_data_list]
        )
        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)
        self.assertQuerySetEqual(current_response.context['object_list'], self.training_data_list, ordered=False)


class TrainingDataDeleteView(TestCase):

    def setUp(self):
        self.training_data = get_2x2_training_data()
        self.url = reverse('analysis:delete_training_data', kwargs={'pk': self.training_data.pk})

    def test_get(self):
        request = Request(
            url=self.url,
        )

        content_values = [
            self.training_data.name,
        ]

        true_response = TrueResponse(
            status_code=200,
            context=Context(
                keys=['object'],
                items={
                    'object': self.training_data
                }
            ),
            content_values=content_values
        )

        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)

    def test_post(self):
        request = Request(
            url=self.url,
            method=POST,
        )

        true_response = TrueResponse(
            status_code=302,
            redirect_url=reverse('analysis:training_data_list')
        )

        current_response = request.get_response(self.client)
        self.assertTrueResponse(current_response, true_response)
