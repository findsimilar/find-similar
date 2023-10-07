"""
App config for core app
"""
from django.apps import AppConfig


class CoreConfig(AppConfig):
    """
    Config class for core app
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "core"
