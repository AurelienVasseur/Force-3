from Piece import Piece
from Image import Image


class Square(Piece):
    def __init__(self, _empty):
        Piece.__init__(self, Image.SQUARE)
        self.empty = _empty