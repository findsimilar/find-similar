"""
Calculation functions to find similarity percent
"""
from .tokenize import tokenize


def calc_cosine_similarity_opt(x_set: set, y_set: set) -> float:
    """
    Get cos between two sets of words
    :param x_set: One set
    :param y_set: Another set
    :return: cos similarity
    """
    intersection_length = len(y_set & x_set)
    cosine = 0
    if intersection_length > 0:
        l1n_sum = len(x_set)
        l2n_sum = len(y_set)
        sum_l1_l2 = l1n_sum * l2n_sum
        cosine = intersection_length / float(sum_l1_l2**0.5)
    return cosine


class TokenText:
    """
    The main type to work with text tokens
    """

    def __init__(self, text, tokens=None, dictionary=None, **kwargs):
        """
        init method
        :param text: simple text
        :param tokens: You can set already created tokens. Default = None
        :param dictionary: default = None.
        If you want to replace one words to others you can send the dictionary.
        :param **kwargs: You can set any properties in the result object
        :return: cos similarity
        """
        self.text = text
        for k, val in kwargs.items():
            setattr(self, k, val)
        self.tokens = tokens if tokens else get_tokens(text, dictionary=dictionary)

    def __eq__(self, other):
        """
        compare two TokenText objects
        :param other: second TokenText objects (self - is the first)
        :return: True or False, depends on object id
        """
        return self.id == other.id_base_item

    def __str__(self):
        return repr(self)

    def __repr__(self):
        return f'TokenText(text="{self.text}", tokens={self.tokens})'


def get_tokens(text, dictionary=None, language="russian") -> set:
    """
    Get tokens from str text
    :param text: str text
    :param dictionary: default = None.
    If you want to replace one words to others you can send the dictionary
    :param language
    :return: tokes for text
    """
    tokens = tokenize(text, language, dictionary)
    return tokens
