from Cell import Cell
from Position import Position
from Color import Color

class Pawn(Cell):

    def __init__(self, position: Position, color: Color):
        super(Pawn, self).__init__(position, type(self).__name__)
        self.color = color

    def __str__(self):
        return "{ " + "position: {}".format(str(self.position)) + ", type: {}".format(self.type) + ", color: {}".format(self.color) + " }"

