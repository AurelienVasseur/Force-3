from .Position import Position
from .MoveType import MoveType
from .Direction import Direction

class Move:
    def __init__(self, start: Position, end: Position, moveType: MoveType, direction: Direction = None):
        self.start = Position(start.x, start.y)
        self.end = Position(end.x, end.y)
        self.moveType = moveType
        self.direction = direction