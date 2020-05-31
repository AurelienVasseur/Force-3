from Color import Color
from Selector import Selector
from Position import Position

class Player:

    def __init__(self, color: Color):
        self.color = color
        self.isTurnActive = False
        self.selector = None
        if(self.color == Color.BLACK):
            self.selector = Selector(Position(3, 0), 0, 3)
        else:
            self.selector = Selector(Position(-1, 0), -1, 2)
        

    
    def placePawnOnBoard(self):
        return