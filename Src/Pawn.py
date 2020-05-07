from Piece import Piece
from Image import Image
from Color import Color


class Pawn(Piece):
    def __init__(self, _color):
        if _color == Color.BLACK:
            Piece.__init__(self, Image.PAWN_BLACK)
        else:
            Piece.__init__(self, Image.PAWN_WHITE)
        self.Color = _color
        self.number = 10
