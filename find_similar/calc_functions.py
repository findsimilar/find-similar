"""
Calculation functions to find similarity percent
"""
from .tokenize import tokenize, STOP_WORDS


def calc_cosine_similarity_opt(x_set: set, y_set: set) -> float:
    """
    Get cos between two sets of words
    :param x_set: One set
    :param y_set: Another set
    :return: cos similarity
    """
    c = len(y_set & x_set)
    cosine = 0
    if c > 0:
        l1n_sum = len(x_set)
        l2n_sum = len(y_set)
        sum_l1_l2 = (l1n_sum * l2n_sum)
        cosine = c / float(sum_l1_l2 ** 0.5)
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
        :param dictionary: default = None. If you want to replace one words to others you can send the dictionary.
        :param **kwargs: You can set any properties in the result object
        :return: cos similarity
        """
        self.text = text
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.tokens = tokens if tokens else get_tokens(text, dictionary)

    def __eq__(self, other):
        """
        compare two TokenText objects
        :param other: second TokenText objects (self - is the first)
        :return: True or False, depends on object id
        """
        return self.id == other.id_base_item


def get_tokens(text, dictionary=None) -> set:
    """
    Get tokens from str text
    :param text: str text
    :param dictionary: default = None. If you want to replace one words to others you can send the dictionary.
    :return: tokes for text
    """
    tokens = tokenize(text, STOP_WORDS, dictionary)
    return tokens
