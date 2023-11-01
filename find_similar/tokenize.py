"""
Module with tokenize functions
"""
import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import pymorphy3 as pymorphy

from find_similar.calc_models import LanguageNotFoundException

morph = pymorphy.MorphAnalyzer()

PUNCTUATION_SET = {";", ",", ".", "(", ")", "*", "-", ":"}
UNUSEFUL_WORDS = {
    "шт",
    "уп",
    "x",
    "х",  # одна букава x-английская, вторая х-русская
    "mm",
    "мм",
    "сс",
    "cc",
    "m",
    "м",
    "подха",  # там есть подх.для
    "тип",
    "d",
    "vz",
    # 'мя' # 2-мя, 3-мя, ...
}

STOP_WORDS_NO_LANGUAGE = PUNCTUATION_SET.union(UNUSEFUL_WORDS)


def get_stopwords_from_nltk(language: str):
    """
    Get stopwords for specific language
    :param language: current text language
    """
    try:
        stopwords_with_language = stopwords.words(language)
    except LookupError:
        nltk.download("stopwords")
        nltk.download("punkt")
        stopwords_with_language = stopwords.words(language)
    except OSError as exc:
        raise LanguageNotFoundException(language) from exc
    return stopwords_with_language


def add_nltk_stopwords(language: str, stop_words=None):
    """
    Add stopwords to STOP_WORDS_NO_LANGUAGE
    :param language: current text language
    :param stop_words: existing stop words
    """
    if stop_words is None:
        stop_words = STOP_WORDS_NO_LANGUAGE
    stopwords_with_language = get_stopwords_from_nltk(language)
    stop_words = stop_words.union(stopwords_with_language)
    return stop_words


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
    return text.replace("ё", "е")


def split_text_and_digits(text):
    """
    Split words and digits
    :param text: enter text
    :return: list of separated texts
    """
    regex = r"^\D+[0]\D+$"
    match = re.search(regex, text, re.MULTILINE)
    if match:
        return [text]
    # Проверяем на вольты и амперы
    regex = r"\d+[.]?\d?[в|а|В|А|B|A|a]{1}$"
    match = re.search(regex, text, re.MULTILINE)
    if match:
        text = match.group()
        chars = "вВB"
        for char in chars:
            text = text.replace(char, "v")
        chars = "аАaA"
        for char in chars:
            text = text.replace(char, "ah")
    # Делим цифры и буквы
    regex = r"\D+|\d+"
    texts = []
    matches = re.finditer(regex, text, re.MULTILINE)
    for _, match in enumerate(matches, start=1):
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
    """
    Use dictionary with multiple compliance
    """
    for k, val in dictionary.items():
        if k.issubset(tokens):
            tokens = (tokens - k).union(val)
    return tokens


def remove_part_speech(part_parse, parts=None, dictionary=None):
    """
    Remove variable part of speach from word
    :param dictionary: default = None.
    If you want to replace one words to others you can send the dictionary.
    :param part_parse: pymorph2 object
    :param parts: set of part of speach
    NOUN	noun name
    ADJF	adjective name (full)
    VERB	verb (personal form)
    INFN	verb (infinitive)
    NUMR	numeral
    PREP	preposition
    CONJ	conjunction
    PRCL	particle
    :return: text without variable part of speach or None
    """
    result = get_normal_form(part_parse)
    if dictionary and HashebleSet([result]) in dictionary:
        return result
    if parts is None:
        parts = {"INFN", "VERB"}
    for part in parts:
        if part in part_parse.tag:
            return None
    return result


def get_parsed_text(word: str):
    """
    Get Parsed Text
    :param word: str word
    :return: pymorphy2 object
    """
    return morph.parse(word)[0]


def tokenize(text: str, language: str, dictionary=None, remove_stopwords=True):
    """
    Main function to tokenize text
    :param text: Text to tokenize
    :param language: language for setting stop-words
    :param dictionary: default = None.
    If you want to replace one words to others you can send the dictionary.
    :param remove_stopwords: default = True. Remove stopwords if True
    :return: Tokens
    """
    # replace these characters with spaces
    punc_to_space = [",", "/", "-", "=", "."]
    text = spacing(text, punc_to_space)
    # delete these characters (replace with an empty string)
    punc_to_delete = ["Ø", "¶", "”"]
    text = replacing(text, punc_to_delete)
    text = replace_yio(text)
    tmp_set = set()
    # now we go by individual words
    stop_words = add_nltk_stopwords(language)
    for word in word_tokenize(text, language=language):
        # divide into parts if there are numbers in the word
        parts = split_text_and_digits(word)
        # then we go in parts
        for part in parts:
            # check if the verb - remove it
            # in the opposite case, we bring it to the normal form
            part_parse = get_parsed_text(part)
            # we remove the verbs and bring them to the normal form
            word_normal_form = remove_part_speech(part_parse, dictionary=dictionary)
            if word_normal_form:
                # remove stop words
                if remove_stopwords:
                    if word_normal_form not in stop_words:
                        tmp_set.add(word_normal_form)
                else:
                    tmp_set.add(word_normal_form)
    if dictionary:
        # use dictionary
        tmp_set = use_dictionary_multiple(tmp_set, dictionary)
    return tmp_set


def prepare_dictionary(dictionary):
    """
    Get special object from simple python dict
    :param dictionary: default = None.
    If you want to replace one words to others you can send the dictionary.
    :return: dictionary of HashebleSet with data
    """
    result = {}
    for k, val in dictionary.items():
        # взять нормальные формы
        keys = k.split()
        keys = [get_normal_form(get_parsed_text(key)) for key in keys]
        new_k = HashebleSet(keys)

        values = val.split()
        values = [get_normal_form(get_parsed_text(value)) for value in values]

        new_v = set(values)
        result[new_k] = new_v
    return result
