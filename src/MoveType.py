from enum import Enum

class MoveType(Enum):

    PUT_UNUSED_PAWN_ON_SQUARE = 0
    PUT_USED_PAWN_ON_SQUARE = 1
    SIMPLE_SLIDE = 2
    DOUBLE_SLIDE = 3