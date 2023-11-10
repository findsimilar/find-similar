"""
Test calc_functions
"""
import math

import pytest
from find_similar import calc_cosine_similarity_opt, TokenText
from find_similar.calc_functions import calc_keywords_rating, sort_search_list
from find_similar.tokenize import prepare_dictionary


@pytest.mark.parametrize(
    "x_set,y_set,result",
    [
        ({"иван", "родить", "девченка"}, {"иван", "родить", "девченка"}, 1),
        ({"и", "р", "д"}, {"иван", "родить", "девченка"}, 0),
        ({"иван", "родить"}, {"родить", "девченка"}, 0.5),
    ],
)
def test_calc_cosine_similarity_opt(x_set, y_set, result):
    """
    Test cals_cosine_similarity_opt
    """
    assert calc_cosine_similarity_opt(x_set, y_set) == result


def test_calc_keywords_rating():
    """
    calc_keywords_rating
    """
    text = TokenText(text="venus venus venus mercury earth mars jupiter")
    keywords = {'venus': 0.25, 'mars': 0.33, 'sun': 0.45}
    keywords_number = calc_keywords_rating(text, keywords)
    assert math.isclose(keywords_number, 0.58)


def test_sort_search_list():
    """
    sort_search_list
    """
    night_text = 'ночь'
    street_text = 'улица'
    lamp_text = 'фонарь'

    night = TokenText(night_text)
    street = TokenText(street_text)
    lamp = TokenText(lamp_text)

    token_texts = [night, street, lamp]

    night.cos = 0.9
    street.cos = 0.8
    lamp.cos = 1

    night.key = 1
    street.key = 0
    lamp.key = 0

    sort_with_keyword = sort_search_list(token_texts, {"аптека": 1})
    sort_without_keyword = sort_search_list(token_texts)

    assert [text.text for text in sort_with_keyword] == [night_text, lamp_text, street_text]
    assert [text.text for text in sort_without_keyword] == [lamp_text, night_text, street_text]

    night.cos = 1
    street.cos = 0.8
    lamp.cos = 0.9

    night.key = 0
    street.key = 1
    lamp.key = 0

    sort_with_keyword = sort_search_list(token_texts, {"аптека": 1})
    sort_without_keyword = sort_search_list(token_texts)

    # by key first
    assert [text.text for text in sort_with_keyword] == [street_text, night_text, lamp_text]
    assert [text.text for text in sort_without_keyword] == [night_text, lamp_text, street_text]


class TestTokenText:
    """
    Test TokenText class
    """
    def test_init_create_tokens(self):
        """
        Test create tokens in init
        """
        text = TokenText("иван родил девчёнку")
        assert text.text == "иван родил девчёнку"
        assert text.tokens == {"иван", "девчёнка"}

    def test_init_set_tokens(self):
        """
        Test set tokens in init
        """
        text = TokenText("иван родил девчёнку", tokens={"a", "b", "c"})
        assert text.tokens == {"a", "b", "c"}

    def test_init_set_dict(self):
        """
        Test set dict in init
        """
        dictionary = {"иван": "рабан"}
        dictionary = prepare_dictionary(dictionary)
        text = TokenText("иван родил девчёнку", dictionary=dictionary)
        assert text.tokens == {"рабан", "девчёнка"}

    def test_set_extended_kwargs(self):
        """
        Test send extended kwargs to init
        """
        extended_kwarg = "extended kwarg"
        text = TokenText("some text", extended=extended_kwarg)
        assert text.extended == extended_kwarg

    def test_equal(self):
        """
        Test eq magic method
        """
        one_text = TokenText("one text", id=1)
        two_text = TokenText("one text", id_base_item=1)
        assert one_text == two_text

    def test_repr(self):
        """
        Test repr magic method
        """
        text = TokenText(text="one two")
        assert repr(text) == 'TokenText(text="one two", len(tokens)=2)'

        text.cos = 0.9
        assert repr(text) == 'TokenText(text="one two", len(tokens)=2, cos=0.9)'

    def test_str(self):
        """
        Test str magic method
        """
        text = TokenText(text="one two")
        assert str(text) == repr(text)
