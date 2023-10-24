
from dataclasses import dataclass
from enum import IntEnum


class TokenType(IntEnum):
    Eof = -1
    Unknown = 0
    Integer = 1
    Identifier = 2
    Add = 3
    Subtract = 4
    Multiply = 5
    Divide = 6
    OpenParenthesis = 7
    CloseParenthesis = 8
    Assign = 9
    Input = 10
    Output = 11

@dataclass
class Token:
    token_type: TokenType
    content: str = ""