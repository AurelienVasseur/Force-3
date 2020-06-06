from .Cell import Cell
from .Square import Square
from .Pawn import Pawn
from .Color import Color
from .Position import Position
from copy import deepcopy
from .Player import Player
from .Move import Move
from .MoveType import MoveType
from .GameStatus import GameStatus
from .StatusType import StatusType
from .WinType import WinType
from .Direction import Direction
import random
import math

class GameBoard:

    def __init__(self, gameBoard = None):
        self.grid = [[None for j in range(3)] for i in range(3)]
        self.pawns = [[None for j in range(3)] for i in range(2)]
        self.previousActionWasDoubleSlide = False


        if(gameBoard is not None):
            self.grid = deepcopy(gameBoard.grid)
            self.pawns = deepcopy(gameBoard.pawns)
            self.previousActionWasDoubleSlide = deepcopy(gameBoard.previousActionWasDoubleSlide)
        else:
            
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    self.grid[i][j] = Square(Position(i, j))
            self.grid[1][1] = Cell(Position(1, 1))
            
            
            for j in range(3):
                self.pawns[Color.BLACK.value][j] = Pawn(None, Color.BLACK)
                self.pawns[Color.WHITE.value][j] = Pawn(None, Color.WHITE)

        
    def getPossibleMoves(self, activePlayer: Player):
        possibleMoves = []
        # possible pawn moves
        for playerPawn in self.pawns[activePlayer.color.value]:
            for i in range(len(self.grid)):
                for j in range(len(self.grid[i])):
                    cell = self.grid[i][j]
                    if(cell.type == "Square"):
                        if(playerPawn.position is None):
                            # it is possible to place unused pawn on free square
                            yIndex = -1
                            playerIndex = activePlayer.color.value
                            for i in range(len(self.pawns[playerIndex])):
                                if(self.pawns[playerIndex][i].position == None):
                                    yIndex = i
                            possibleMoves.append(Move(Position(playerIndex, yIndex), cell.position, MoveType.PUT_UNUSED_PAWN_ON_SQUARE))
                        if(playerPawn.position is not None):
                            # it is possible to place used pawn on free
                            possibleMoves.append(Move(playerPawn.position, cell.position, MoveType.PUT_USED_PAWN_ON_SQUARE))
        
        # possible slide action
        for i in range(len(self.grid)):
            for j in range(len(self.grid[i])):
                cell = self.grid[i][j]
                if(cell.type == "Cell"):
                    if(cell.position.x == 0):
                        # first line
                        if(cell.position.y == 0):
                            # top left corner
                            possibleMoves.append(Move(Position(0, 1), cell.position, MoveType.SIMPLE_SLIDE, Direction.LEFT))
                            possibleMoves.append(Move(Position(1, 0), cell.position, MoveType.SIMPLE_SLIDE, Direction.UP))
                            if(not self.previousActionWasDoubleSlide):
                                possibleMoves.append(Move(Position(0, 2), cell.position, MoveType.DOUBLE_SLIDE, Direction.LEFT))
                                possibleMoves.append(Move(Position(2, 0), cell.position, MoveType.DOUBLE_SLIDE, Direction.UP))
                        elif(cell.position.y == 2):
                            # top right corner
                            possibleMoves.append(Move(Position(0, 1), cell.position, MoveType.SIMPLE_SLIDE, Direction.RIGHT))
                            possibleMoves.append(Move(Position(1, 2), cell.position, MoveType.SIMPLE_SLIDE, Direction.UP))
                            if(not self.previousActionWasDoubleSlide):
                                possibleMoves.append(Move(Position(0, 0), cell.position, MoveType.DOUBLE_SLIDE, Direction.RIGHT))
                                possibleMoves.append(Move(Position(2, 2), cell.position, MoveType.DOUBLE_SLIDE, Direction.UP))
                        else:
                            # top middle
                            possibleMoves.append(Move(Position(0, 0), cell.position, MoveType.SIMPLE_SLIDE, Direction.LEFT))
                            possibleMoves.append(Move(Position(0, 2), cell.position, MoveType.SIMPLE_SLIDE, Direction.RIGHT))
                            possibleMoves.append(Move(Position(1, 1), cell.position, MoveType.SIMPLE_SLIDE, Direction.UP))
                            if(not self.previousActionWasDoubleSlide):
                                possibleMoves.append(Move(Position(2, 1), cell.position, MoveType.DOUBLE_SLIDE, Direction.UP))
                    elif(cell.position.x == 2):
                        # last line
                        if(cell.position.y == 0):
                            # bottom left corner
                            possibleMoves.append(Move(Position(2, 1), cell.position, MoveType.SIMPLE_SLIDE, Direction.LEFT))
                            possibleMoves.append(Move(Position(1, 0), cell.position, MoveType.SIMPLE_SLIDE, Direction.DOWN))
                            if(not self.previousActionWasDoubleSlide):
                                possibleMoves.append(Move(Position(2, 2), cell.position, MoveType.DOUBLE_SLIDE, Direction.LEFT))
                                possibleMoves.append(Move(Position(0, 0), cell.position, MoveType.DOUBLE_SLIDE, Direction.DOWN))
                        elif(cell.position.y == 2):
                            # bottom right corner
                            possibleMoves.append(Move(Position(2, 1), cell.position, MoveType.SIMPLE_SLIDE, Direction.RIGHT))
                            possibleMoves.append(Move(Position(1, 2), cell.position, MoveType.SIMPLE_SLIDE, Direction.DOWN))
                            if(not self.previousActionWasDoubleSlide):
                                possibleMoves.append(Move(Position(2, 0), cell.position, MoveType.DOUBLE_SLIDE, Direction.RIGHT))
                                possibleMoves.append(Move(Position(0, 2), cell.position, MoveType.DOUBLE_SLIDE, Direction.DOWN))
                        else:
                            # bottom middle
                            possibleMoves.append(Move(Position(2, 0), cell.position, MoveType.SIMPLE_SLIDE, Direction.RIGHT))
                            possibleMoves.append(Move(Position(2, 2), cell.position, MoveType.SIMPLE_SLIDE, Direction.LEFT))
                            possibleMoves.append(Move(Position(1, 1), cell.position, MoveType.SIMPLE_SLIDE, Direction.DOWN))
                            if(not self.previousActionWasDoubleSlide):
                                possibleMoves.append(Move(Position(0, 1), cell.position, MoveType.DOUBLE_SLIDE, Direction.DOWN))
                    else:
                        # middle line
                        if(cell.position.y == 0):
                            # middle left
                            possibleMoves.append(Move(Position(1, 1), cell.position, MoveType.SIMPLE_SLIDE, Direction.LEFT))
                            possibleMoves.append(Move(Position(0, 0), cell.position, MoveType.SIMPLE_SLIDE, Direction.DOWN))
                            possibleMoves.append(Move(Position(2, 0), cell.position, MoveType.SIMPLE_SLIDE, Direction.UP))
                        elif(cell.position.y == 2):
                            # middle right
                            possibleMoves.append(Move(Position(1, 1), cell.position, MoveType.SIMPLE_SLIDE, Direction.RIGHT))
                            possibleMoves.append(Move(Position(0, 2), cell.position, MoveType.SIMPLE_SLIDE, Direction.DOWN))
                            possibleMoves.append(Move(Position(2, 2), cell.position, MoveType.SIMPLE_SLIDE, Direction.UP))
                        else:
                            # middle middle
                            possibleMoves.append(Move(Position(1, 0), cell.position, MoveType.SIMPLE_SLIDE, Direction.RIGHT))
                            possibleMoves.append(Move(Position(1, 2), cell.position, MoveType.SIMPLE_SLIDE, Direction.LEFT))
                            possibleMoves.append(Move(Position(0, 1), cell.position, MoveType.SIMPLE_SLIDE, Direction.DOWN))
                            possibleMoves.append(Move(Position(2, 1), cell.position, MoveType.SIMPLE_SLIDE, Direction.UP))
        # print("nbPossibleMoves={}".format(len(possibleMoves)))
        return possibleMoves

    
    def getGameStatus(self):
        # line victory check
        for i in range(len(self.grid)):
            line = self.grid[i]
            if(line[0].type == "Pawn" and line[1].type == "Pawn" and line[2].type == "Pawn" and line[0].color == line[1].color and line[1].color == line[2].color):
                return GameStatus(StatusType.END, WinType.LINE, line[0].color)
        # column victory check
        grid = self.grid
        for i in range(len(self.grid)):
            if(grid[0][i].type == "Pawn" and grid[1][i].type == "Pawn" and grid[2][i].type == "Pawn" and grid[0][i].color == grid[1][i].color and grid[1][i].color == grid[2][i].color):
                return GameStatus(StatusType.END, WinType.COLUMN, grid[0][i].color)
        # diagonal victory check
        if(grid[0][0].type == "Pawn" and grid[1][1].type == "Pawn" and grid[2][2].type == "Pawn" and grid[0][0].color == grid[1][1].color and grid[1][1].color == grid[2][2].color):
            return GameStatus(StatusType.END, WinType.DIAGONAL, grid[0][0].color)
        if(grid[0][2].type == "Pawn" and grid[1][1].type == "Pawn" and grid[2][0].type == "Pawn" and grid[0][2].color == grid[1][1].color and grid[1][1].color == grid[2][0].color):
            return GameStatus(StatusType.END, WinType.REVERSE_DIAGONAL, grid[0][2].color)
        return GameStatus(StatusType.ONGOING)

    def isGameEnded(self):
        return self.getGameStatus().status == StatusType.END

    
    def move(self, move: Move):
        if(move.moveType == MoveType.PUT_UNUSED_PAWN_ON_SQUARE):
            self.grid[move.end.x][move.end.y] = self.pawns[move.start.x][move.start.y]
            self.grid[move.end.x][move.end.y].position = Position(move.end.x, move.end.y)
        elif(move.moveType == MoveType.PUT_USED_PAWN_ON_SQUARE):
            self.grid[move.end.x][move.end.y] = self.grid[move.start.x][move.start.y]
            self.grid[move.end.x][move.end.y].position = Position(move.end.x, move.end.y)
            self.grid[move.start.x][move.start.y] = Square(Position(move.start.x, move.start.y))
        elif(move.moveType == MoveType.SIMPLE_SLIDE):
            self.grid[move.end.x][move.end.y] = self.grid[move.start.x][move.start.y]
            self.grid[move.end.x][move.end.y].position = Position(move.end.x, move.end.y)
            self.grid[move.start.x][move.start.y] = Cell(Position(move.start.x, move.start.y))
        elif(move.moveType == MoveType.DOUBLE_SLIDE):
            offset = Position()
            if(move.direction == Direction.UP):
                offset = Position(-1, 0)
            elif(move.direction == Direction.DOWN):
                offset = Position(1, 0)
            elif(move.direction == Direction.LEFT):
                offset = Position(0, -1)
            elif(move.direction == Direction.RIGHT):
                offset = Position(0, 1)

            self.grid[move.end.x][move.end.y] = self.grid[move.start.x + offset.x][move.start.y + offset.y]
            self.grid[move.end.x][move.end.y].position = Position(move.end.x, move.end.y)
            self.grid[move.start.x + offset.x][move.start.y + offset.y] = self.grid[move.start.x][move.start.y]
            self.grid[move.start.x + offset.x][move.start.y + offset.y].position = Position(move.start.x + offset.x, move.start.y + offset.y)
            self.grid[move.start.x][move.start.y] = Cell(Position(move.start.x, move.start.y))
        
        
        

    # EVALUATION METHOD
    def getPlayerScore(self, player):
        #return math.floor(random.random() * 100)
        sign = -1
        if(player.color == Color.BLACK):
            sign = 1
        gameStatus = self.getGameStatus()
        if(gameStatus.status == StatusType.END):
            if(gameStatus.winner == player.color):
                return sign * 1
            return sign * -1
        return 0