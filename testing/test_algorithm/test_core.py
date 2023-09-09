"""
Test core
"""
from find_similar import find_similar, TokenText


def test_find_similar_with_tokens():
    """
    Test find_similar send tokens directly
    """
    text = TokenText("иван родил девчёнку", tokens={"иван", "родить", "девчёнка"})

    texts = [
        TokenText("иван родил девчёнку", tokens={"иван", "родить", "девчёнка"}),
        TokenText("a b c", tokens={"a", "b", "c"}),
        TokenText("иван b 0", tokens={"иван", "b", "0"}),
    ]

    result = find_similar(text, texts)
    assert result[0].text == "иван родил девчёнку"
    assert result[1].text == "иван b 0"


def test_find_similar_with_str():
    """
    Test find_similar send str only
    """
    text = "иван родил девчёнку"

    texts = [
        TokenText("иван родил девчёнку", tokens={"иван", "родить", "девчёнка"}),
        TokenText("a b c", tokens={"a", "b", "c"}),
        TokenText("иван b 0", tokens={"иван", "b", "0"}),
    ]

    result = find_similar(text, texts)
    assert result[0].text == "иван родил девчёнку"
    assert result[1].text == "иван b 0"


def test_find_similar_with_str_list():
    """
    Test find_similar send str_list
    """
    text = "иван родил девчёнку"

    texts = [
        "иван родил девчёнку",
        "a b c",
        "иван b 0",
    ]

    result = find_similar(text, texts)
    assert result[0].text == "иван родил девчёнку"
    assert result[1].text == "иван b 0"
