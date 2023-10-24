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


class LoadTrainingDataForm(forms.Form):
    name = forms.CharField(max_length=128, widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    excel_file = forms.FileField(max_length=128, widget=forms.FileInput(attrs={
        'class': 'form-control'
    }))
    sheet_name = forms.IntegerField(required=False, initial=0, widget=forms.NumberInput(attrs={
        'class': 'form-control'
    }))
