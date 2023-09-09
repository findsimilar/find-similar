"""
Settings for laboratory
"""
import sys

sys.path.append("../")
from find_similar.tokenize import prepare_dictionary  # pylint: disable=wrong-import-position

DICTIONARY = None

# BRANDS
BRANDS = {
    "бош": "BOSCH",
}

DICTIONARY = BRANDS

# сокращения
SHORT_WORDS = {
    "вкл": "включение",
}

DICTIONARY.update(SHORT_WORDS)

ERROR_WORDS = {
    "апарат": "аппарат",
}

DICTIONARY.update(ERROR_WORDS)

EQUIPMENT = {"рукоятка": "ручка"}

DICTIONARY.update(EQUIPMENT)

EQUIPMENT = {
    "бак": "топливный бак",
}

DICTIONARY.update(EQUIPMENT)

DICTIONARY = prepare_dictionary(DICTIONARY)

TOP_ELEMENT = 0


def load_from_file(filename):
    """
    Get data from file and set language
    """
    print("Read data from file...")
    with open(filename, "r", encoding="utf-8") as file:
        line = file.read()

    try:
        _, language, *__ = sys.argv
    except ValueError:
        language = "russian"
    return line, language
