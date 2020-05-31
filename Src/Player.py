from Color import Color
from Selector import Selector
from Position import Position
from copy import deepcopy

class Player:

    def __init__(self, color: Color, isTurnActive = False, selector = None):
        self.color = deepcopy(color)
        self.isTurnActive = deepcopy(isTurnActive)
        self.selector = deepcopy(selector)
        if(self.selector is None):
            if(self.color == Color.BLACK):
                self.selector = Selector(Position(3, 0), 0, 3)
            else:
                self.selector = Selector(Position(-1, 0), -1, 2)


    
    def placePawnOnBoard(self):
        return