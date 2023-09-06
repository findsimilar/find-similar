"""
Core module with search functions
"""

from .calc_functions import TokenText, calc_cosine_similarity_opt
from .tokenize import tokenize, add_nltk_stopwords


def find_similar(
        text_to_check,
        texts,
        language='russian',
        count=5,
        dictionary=None) -> list[TokenText]:
    """
    The main function to search similar texts.
    :param text_to_check: Text to find similars
    :param texts: List of str or TokenText. In these texts we will search similars
    :param language: Language, default='russian'
    :param count: Count results
    :param dictionary: default = None. If you want to replace one words to others you can send the dictionary.
    :return: Result list sorted by similarity percent
    """
    if isinstance(text_to_check, TokenText):
        text_to_check_tokens = text_to_check.tokens
    else:
        text_to_check_tokens = tokenize(text_to_check, language, dictionary)

    token_texts = []
    for text in texts:
        if not isinstance(text, TokenText):
            text = TokenText(text)
        cos = calc_cosine_similarity_opt(text.tokens, text_to_check_tokens)
        text.cos = cos
        token_texts.append(text)
    text_rated_sorted = sorted(token_texts, key=lambda item: item.cos, reverse=True)
    return text_rated_sorted[:count]