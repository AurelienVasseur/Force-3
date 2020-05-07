import numpy as np
from Pawn import Pawn
from Color import Color
from Square import Square
from Movement import Movement
from Selector import Selector
from CoordinatesPrintGraphic import CoordinatesPrintGraphic



class GameBoard:
    def __init__(self):
        ### self.pawnsInit = np.zeros([3,2]) #marche pas pour ligne 20, car on peut pas mettre un Pawn au lieu d'un entier
        # Il faut initialiser le tableau de type Pawn (Rows et cols inversés!)
        self.pawnsInit = [[Pawn(None) for i in range(2)] for y in range(3)]
        self.gridPawn = np.array([3, 3])  # initialiser que avec des None
        # Il faut initialiser le tableau de type Square
        self.gridSquare = [[Square() for i in range(3)] for y in range(3)]
        # faire juste coordonnées et vérifier
        self.gridLastSquare = np.zeros([3, 3])

        #self.selectorMovement = Selector()       # A MODIFIER -> IL FAUT L'INITIALISER
        #self.selectorPieceSelected = Selector()  # A MODIFIER -> IL FAUT L'INITIALISER

        #White pawns
        for i in range(3):
            # Il faut utiliser np.array sinon erreur
            np.array(self.pawnsInit)[i, 0] = Pawn(Color.WHITE)
        #Black pawns init
        for i in range(3):
            np.array(self.pawnsInit)[i, 1] = Pawn(Color.BLACK)
        #Squares init
        np.array(self.gridSquare)[1, 1] = None

    def movementPawnFromPawnInitToGridPawn(self, _pawn, _newPosition):
        x = _pawn.position[0]
        y = _pawn.position[1]
        if self.checkPossibilitiesPositionPawn(_newPosition):
            # il faudrait plutot pop le pawn en question
            # Update last position on grid
            np.array(self.pawnsInit)[x, y] = None

            # Update pawn's position
            _pawn.position = [_newPosition[0], _newPosition[1]]
            self.gridPawn[_newPosition[0], _newPosition[1]
                          ] = _pawn  # Update new position on grid
    def movementPawn(self, _movement, _pawn):
        if _movement == Movement.RIGHT:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if self.checkPossibilitiesMovementPawn(_movement, _pawn):
                _pawn.position = [x+1, y]
                self.gridPawn[x, y] = 0  # Update last position on grid
                self.gridPawn[x+1, y] = _pawn  # Update new position on grid
                _pawn.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN[x+1][y][0]
                _pawn.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN[x+1][y][1]

        if _movement == Movement.LEFT:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if self.checkPossibilitiesMovementPawn(_movement, _pawn):
                _pawn.position = [x-1, y]
                self.gridPawn[x, y] = 0  # Update last position on grid
                self.gridPawn[x-1, y] = _pawn  # Update new position on grid
                _pawn.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN[x-1][y][0]
                _pawn.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN[x-1][y][1]

        if _movement == Movement.UP:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if self.checkPossibilitiesMovementPawn(_movement, _pawn):
                _pawn.position = [x, y-1]
                self.gridPawn[x, y] = 0  # Update last position on grid
                self.gridPawn[x, y-1] = _pawn  # Update new position on grid
                _pawn.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN[x][y-1][0]
                _pawn.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN[x][y-1][1]

        if _movement == Movement.DOWN:
            x = _pawn.position[0]
            y = _pawn.position[1]
            if self.checkPossibilitiesMovementPawn(_movement, _pawn):
                _pawn.position = [x, y+1]
                self.gridPawn[x, y] = 0  # Update last position on grid
                self.gridPawn[x, y+1] = _pawn  # Update new position on grid
                _pawn.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN[x][y+1][0]
                _pawn.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN[x][y+1][1]
    def movementSquare(self, _movement, _square):
        if _movement == Movement.RIGHT:
            x = _square.position[0]
            y = _square.position[1]
            if self.checkPossibilitiesMovementSquare(_movement, _square):
                _square.position = [x+1, y]
                self.gridSquare[x, y] = 0  # Update last position on grid
                # Update new position on grid
                self.gridSquare[x+1, y] = _square
                _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE[x+1][y][0]
                _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE[x+1][y][1]

        if _movement == Movement.LEFT:
            x = _square.position[0]
            y = _square.position[1]
            if self.checkPossibilitiesMovementSquare(_movement, _square):
                _square.position = [x-1, y]
                self.gridSquare[x, y] = 0  # Update last position on grid
                # Update new position on grid
                self.gridSquare[x-1, y] = _square
                _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE[x-1][y][0]
                _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE[x-1][y][1]

        if _movement == Movement.UP:
            x = _square.position[0]
            y = _square.position[1]
            if self.checkPossibilitiesMovementSquare(_movement, _square):
                _square.position = [x, y-1]
                self.gridSquare[x, y] = 0  # Update last position on grid
                # Update new position on grid
                self.gridSquare[x, y-1] = _square
                _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE[x][y-1][0]
                _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE[x][y-1][1]

        if _movement == Movement.DOWN:
            x = _square.position[0]
            y = _square.position[1]
            if self.checkPossibilitiesMovementSquare(_movement, _square):
                _square.position = [x, y+1]
                self.gridSquare[x, y] = 0  # Update last position on grid
                # Update new position on grid
                self.gridSquare[x, y+1] = _square
                _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE[x][y+1][0]
                _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE[x][y+1][1]
    def checkPossibilitiesMovementPawn(self, _movement, _pawn):
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

        return self.checkPossibilitiesPositionPawn([newX, newY])

    def checkPossibilitiesMovementSquare(self, _movement, _square):
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

        return self.checkPossibilitiesPositionSquare([newX, newY])

    def checkPossibilitiesPositionPawn(self, _position):
        x = _position[0]
        y = _position[1]
        if 0 <= x < 3 and 0 <= y < 3 and self.gridPawn[x, y] == 0:
            return True
        else:
            return False

    def checkPossibilitiesPositionSquare(self, _position):
        x = _position[0]
        y = _position[1]
        if 0 <= x < 3 and 0 <= y < 3 and self.gridSquare[x, y] == 0:
            return True
        else:
            return False

