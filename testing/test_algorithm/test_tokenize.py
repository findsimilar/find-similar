"""
Tests for tokenize
"""
import pytest
from find_similar.calc_models import LanguageNotFoundException
from find_similar.tokenize import (
    spacing,
    replacing,
    split_text_and_digits,
    get_normal_form,
    tokenize,
    remove_part_speech,
    get_parsed_text,
    prepare_dictionary,
    HashebleSet,
    replace_yio,
    add_nltk_stopwords,
)


def test_spacing():
    """
    Test spacing
    """
    chars = ["a", "b"]
    label = "ivonailonbi"
    label = spacing(label, chars)
    assert label == "ivon ilon i"


def test_replacing():
    """
    Test replacing
    """
    chars = ["a", "b"]
    label = "ivonailonbi"
    label = replacing(label, chars)
    assert label == "ivoniloni"


def test_split_text_and_digits():
    """
    Test split_text_and_digits
    """
    input_str = "1some2string5with9"
    result = split_text_and_digits(input_str)
    assert result == ["1", "some", "2", "string", "5", "with", "9"]


def test_get_normal_form():
    """
    Test get_normal_form
    """
    word = "рыбы"
    normal_form = get_normal_form(get_parsed_text(word))
    assert normal_form == "рыба"


def test_tokenize():
    """
    Test tokenize
    """
    text = "Иван,родил/девченку-веле¶л 1тащить2пеленку3"
    result = {"пелёнка", "3", "девчёнка", "2", "1", "иван"}
    # without dictionary
    assert tokenize(text, "russian") == result

    # with dictionary
    dictionary = {"3": "новый конь"}
    result = {"пелёнка", "новый", "конь", "девчёнка", "2", "1", "иван"}
    dictionary = prepare_dictionary(dictionary)
    assert tokenize(text, "russian", dictionary) == result

    text = "My/ very ,,excited mot¶her 1just 3served us 2nine pies"
    result = {"2", "3", "pies", "us", "nine", "excited", "1", "mother", "served"}
    # without dictionary
    assert tokenize(text, "english") == result

    # with dictionary
    dictionary = {"excited": "educated"}
    result = {"2", "3", "pies", "us", "nine", "educated", "1", "mother", "served"}
    dictionary = prepare_dictionary(dictionary)
    assert tokenize(text, "english", dictionary) == result


def test_remove_part_speech():
    """
    Test remove_part_speech
    """
    words = ["рыбы", "велел", "тащить", "пелёнку"]
    non_verb_form = []
    for word in words:
        non_verb_form.append(remove_part_speech(get_parsed_text(word)))
    assert non_verb_form == ["рыба", None, None, "пелёнка"]

    word_ad = ["быстрый", "1", "тащить", "коня"]
    non_ad_form = []
    for word in word_ad:
        non_ad_form.append(remove_part_speech(get_parsed_text(word), {"ADJF"}))
    assert non_ad_form == [None, "1", "тащить", "конь"]


def test_get_parsed_text():
    """
    Test get_parsed_text
    """
    word = "текст"
    parsed_object = get_parsed_text(word)
    assert parsed_object.word == "текст"


class TestHashebleSet:
    """
    Test HashebleSet class
    """
    def test_hash(self):
        """
        Test hash
        """
        hasheble_set = HashebleSet(["one"])
        assert hash(hasheble_set) == hash("HashebleSet({'one'})")


def test_prepare_dictionary():
    """
    Test prepare_dictionary
    """
    dictionary = {"one two": "two three"}
    dictionary = prepare_dictionary(dictionary)
    assert dictionary == {HashebleSet(["one", "two"]): {"two", "three"}}


def test_replace_yio():
    """
    Test replace_yio
    """
    assert "новье" == replace_yio("новьё")


def test_add_nltk_stopwords():
    """
    Test add_nltk_stopwords
    """
    test_dict = {"russian": "будто", "english": "yourself"}
    for k, val in test_dict.items():
        stop_words = add_nltk_stopwords(k)
        is_word_in_set = False
        if val in stop_words:
            is_word_in_set = True
        assert is_word_in_set
    with pytest.raises(LanguageNotFoundException):
        stop_words = add_nltk_stopwords("unknown_language")


def test_remove_or_not_stopwords():
    """
    Test remove_stopwords parameter
    """
    text = "что я знаю о кругах"
    result = {"круг"}
    assert tokenize(text, "russian", remove_stopwords=True) == result
    result = {"что", "я", "о", "круг"}
    assert tokenize(text, "russian", remove_stopwords=False) == result
