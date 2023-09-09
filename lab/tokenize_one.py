"""
Читает текст из файла и создает токены
Read text from file and create tokens
"""
import sys

from settings import DICTIONARY, load_from_file  # pylint: disable=import-error

sys.path.append("../")

from analytics.functions import analyze_one_item  # pylint: disable=wrong-import-position

FILENAME = "tokenize_one.txt"

line, language = load_from_file(FILENAME)

one = line.strip()
print(f"{one} has been loaded")
one_tokens = analyze_one_item(one, DICTIONARY, language=language)
print("TOKENS:", one_tokens)
