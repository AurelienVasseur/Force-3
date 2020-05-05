from Pawn import Pawn
from Square import Square
from Movement import Movement
from Selector import Selector
from CoordinatesPrintGraphic import CoordinatesPrintGraphic
import numpy as np

class GameBoard:
    def __init__(self):
        self.pawnsInit = np.zeros([3,2])
        self.gridPawn = np.zeros([3,3])
        self.gridSquare = np.zeros([3,3])
        self.gridLastSquare = np .zeros([3,3])
        self.selectorMovement = Selector()
        self.selectorPieceSelected = Selector()
        self.coordinatesPrintGraphic = CoordinatesPrintGraphic()

        

    def movementPawn(self,_movement,_pawn):
        if _movement == Movement.RIGHT:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if checkPossibilitiesMovementPawn(_movement,_pawn):
                _pawn.position=[x+1,y]
                self.gridPawn[x][y] = 0 #Update last position on grid
                self.gridPawn[x+1][y] = 1 #Update new position on grid
                _pawn.positionImage = self.coordinatesPrintGraphic[x+1][y]

        if _movement == Movement.LEFT:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if checkPossibilitiesMovementPawn(_movement,_pawn):
                _pawn.position=[x-1,y]
                self.gridPawn[x][y] = 0 #Update last position on grid
                self.gridPawn[x-1][y] = 1 #Update new position on grid
                _pawn.positionImage = self.coordinatesPrintGraphic[x-1][y]

        if _movement == Movement.UP:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if checkPossibilitiesMovementPawn(_movement,_pawn):
                _pawn.position=[x,y+1]
                self.gridPawn[x][y] = 0 #Update last position on grid
                self.gridPawn[x][y+1] = 1 #Update new position on grid
                _pawn.positionImage = self.coordinatesPrintGraphic[x][y+1]

        if _movement == Movement.DOWN:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if checkPossibilitiesMovementPawn(_movement,_pawn):
                _pawn.position=[x,y-1]
                self.gridPawn[x][y] = 0 #Update last position on grid
                self.gridPawn[x][y-1] = 1 #Update new position on grid
                _pawn.positionImage = self.coordinatesPrintGraphic[x][y-1]



    def movementSquare(self,_movement,_square):
        if _movement == Movement.RIGHT:
            x = _square.position[0]
            y = _square.position[1]
            if checkPossibilitiesMovementSquare(_movement,_square):
                _square.position=[x+1,y]
                self.gridSquare[x][y] = 0 #Update last position on grid
                self.gridSquare[x+1][y] = 1 #Update new position on grid
                _square.positionImage = self.coordinatesPrintGraphic[x+1][y]

        if _movement == Movement.LEFT:
            x = _square.position[0]
            y = _square.position[1]
            if checkPossibilitiesMovementSquare(_movement,_square):
                _square.position=[x-1,y]
                self.gridSquare[x][y] = 0 #Update last position on grid
                self.gridSquare[x-1][y] = 1 #Update new position on grid
                _square.positionImage = self.coordinatesPrintGraphic[x-1][y]

        if _movement == Movement.UP:
            x = _square.position[0]
            y = _square.position[1]
            if checkPossibilitiesMovementSquare(_movement,_square):
                _square.position=[x,y+1]
                self.gridSquare[x][y] = 0 #Update last position on grid
                self.gridSquare[x][y+1] = 1 #Update new position on grid
                _square.positionImage = self.coordinatesPrintGraphic[x][y+1]

        if _movement == Movement.DOWN:
            x = _square.position[0]
            y = _square.position[1]
            if checkPossibilitiesMovementSquare(_movement,_square):
                _square.position=[x,y-1]
                self.gridSquare[x][y] = 0 #Update last position on grid
                self.gridSquare[x][y-1] = 1 #Update new position on grid
                _square.positionImage = self.coordinatesPrintGraphic[x][y-1]



    def checkPossibilitiesMovementPawn(self,_movement,_pawn):
        #A définir

    def checkPossibilitiesMovementSquare(self,_movement,_square):
        #A définir
