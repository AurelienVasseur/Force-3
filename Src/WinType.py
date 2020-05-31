from enum import Enum

class WinType(Enum):
    LINE = 0
    COLUMN = 1
    DIAGONAL = 2
    REVERSE_DIAGONAL = 3