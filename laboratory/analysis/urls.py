"""
Analysis app urls
"""
from django.urls import path
from . import views

app_name = 'analysis'

urlpatterns = [
    path('tokenize-one/', views.TokenizeOneView.as_view(), name="tokenize_one"),
    path('compare-two/', views.CompareTwoView.as_view(), name="compare_two"),
    path('example-frequency/', views.ExampleFrequencyAnalysis.as_view(), name="example_frequency"),
    path('load-training-data/', views.LoadTrainingDataView.as_view(), name="load_training_data"),
    path('training-data/<int:pk>/', views.LoadTrainingDataView.as_view(), name="training_data"),
]
