"""
User-friendly library to find similar objects.
Main package.

Install:

pip install find-similar

Usage:

from find_similar import find_similar

texts = ['one two', 'two three', 'three four'] \n
result = find_similar('one four', texts, count=10)

"""
from .core import find_similar
from .calc_functions import calc_cosine_similarity_opt, get_tokens, TokenText
from .calc_models import Item
