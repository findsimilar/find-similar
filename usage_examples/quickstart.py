"""
Quickstart module
"""
from find_similar import find_similar


def main():
    """
    Simple usage
    """
    texts = ['one two', 'two three', 'three four']  # texts to check

    text_to_compare = 'one four'  # the main text
    result = find_similar(text_to_compare, texts, count=10)  # using find_similar
    return result  # [TokenText(text="one two", len(tokens)=2, cos=0.5),
                    # TokenText(text="three four", len(tokens)=2, cos=0.5),
                    # TokenText(text="two three", len(tokens)=2, cos=0)]
