from .Cell import Cell
from .Position import Position

class Square(Cell):

    def __init__(self, position = None):
        super(Square, self).__init__(position, type(self).__name__)

    def __str__(self):
        return super(Square, self).__str__()


