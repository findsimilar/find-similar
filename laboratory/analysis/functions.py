"""
Analysis functions
"""
from django.conf import settings


def analyze_one_item(item, dictionary=None, language="russian", printer=print):
    """
    Analyze one item for tokenize
    """
    printer(f'Get tokens for {item}...')
    tokens = settings.TOKENIZE(item, language=language, dictionary=dictionary)
    printer('Done:')
    printer(tokens)
    printer('End')
    return tokens
