"""
Models for calculation and compare
"""
from typing import Optional
from pydantic import BaseModel  # pylint: disable=no-name-in-module


class Item(BaseModel):
    """
    Item
    """
    id: Optional[int]  # pylint: disable=invalid-name
    label: str
    part_number: str
    id_shop: int
    id_base_item: Optional[int]
    cos: Optional[float] = 0
    token_set: Optional[set]

    def __eq__(self, other):
        return self.id == other.id_base_item


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
