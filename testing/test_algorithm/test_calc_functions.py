import pytest
from algorithm import calc_cosine_similarity_opt, TokenText
from algorithm.tokenize import prepare_dictionary


@pytest.mark.parametrize(
    "x_set,y_set,result",
    [
        ({'иван', 'родить', 'девченка'}, {'иван', 'родить', 'девченка'}, 1),
        ({'и', 'р', 'д'}, {'иван', 'родить', 'девченка'}, 0),
        ({'иван', 'родить'}, {'родить', 'девченка'}, 0.5),
    ]
)
def test_calc_cosine_similarity_opt(x_set, y_set, result):
    assert calc_cosine_similarity_opt(x_set, y_set) == result


class TestTokenText:

    def test_init_create_tokens(self):
        text = TokenText('иван родил девчёнку')
        assert text.text == 'иван родил девчёнку'
        assert text.tokens == {'иван', 'девчёнка'}

    def test_init_set_tokens(self):
        text = TokenText('иван родил девчёнку', tokens={'a', 'b', 'c'})
        assert text.tokens == {'a', 'b', 'c'}

    def test_init_set_dict(self):
        dictionary = {
            'иван': 'рабан'
        }
        dictionary = prepare_dictionary(dictionary)
        text = TokenText('иван родил девчёнку', dictionary=dictionary)
        assert text.tokens == {'рабан', 'девчёнка'}
