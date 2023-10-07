"""
Analysis views
"""
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import OneTextForm


class TokenizeOneView(FormView):
    """
    For get tokens from one text
    """
    form_class = OneTextForm
    template_name = 'analysis/tokenize_one.html'
    success_url = reverse_lazy('analysis:tokenize_one')
