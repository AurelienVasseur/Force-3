import numpy as np
from Pawn import Pawn
from Color import Color
from Square import Square
from Movement import Movement
from Selector import Selector
from CoordinatesPrintGraphic import CoordinatesPrintGraphic


class GameBoard:
    def __init__(self):
        #Initialisation de la matrice des pions de début de partie, la couleur a été mise par défaut à 'None'
        self.pawnsInit = np.array([[Pawn(None) for i in range(2)] for y in range(3)]) 

        #Initialisation de la matrice des pions sur le tablier, la couleur de chaque pion a été mise à 'None'
        #Pour savoir si un pion est présent ou non sur le tablier, il faut se fier à sa couleur. Si la couleur du pion présent sur une
        # case est 'None', alors il n'y a pas de pion
        self.gridPawn = np.array([[Pawn(None) for i in range(3)] for y in range(3)])

        #Initialisation de la matrice des cases du tablier, elles sont pour le moment toutes remplies ('empty' = False)
        self.gridSquare = np.array([[Square(False) for i in range(3)] for y in range(3)])

        #Initialisation du tableau correspondant aux coordonnées [x,y] du coup précédent, les valeurs par défauts sont [-1,-1]
        self.gridLastSquare = np.array([1,1]) 
        self.gridLastSquare[0] = -1
        self.gridLastSquare[1] = -1

        #Initialisation des pions blancs
        for i in range(3):
            self.pawnsInit[i,0].Color = Color.WHITE #Il faut utiliser np.array sinon erreur
        #Initialisation des pions noirs
        for i in range(3):
            self.pawnsInit[i,1].Color = Color.BLACK
        #Initialisation des cases du tablier
        self.gridSquare[1,1].empty = True 

        #Initialisation des selecteurs
        #self.selectorMovement = Selector()       # A MODIFIER -> IL FAUT L'INITIALISER
        #self.selectorPieceSelected = Selector()  # A MODIFIER -> IL FAUT L'INITIALISER


    #_position correspond à la position du pion, _newPosition correspond à la position destination du pion
    def movementPawnFromPawnInitToGridPawn(self,_pawn, _position,_newPosition):
        x = _position[0]
        y = _position[1]
        #Si la couleur du pion est None, alors cela signifie qu'il n'existe pas
        if checkPossibilitiesMovementPawn(_newPosition):  
            self.gridPawn[x, y] = _pawn
            self.pawnsInit[x,y] = Pawn(None) 
            #On met à jour la position graphique du pion
            _pawn.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x][y][0]
            _pawn.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x][y][1]

    def movementPawn(self, _pawn, _positionArray, _positionDestination):
        #On verifie que la case de destination n'est pas occupée par un pion
        if(self.checkPossibilitiesMovementPawn(_positionDestination)):
            #Position du pion dans la matrice
            x = _positionArray[0] 
            y = _positionArray[1]
            #Destination
            x1 = _positionDestination[0]
            y1 = _positionDestination[1]

            #On déplace le pion vers la case déstination
            self.gridPawn[x1, y1] = _pawn
            self.gridPawn[x, y] = Pawn(None)

            #On met à jour la position graphique du pion
            _pawn.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x1][y1][0]
            _pawn.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_PAWN.value[x1][y1][1]

            
    def movementSquare(self, _movement, _square, _positionArray): #_positionArray correspond à la position de la case (c'est la position dans la matrice)
        if _square.empty == False: #On vérifie si la case n'est pas celle qui est vide
            #Position de la case dans la matrice
            x = _positionArray[0]
            y = _positionArray[1]

            #on vérifie si un pion se trouve sur la case
            pawnPresent = False
            if(self.gridPawn[x, y].Color != None):
                pawnPresent = True

            #on vérifie les types de mouvements    
            if _movement == Movement.RIGHT:
                #Si la case de droite est vide, alors on inverse les deux cases
                if self.checkPossibilitiesMovementSquare(_movement, _square, _positionArray):
                    squareTemp = self.gridSquare[x+1, y]
                    self.gridSquare[x+1, y] = self.gridSquare[x, y]
                    self.gridSquare[x, y].empty = squareTemp
                    #Enregistrement des valeurs pour le tour suivant
                    self.gridLastSquare[0] = x+1
                    self.gridLastSquare[1] = y
                    _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x+1][y][0]
                    _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x+1][y][1]
                    #on déplace le pion si il y en a un
                    if pawnPresent:
                        self.gridPawn[x+1, y] = self.gridPawn[x, y]
                        self.gridPawn[x, y] = Pawn(None)

            elif _movement == Movement.LEFT:
                if self.checkPossibilitiesMovementSquare(_movement, _square, _positionArray):
                    squareTemp = self.gridSquare[x-1, y]
                    self.gridSquare[x-1, y] = self.gridSquare[x, y]
                    self.gridSquare[x, y].empty = squareTemp
                    #Enregistrement des valeurs pour le tour suivant
                    self.gridLastSquare[0] = x-1
                    self.gridLastSquare[1] = y
                    _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x-1][y][0]
                    _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x-1][y][1]
                    #on déplace le pion si il y en a un
                    if pawnPresent:
                        self.gridPawn[x-1, y] = self.gridPawn[x, y]
                        self.gridPawn[x, y] = Pawn(None)

            elif _movement == Movement.UP:
                if self.checkPossibilitiesMovementSquare(_movement, _square, _positionArray):
                    squareTemp = self.gridSquare[x, y-1]
                    self.gridSquare[x, y-1] = self.gridSquare[x, y]
                    self.gridSquare[x, y].empty = squareTemp
                    #Enregistrement des valeurs pour le tour suivant
                    self.gridLastSquare[0] = x
                    self.gridLastSquare[1] = y-1
                    _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x][y-1][0]
                    _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x][y-1][1]
                    #on déplace le pion si il y en a un
                    if pawnPresent:
                        self.gridPawn[x, y-1] = self.gridPawn[x, y]
                        self.gridPawn[x, y] = Pawn(None)

            elif _movement == Movement.DOWN:
                if self.checkPossibilitiesMovementSquare(_movement, _square, _positionArray):
                    squareTemp = self.gridSquare[x+1, y]
                    self.gridSquare[x, y+1] = self.gridSquare[x, y+1]
                    self.gridSquare[x, y].empty = squareTemp
                    #Enregistrement des valeurs pour le tour suivant
                    self.gridLastSquare[0] = x
                    self.gridLastSquare[1] = y+1
                    _square.positionImage[0] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x][y+1][0]
                    _square.positionImage[1] = CoordinatesPrintGraphic.POSITION_PRINT_SQUARE.value[x][y+1][1]
                    #on déplace le pion si il y en a un
                    if pawnPresent:
                        self.gridPawn[x, y+1] = self.gridPawn[x, y]
                        self.gridPawn[x, y] = Pawn(None)
    
    #_position correspond à la possible position destination du pion
    def checkPossibilitiesMovementPawn(self, _position):
            x = _position[0]
            y = _position[1]
            #On verifie si la case destination est occupée par un pion et qu'une case s'y trouve
            if (self.gridPawn[x, y].Color == None and self.gridSquare[x, y].empty == False):
                return True
            return False

    #_position correspond à la position de la case (elle correspond à la position dans la matrice)
    def checkPossibilitiesMovementSquare(self, _movement, _position):
        x = _position[0]
        y = _position[1]

        if _movement == Movement.RIGHT:
            if (x < 2 and self.gridSquare[x+1, y].empty == True and self.gridLastSquare[0] != x+1):
                return True
            return False

        elif _movement == Movement.LEFT:
            if (x > 0 and self.gridSquare[x-1, y].empty == True and self.gridLastSquare[0] != x-1):
                return True
            return False

        elif _movement == Movement.UP:
            if (y > 0 and self.gridSquare[x, y-1].empty == True and self.gridLastSquare[1] != y-1):
                return True
            return False

        elif _movement == Movement.DOWN:
            if (y < 2 and self.gridSquare[x, y+1].empty == True and self.gridLastSquare[1] != y+1):
                return True
            return False

   




