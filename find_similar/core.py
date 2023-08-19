from .calc_functions import TokenText, calc_cosine_similarity_opt
from .tokenize import STOP_WORDS, tokenize


def find_similar(
        text_to_check,
        texts,
        language='russian',
        count=5,
        dictionary=None) -> list[TokenText]:
    """
    Возвращает отсортированный по вероятности совпадения ограниченный список базовых текстов
    :param dictionary:
    :param text_to_check: искомая строка
    :param texts:
    :param language: используемый язык
    :param count: ограничение в результирующей выборке
    :return:
    """
    if isinstance(text_to_check, TokenText):
        text_to_check_tokens = text_to_check.tokens
    else:
        text_to_check_tokens = tokenize(text_to_check, STOP_WORDS, dictionary)

    token_texts = []
    for text in texts:
        if not isinstance(text, TokenText):
            text = TokenText(text)
        cos = calc_cosine_similarity_opt(text.tokens, text_to_check_tokens)
        text.cos = cos
        token_texts.append(text)
    text_rated_sorted = sorted(token_texts, key=lambda item: item.cos, reverse=True)
    return text_rated_sorted[:count]