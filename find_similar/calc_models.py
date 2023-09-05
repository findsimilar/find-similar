from typing import Optional

from pydantic import BaseModel


class Item(BaseModel):
    id: Optional[int]
    label: str
    part_number: str
    id_shop: int
    id_base_item: Optional[int]
    cos: Optional[float] = 0
    token_set: Optional[set]

    def __eq__(self, other):
        return self.id == other.id_base_item


class TokenizeException(Exception):
    pass


class LanguageNotFound(TokenizeException):
    def __init__(self, language):
        self.language = language
        super().__init__(
            f"Language '{language}' is not supported by nltk module"
        )