"""
Core package views
"""
from django.views.generic import TemplateView


class IndexView(TemplateView):
    """
    Main page view
    """
    template_name = 'core/index.html'
