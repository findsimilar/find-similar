"""
Analysis views
"""
from django.views.generic import FormView
from django.urls import reverse
from analysis.functions import analyze_one_item
from .forms import OneTextForm


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
