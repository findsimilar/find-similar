"""
Models for calculation and compare
"""


class TokenizeException(Exception):
    """
    Base Exception class for Tokenize exceptions
    """


class LanguageNotFoundException(TokenizeException):
    """
    Language not found error
    """

    def __init__(self, language):
        self.language = language
        super().__init__(f"Language '{language}' is not supported by nltk module")
