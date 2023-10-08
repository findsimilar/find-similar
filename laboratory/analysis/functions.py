"""
Analysis functions
"""
from django.conf import settings


class Printer:
    """
    This class decorator save results to some place (default print its)
    """

    def __init__(self, title=None, printer=print):
        """
        Init
        :title: callback with title -> title()
        :printer: print function (default print)
        """
        self.title = title
        self.printer = printer

    def __call__(self, func):
        """
        Make decorator
        :func: decorated function
        """
        def inner(*args, **kwargs):
            """
            New function
            """
            printer = kwargs.get('printer', self.printer)

            if 'printer' in kwargs:
                is_delete_printer = True
                if 'is_pass_printer' in kwargs:
                    if kwargs['is_pass_printer']:
                        is_delete_printer = False
                    del kwargs['is_pass_printer']

                if is_delete_printer:
                    del kwargs['printer']

            printer('Start')
            if self.title is not None:
                printer(self.title(*args, **kwargs))
            result = func(*args, **kwargs)
            printer('Done:')
            printer(result)
            printer('End')
            return result

        return inner


@Printer(title=lambda item, **kwargs: f'Get tokens for {item}...')
def analyze_one_item(item, dictionary=None, language="russian"):
    """
    Analyze one item for tokenize
    """
    tokens = settings.TOKENIZE(item, language=language, dictionary=dictionary)
    return tokens


@Printer(title=lambda one, two, **kwargs: f'Get cos between "{one}" and "{two}"')
def analyze_two_items(one, two, printer=print):
    """
    Calc cos between two items
    """
    one_tokens = analyze_one_item(one, printer=printer)  # pylint: disable=unexpected-keyword-arg
    two_tokens = analyze_one_item(two, printer=printer)  # pylint: disable=unexpected-keyword-arg
    cos = settings.CALC_COSINE_SIMILARITY_OPT(one_tokens, two_tokens)
    return cos


@Printer(title=lambda example, **kwargs: f'Analyze "{example}"...')
def example_frequency_analysis(example):
    """
    Example Frequency analysis
    :example: Example name
    """
    result = settings.FREQUENCY_ANALYSIS(example)
    return result
