"""
Читает 2 элемента из файла, разделенные /// тремя слешами
"""
import sys

from settings import DICTIONARY

sys.path.append('../')

from analytics.functions import analyze_one_item
from find_similar import calc_cosine_similarity_opt
SEPARATOR = '///'
filename = 'compare_two.txt'

print('Read data from file...')
with open(filename, 'r', encoding='utf-8') as f:
    line = f.read()

try:
    _, language, *others = sys.argv
except:
    language = 'russian'

one, two = line.split(SEPARATOR)
print(f'{one} COMPARE WITH {two}')
one_tokens = analyze_one_item(one, DICTIONARY, language=language)
two_tokens = analyze_one_item(two, DICTIONARY, language=language)
cos = calc_cosine_similarity_opt(one_tokens, two_tokens)
print('COS:', cos)

