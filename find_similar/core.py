"""
Core module with search functions
"""

from .calc_functions import (
    TokenText,
    calc_cosine_similarity_opt,
    calc_keywords_rating,
    sort_search_list,
)
from .tokenize import tokenize


# TODO: pylint said too many arguments here. And it's true. We should think about this problem
def find_similar(  # pylint: disable=too-many-arguments
    text_to_check,
    texts,
    language="russian",
    count=5,
    dictionary=None,
    remove_stopwords=True,
    keywords=None,
) -> list[TokenText]:
    """
    The main function to search similar texts.

    :param text_to_check: Text to find similars
    :param texts: List of str or TokenText. In these texts we will search similars
    :param language: Language, default='russian'
    :param count: Results count
    :param dictionary: default = None. If you want to replace one words to others
    :param keywords: default = None.
    :param remove_stopwords: default = True. Remove or not stopwords
    :return: Result list sorted by similarity percent (cos)
    """
    if isinstance(text_to_check, TokenText):
        text_to_check_tokens = text_to_check.tokens
    else:
        text_to_check_tokens = tokenize(
            text_to_check, language, dictionary, remove_stopwords
        )

    token_texts = []
    for text in texts:
        if not isinstance(text, TokenText):
            text = TokenText(text,
                             dictionary=dictionary,
                             language=language,
                             remove_stopwords=remove_stopwords)
        cos = calc_cosine_similarity_opt(text.tokens, text_to_check_tokens)
        text.cos = cos
        if keywords:
            keywords_rating = calc_keywords_rating(text, keywords)
            text.key = keywords_rating
        token_texts.append(text)
    text_rated_sorted = sort_search_list(token_texts, keywords=keywords)
    return text_rated_sorted[:count]
