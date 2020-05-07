from Pawn import Pawn
from Color import Color
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
        self.gridLastSquare = np.zeros([3,3])
        #self.selectorMovement = Selector()       # A MODIFIER -> IL FAUT L'INITIALISER
        #self.selectorPieceSelected = Selector()  # A MODIFIER -> IL FAUT L'INITIALISER
        #White pawns
        for i in range(3):
            self.pawnsInit[i,0] = Pawn(Color.WHITE)
        #Black pawns init
        for i in range(3):
            self.pawnsInit[i,1] = Pawn(Color.BLACK)
        #Squares init
        x=0
        y=0
        for i in range(8):
            if x>2:
                x=0
                y+=1
            if x!=1 or y!=1:
                self.gridSquare[x,y] = Square()
            else:
                self.gridSquare[2,2] = Square()
            x+=1 



    def movementPawnFromPawnInitToGridPawn(self,_pawn,_newPosition):
        x = _pawn.position[0]
        y = _pawn.position[1]
        if checkPossibilitiesPositionPawn(_newPosition):  
            self.pawnsInit[x,y] = 0 #Update last position on grid
            _pawn.position = [_newPosition[0],_newPosition[1]]  #Update pawn's position
            self.gridPawn[_newPosition[0],_newPosition[1]] = _pawn  #Update new position on grid            


    def movementPawn(self,_movement,_pawn):
        if _movement == Movement.RIGHT:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if checkPossibilitiesMovementPawn(_movement,_pawn):
                _pawn.position=[x+1,y]
                self.gridPawn[x,y] = 0 #Update last position on grid
                self.gridPawn[x+1,y] = _pawn  #Update new position on grid
                _pawn.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x+1,y][0]
                _pawn.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x+1,y][1]

        if _movement == Movement.LEFT:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if checkPossibilitiesMovementPawn(_movement,_pawn):
                _pawn.position=[x-1,y]
                self.gridPawn[x,y] = 0 #Update last position on grid
                self.gridPawn[x-1,y] = _pawn #Update new position on grid
                _pawn.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x-1,y][0]
                _pawn.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x-1,y][1]

        if _movement == Movement.UP:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if checkPossibilitiesMovementPawn(_movement,_pawn):
                _pawn.position=[x,y-1]
                self.gridPawn[x,y] = 0 #Update last position on grid
                self.gridPawn[x,y-1] = _pawn #Update new position on grid
                _pawn.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x,y-1][0]
                _pawn.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x,y-1][1]

        if _movement == Movement.DOWN:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if checkPossibilitiesMovementPawn(_movement,_pawn):
                _pawn.position=[x,y+1]
                self.gridPawn[x,y] = 0 #Update last position on grid
                self.gridPawn[x,y+1] = _pawn #Update new position on grid
                _pawn.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x,y+1][0]
                _pawn.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x,y+1][1]



    def movementSquare(self,_movement,_square):
        if _movement == Movement.RIGHT:
            x = _square.position[0]
            y = _square.position[1]
            if checkPossibilitiesMovementSquare(_movement,_square):
                _square.position=[x+1,y]
                self.gridSquare[x,y] = 0 #Update last position on grid
                self.gridSquare[x+1,y] = _square #Update new position on grid
                _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x+1,y][0]
                _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x+1,y][1]

        if _movement == Movement.LEFT:
            x = _square.position[0]
            y = _square.position[1]
            if checkPossibilitiesMovementSquare(_movement,_square):
                _square.position=[x-1,y]
                self.gridSquare[x,y] = 0 #Update last position on grid
                self.gridSquare[x-1,y] = _square #Update new position on grid
                _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x-1,y][0]
                _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x-1,y][1]

        if _movement == Movement.UP:
            x = _square.position[0]
            y = _square.position[1]
            if checkPossibilitiesMovementSquare(_movement,_square):
                _square.position=[x,y-1]
                self.gridSquare[x,y] = 0 #Update last position on grid
                self.gridSquare[x,y-1] = _square #Update new position on grid
                _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x,y-1][0]
                _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x,y-1][1]

        if _movement == Movement.DOWN:
            x = _square.position[0]
            y = _square.position[1]
            if checkPossibilitiesMovementSquare(_movement,_square):
                _square.position=[x,y+1]
                self.gridSquare[x,y] = 0 #Update last position on grid
                self.gridSquare[x,y+1] = _square #Update new position on grid
                _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x,y+1][0]
                _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x,y+1][1]


    def checkPossibilitiesMovementPawn(self,_movement,_pawn):
        newX = None
        newY = None

        if _movement == Movement.RIGHT:
            newX = _pawn.position[0]+1
            newY = _pawn.position[1]

        elif _movement == Movement.LEFT:
            newX = _pawn.position[0]-1
            newY = _pawn.position[1]

        elif _movement == Movement.UP:
            newX = _pawn.position[0]
            newY = _pawn.position[1]-1

        elif _movement == Movement.DOWN:
            newX = _pawn.position[0]
            newY = _pawn.position[1]+1

        else:
            return False

        return checkPossibilitiesPositionPawn([newX,newY])    

    def checkPossibilitiesMovementSquare(self,_movement,_square):
        newX = None
        newY = None

        if _movement == Movement.RIGHT:
            newX = _square.position[0]+1
            newY = _square.position[1]

        elif _movement == Movement.LEFT:
            newX = _square.position[0]-1
            newY = _square.position[1]

        elif _movement == Movement.UP:
            newX = _square.position[0]
            newY = _square.position[1]-1

        elif _movement == Movement.DOWN:
            newX = _square.position[0]
            newY = _square.position[1]+1

        else:
            return False

        return checkPossibilitiesPositionSquare([newX,newY]) 
    

    def checkPossibilitiesPositionPawn(self,_position):
        x=_position[0]
        y=_position[1]
        if 0<=x<3 and 0<=y<3 and self.gridPawn[x,y] == 0:
            return True
        else:
            return False

    def checkPossibilitiesPositionSquare(self,_position):
        x=_position[0]
        y=_position[1]
        if 0<=x<3 and 0<=y<3 and self.gridSquare[x,y] == 0:
            return True
        else:
            return False




