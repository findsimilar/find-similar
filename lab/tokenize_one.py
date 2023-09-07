"""
Читает текст из файла и создает токены
"""
import sys

from settings import DICTIONARY

sys.path.append('../')

from analytics.functions import analyze_one_item

filename = 'tokenize_one.txt'

print('Read data from file...')
with open(filename, 'r', encoding='utf-8') as f:
    line = f.read()

try:
    _, language, *others = sys.argv
except:
    language = 'russian'

one = line.strip()
print(f'{one} has been loaded')
one_tokens = analyze_one_item(one, DICTIONARY, language=language)
print('TOKENS:', one_tokens)