from Cell import Cell
from Square import Square
from Pawn import Pawn
from Color import Color
from Position import Position

class GameBoard:

    def __init__(self):
        self.grid = [[None for j in range(3)] for i in range(3)]
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                self.grid[i][j] = Square(Position(i, j))
        self.grid[1][1] = Cell(Position(1, 1))
        
        self.pawns = [[None for j in range(3)] for i in range(2)]
        for j in range(3):
            self.pawns[0][j] = Pawn(None, Color.BLACK)
            self.pawns[1][j] = Pawn(None, Color.WHITE)