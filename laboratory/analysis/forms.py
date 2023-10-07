"""
Forms
"""
from django import forms


class OneTextForm(forms.Form):
    """
    Form with one text
    """
    text = forms.CharField(max_length=128, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
