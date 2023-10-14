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


class TwoTextForm(forms.Form):
    """
    Form with two texts
    """
    one_text = forms.CharField(max_length=128, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    two_text = forms.CharField(max_length=128, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
