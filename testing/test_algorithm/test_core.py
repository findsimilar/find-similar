from algorithm import find_similar, TokenText


def test_find_similar_with_tokens():
    text = TokenText('иван родил девчёнку', tokens={'иван', 'родить', 'девчёнка'})

    texts = [
        TokenText('иван родил девчёнку', tokens={'иван', 'родить', 'девчёнка'}),
        TokenText('a b c', tokens={'a', 'b', 'c'}),
        TokenText('иван b 0', tokens={'иван', 'b', '0'}),
    ]

    result = find_similar(text, texts, 2)
    assert result[0].text == 'иван родил девчёнку'
    assert result[1].text == 'иван b 0'


def test_find_similar_with_str():
    text = 'иван родил девчёнку'

    texts = [
        TokenText('иван родил девчёнку', tokens={'иван', 'родить', 'девчёнка'}),
        TokenText('a b c', tokens={'a', 'b', 'c'}),
        TokenText('иван b 0', tokens={'иван', 'b', '0'}),
    ]

    result = find_similar(text, texts, 2)
    assert result[0].text == 'иван родил девчёнку'
    assert result[1].text == 'иван b 0'