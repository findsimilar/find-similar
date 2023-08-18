import sys
sys.path.append('../')
from algorithm.tokenize import prepare_dictionary

DICTIONARY = None

# BRANDS
BRANDS = {
    'бош':	'BOSCH',
}

DICTIONARY = BRANDS

# сокращения
SHORT_WORDS = {
    'вкл': 'включение',
}

DICTIONARY.update(SHORT_WORDS)

ERROR_WORDS = {
    'апарат': 'аппарат',
}

DICTIONARY.update(ERROR_WORDS)

EQUIPMENT = {
    'рукоятка': 'ручка'
}

DICTIONARY.update(EQUIPMENT)

EQUIPMENT = {
    'бак':	'топливный бак',
}

DICTIONARY.update(EQUIPMENT)

DICTIONARY = prepare_dictionary(DICTIONARY)

TOP_ELEMENT = 0