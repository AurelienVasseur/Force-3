from Piece import Piece
from Image import Image


class Square(Piece):
    def __init__(self):
        Piece.__init__(self, Image.SQUARE)
