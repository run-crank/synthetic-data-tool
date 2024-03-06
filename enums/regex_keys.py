import enum


class RegexKeys(enum.Enum):
    """
    Enum for regex keys
    """
    NAME = r"{{any.name}}"
    WORD = r"{{any.word}}"
    EMAIL = r"{{any.email}}"
    PHONE = r"{{any.phone}}"
    ADDRESS = r"{{any.address}}"

