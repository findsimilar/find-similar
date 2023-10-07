"""
Analysis app urls
"""
from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('tokenize-one/', views.TokenizeOneView.as_view(), name="tokenize_one"),
]
