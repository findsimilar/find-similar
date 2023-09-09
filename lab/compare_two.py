"""
Читает 2 элемента из файла, разделенные /// тремя слешами
Read 2 elements from file splitted by ///
"""
import sys
from settings import DICTIONARY, load_from_file  # pylint: disable=import-error

sys.path.append("../")

from analytics.functions import analyze_one_item  # pylint: disable=wrong-import-position
from find_similar import calc_cosine_similarity_opt  # pylint: disable=wrong-import-position

SEPARATOR = "///"
FILENAME = "compare_two.txt"

line, language = load_from_file(FILENAME)

one, two = line.split(SEPARATOR)
print(f"{one} COMPARE WITH {two}")
one_tokens = analyze_one_item(one, DICTIONARY, language=language)
two_tokens = analyze_one_item(two, DICTIONARY, language=language)
cos = calc_cosine_similarity_opt(one_tokens, two_tokens)
print("COS:", cos)
