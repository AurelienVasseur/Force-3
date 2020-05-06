from GameBoard import GameBoard
from Player import Player

class GameManager:
    def __init__(self):
        self.GameBoard=GameBoard()
        self.player_1=Player()
        self.player_2=Player()