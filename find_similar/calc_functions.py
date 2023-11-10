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

    def __init__(self,  # pylint: disable=too-many-arguments
                 text,
                 tokens=None,
                 dictionary=None,
                 language='russian',
                 remove_stopwords=True,
                 **kwargs):
        """
        init method
        :param text: simple text
        :param tokens: You can set already created tokens. Default = None
        :param dictionary: default = None.
        If you want to replace one words to others you can send the dictionary.
        :param remove_stopwords: default = True.
        :param language: default = russian.
        :param **kwargs: You can set any properties in the result object
        :return: cos similarity
        """
        self.text = text
        self.key = 0
        for k, val in kwargs.items():
            setattr(self, k, val)
        self.tokens = tokens if tokens else get_tokens(text,
                                                       dictionary=dictionary,
                                                       language=language,
                                                       remove_stopwords=remove_stopwords)

    def __eq__(self, other):
        """
        compare two TokenText objects
        :param other: second TokenText objects (self - is the first)
        :return: True or False, depends on object id
        """
        return self.text == other.text

    def __str__(self):
        return repr(self)

    def __repr__(self):
        cos_str = f', cos={self.cos}' if hasattr(self, 'cos') else ''
        return f'TokenText(text="{self.text}", len(tokens)={len(self.tokens)}{cos_str})'


def get_tokens(text, dictionary=None, language="russian", remove_stopwords=True) -> set:
    """
    Get tokens from str text
    :param text: str text
    :param dictionary: default = None.
    If you want to replace one words to others you can send the dictionary
    :param language
    :param remove_stopwords
    :return: tokes for text
    """
    tokens = tokenize(text, language, dictionary, remove_stopwords)
    return tokens


def calc_keywords_rating(text, keywords):
    """
    Calc keywords rating
    :param keywords: Keywords
    """
    rating = 0
    for token in text.tokens:
        for k, v in keywords.items():
            if str(k) == str(token):
                rating = rating + v
    return rating


def sort_search_list(token_texts, keywords=None):
    """
    Sort search list
    :param token_texts: Texts with tokens
    :param keywords: Keywords, default None
    """
    text_sorted_by_cos = sorted(
        token_texts,
        key=lambda item: item.cos,
        reverse=True
    )
    if keywords:
        text_sorted_by_cos = sorted(
            token_texts,
            key=lambda item: (item.key, item.cos),
            reverse=True
        )
    return text_sorted_by_cos
