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
    for char in chars:
        text = text.replace(char, " ")
    return text


def replacing(text: str, chars: list):
    for char in chars:
        text = text.replace(char, "")
    return text


def replace_yio(text):
    return text.replace('ё', 'е')


def split_text_and_digits(s):
    # Проверяем на строки с ед. цифрой внутри
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
        # делим все цифры
        # part = match.group()
        # if part.isdigit():
        #     digits = list(part)
        #     for digit in digits:
        #         texts.append(digit)
        # else:
        #     # end
        texts.append(match.group())
    return texts


def get_normal_form(part_parse):
    return part_parse.normal_form


class HashebleSet(set):
    def __hash__(self):
        return hash(str(self))


def use_dictionary_multiple(tokens, dictionary):
    for k, v in dictionary.items():
        if k.issubset(tokens):
            tokens = (tokens - k).union(v)
    return tokens


def remove_part_speech(part_parse, parts=None, dictionary=None):
    """
    Исключить произвольную часть речи из слова
    :param dictionary:
    :param part_parse: объект pymorph2
    :param parts: части речи, передавать как множество {}
        NOUN	имя существительное
        ADJF	имя прилагательное (полное)
        VERB	глагол (личная форма)
        INFN	глагол (инфинитив)
        NUMR	числительное
        PREP	предлог
        CONJ	союз
        PRCL	частица
    :return:
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
    return morph.parse(word)[0]


def tokenize(text: str, stop_words: set, dictionary=None):
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
