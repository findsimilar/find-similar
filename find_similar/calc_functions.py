from .tokenize import tokenize, STOP_WORDS


def calc_cosine_similarity_opt(x_set: set, y_set: set) -> float:
    c = len(y_set & x_set)
    cosine = 0
    if c > 0:
        l1n_sum = len(x_set)
        l2n_sum = len(y_set)
        sum_l1_l2 = (l1n_sum * l2n_sum)
        cosine = c / float(sum_l1_l2 ** 0.5)
    return cosine


class TokenText:
    def __init__(self, text, tokens=None, dictionary=None, **kwargs):
        self.text = text
        for k, v in kwargs.items():
            setattr(self, k, v)
        self.tokens = tokens if tokens else get_tokens(text, dictionary)

    def __eq__(self, other):
        return self.id == other.id_base_item


def get_tokens(text, dictionary=None) -> set:
    tokens = tokenize(text, STOP_WORDS, dictionary)
    return tokens
