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


def analyze_two_items(one, two, printer=print):
    """
    Calc cos between two items
    """
    printer(f'Get cos between "{one}" and "{two}"')
    one_tokens = analyze_one_item(one, printer=printer)
    two_tokens = analyze_one_item(two, printer=printer)
    cos = settings.CALC_COSINE_SIMILARITY_OPT(one_tokens, two_tokens)
    printer('Done')
    printer(f'cos = {float(cos)}')
    printer('End')
    return cos
