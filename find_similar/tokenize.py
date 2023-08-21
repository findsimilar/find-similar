"""
Module with tokenize functions
"""
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pymorphy2

morph = pymorphy2.MorphAnalyzer()

PUNCTUATION_SET = {";", ",", ".", "(", ")", "*", "-", ':'}

UNUSEFUL_WORDS = {
    'шт', 'уп',
    'x', 'х',  # одна букава x-английская, вторая х-русская
    'mm', 'мм', 'сс', 'cc', 'm', 'м',
    'подха',  # там есть подх.для
    'тип',
    'd',
    'vz',
    # 'мя' # 2-мя, 3-мя, ...
}
try:
    stopwords_with_language = stopwords.words('russian')
except LookupError:
    nltk.download('stopwords')
    nltk.download('punkt')
    stopwords_with_language = stopwords.words('russian')
STOP_WORDS = set(stopwords_with_language).union(PUNCTUATION_SET)
STOP_WORDS = STOP_WORDS.union(UNUSEFUL_WORDS)


def spacing(text: str, chars: list):
    """
    replace chars to space
    :param text: Text to spacing
    :param chars: Chars to replace
    :return: new text without chars with spaces
    """
    for char in chars:
        text = text.replace(char, " ")
    return text


def replacing(text: str, chars: list):
    """
    replace chars to empty string
    :param text: Text to replace
    :param chars: Chars to replace
    :return: new text without chars
    """
    for char in chars:
        text = text.replace(char, "")
    return text


def replace_yio(text):
    """
    Change russian ё to e
    :param text: Text to change
    :return: new text without ё with е
    """
    return text.replace('ё', 'е')


def split_text_and_digits(s):
    """
    Split words and digits
    :param s: enter text
    :return: list of separated texts
    """
    regex = r"^\D+[0]\D+$"
    match = re.search(regex, s, re.MULTILINE)
    if match:
        return [s]
    # Проверяем на вольты и амперы
    regex = r"\d+[.]?\d?[в|а|В|А|B|A|a]{1}$"
    match = re.search(regex, s, re.MULTILINE)
    if match:
        s = match.group()
        chars = "вВB"
        for c in chars:
            s = s.replace(c, 'v')
        chars = "аАaA"
        for c in chars:
            s = s.replace(c, 'ah')
    # Делим цифры и буквы
    regex = r"\D+|\d+"
    texts = []
    matches = re.finditer(regex, s, re.MULTILINE)
    for matchNum, match in enumerate(matches, start=1):
        texts.append(match.group())
    return texts


def get_normal_form(part_parse):
    """
    Get Normal Form
    :param part_parse: special object
    :return: object normal form
    """
    return part_parse.normal_form


class HashebleSet(set):
    """
    Special class set with hash to compare and sort two sets
    """
    def __hash__(self):
        return hash(str(self))


def use_dictionary_multiple(tokens, dictionary):
    for k, v in dictionary.items():
        if k.issubset(tokens):
            tokens = (tokens - k).union(v)
    return tokens


def remove_part_speech(part_parse, parts=None, dictionary=None):
    """
    Remove variable part of speach from word
    :param dictionary: default = None. If you want to replace one words to others you can send the dictionary.
    :param part_parse: pymorph2 object
    :param parts: set of part of speach
        NOUN	имя существительное
        ADJF	имя прилагательное (полное)
        VERB	глагол (личная форма)
        INFN	глагол (инфинитив)
        NUMR	числительное
        PREP	предлог
        CONJ	союз
        PRCL	частица
    :return: text without variable part of speach or None
    """
    result = get_normal_form(part_parse)
    if dictionary and HashebleSet([result]) in dictionary:
        return result
    if parts is None:
        parts = {'INFN', 'VERB'}
    for part in parts:
        if part in part_parse.tag:
            return None
    return result


def get_parsed_text(word: str) -> pymorphy2:
    """
    Get Parsed Text
    :param word: str word
    :return: pymorphy2 object
    """
    return morph.parse(word)[0]


def tokenize(text: str, stop_words: set, dictionary=None):
    """
    Main function to tokenize text
    :param text: Text to tokenize
    :param stop_words: Stop words in Language to ignore
    :param dictionary: default = None. If you want to replace one words to others you can send the dictionary.
    :return: Tokens
    """
    # заменяем эти символы на пробелы
    punc_to_space = [',', '/', '-', '=', '.']
    text = spacing(text, punc_to_space)
    # удаляем эти символы (заменяем на пустую строку)
    punc_to_delete = ['Ø', '¶', '”']
    text = replacing(text, punc_to_delete)
    text = replace_yio(text)
    # итоговый set
    # result_set = set()
    tmp_set = set()
    # теперь идем по отдельным словам
    for word in word_tokenize(text):
        # делим на части если в слове есть цифры
        parts = split_text_and_digits(word)
        # дальше идем по частям
        for part in parts:
            # проверяем если глагол - убираем его
            # в обратном случае приводим к нормальной форме
            part_parse = get_parsed_text(part)
            # удаляем глаголы и приводим к нормальной форме
            word_normal_form = remove_part_speech(part_parse, dictionary=dictionary)
            if word_normal_form:
                # убираем стоп слова
                if word_normal_form not in stop_words:
                    tmp_set.add(word_normal_form)
    if dictionary:
        # используем справочник
        tmp_set = use_dictionary_multiple(tmp_set, dictionary)
    return tmp_set


def prepare_dictionary(dictionary):
    """
    Get special object from simple python dict
    :param dictionary: default = None. If you want to replace one words to others you can send the dictionary.
    :return: dictionary of HashebleSet with data
    """
    result = {}
    for k, v in dictionary.items():
        # взять нормальные формы
        keys = k.split()
        keys = [get_normal_form(get_parsed_text(key)) for key in keys]
        new_k = HashebleSet(keys)

        # v = get_normal_form(get_parsed_text(v))
        values = v.split()
        values = [get_normal_form(get_parsed_text(value)) for value in values]

        new_v = set(values)
        result[new_k] = new_v
    return result
