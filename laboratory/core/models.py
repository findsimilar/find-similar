"""
Models
"""
from django.conf import settings


def check_find_similar():
    """
    To check find_similar import first
    """
    settings.FIND_SIMILAR('none', ['one', 'two'])
    return True
