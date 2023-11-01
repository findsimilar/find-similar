"""
Quickstart module
"""
from find_similar import find_similar


def main():
    """
    Simple usage
    """
    texts = ['one two', 'two three', 'three four']

    text_to_compare = 'one four'
    result = find_similar(text_to_compare, texts, count=10)
    for item in result:
        print(item.text)
        print(item.cos)
