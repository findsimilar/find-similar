"""
Analysis views
"""
import os
from django.views.generic import FormView
from django.urls import reverse
from django.conf import settings
from analysis.functions import (
    analyze_one_item,
    analyze_two_items,
    example_frequency_analysis,
    load_training_data,
)
from .forms import (
    OneTextForm,
    TwoTextForm, LoadTrainingDataForm,
)


class TokenizeOneView(FormView):
    """
    For get tokens from one text
    """
    form_class = OneTextForm
    template_name = 'analysis/tokenize_one.html'

    def form_valid(self, form):
        text = form.cleaned_data['text']
        self.text = text
        self.tokens = analyze_one_item(text)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        data = self.request.GET
        text = data.get('text', '')
        tokens = data.getlist('token')
        context['text'] = text
        context['tokens'] = tokens
        return context

    def get_success_url(self):
        url_params = []
        for token in self.tokens:
            param = f'token={token}'
            url_params.append(param)
        url_params = f'?text={self.text}&{"&".join(url_params)}'
        url = f'{reverse("analysis:tokenize_one")}{url_params}'
        return url


class CompareTwoView(FormView):
    """
    For compare two items
    """
    form_class = TwoTextForm
    template_name = 'analysis/compare_two.html'
    success_url = '/analysis/compare-two/'

    def form_valid(self, form):
        self.one_text = form.cleaned_data['one_text']
        self.two_text = form.cleaned_data['two_text']
        self.cos = analyze_two_items(self.one_text, self.two_text)
        return super().form_valid(form)

    def get_success_url(self):
        url_params = f'?one_text={self.one_text}&two_text={self.two_text}&cos={self.cos}'
        url = f'{reverse("analysis:compare_two")}{url_params}'
        return url

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        data = self.request.GET
        one_text = data.get('one_text', '')
        two_text = data.get('two_text', '')
        cos = data.get('cos', '')
        context['one_text'] = one_text
        context['two_text'] = two_text
        context['cos'] = cos
        return context


class ExampleFrequencyAnalysis(FormView):
    """
    Example Frequency Analysis
    """
    form_class = OneTextForm
    template_name = 'analysis/example_frequency.html'

    def form_valid(self, form):
        self.text = form.cleaned_data['text']
        try:
            self.result = example_frequency_analysis(self.text)
            self.error = None
        except FileNotFoundError:
            self.error = 'example not found'
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        data = self.request.GET.dict()
        text = data.pop('text', '')
        context['text'] = text
        error = data.get('error', None)
        if error:
            context['error'] = error
        else:
            result = []
            for key, value in data.items():
                result.append((key, int(value)))
            context['result'] = tuple(result)
        return context

    def get_success_url(self):
        if self.error:
            url = f'{reverse("analysis:example_frequency")}?text={self.text}&error={self.error}'
        else:
            url_params = []
            for key, value in self.result:
                url_params.append(f'{key}={value}')
            url_params = f'?text={self.text}&{"&".join(url_params)}'
            url = f'{reverse("analysis:example_frequency")}{url_params}'
        return url


class LoadTrainingDataView(FormView):
    form_class = LoadTrainingDataForm
    template_name = 'analysis/load_data.html'

    def handle_uploaded_file(self, f):
        uploaded_path = os.path.join(settings.BASE_DIR, 'uploads', 'loaddata.xlsx')
        with open(uploaded_path, 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)
        return uploaded_path

    def form_valid(self, form):
        data = form.cleaned_data
        excel_file = form.cleaned_data['excel_file']
        uploaded_path = self.handle_uploaded_file(excel_file)
        name = data['name']
        self.training_data = load_training_data(name=name, filepath=uploaded_path)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('analysis:training_data', kwargs={'pk': self.training_data.pk})
