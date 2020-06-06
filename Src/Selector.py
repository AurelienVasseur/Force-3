from .Position import Position
from .Direction import Direction
from .Move import Move
from .MoveType import MoveType

class Selector:

    def __init__(self, position: Position, minLine, maxLine):
        self.position = position
        self.minLine = minLine
        self.maxLine = maxLine
        self.isActive = False
        self.activeCell = None

    def isPositionValid(self, position: Position):
        return position.x >= self.minLine and position.x <= self.maxLine and position.y >= 0 and position.y < 3

    def setPosition(self, x, y):
        self.position.x = x if x >= self.minLine and x <= self.maxLine else self.position.x
        self.position.y = y if y >= 0 and y < 3 else self.position.y

    def isInGrid(self):
        return self.position.x >= 0 and self.position.x < 3

    def move(self, direction: Direction):
        if(direction == Direction.UP):
            self.setPosition(self.position.x - 1, self.position.y)
        if(direction == Direction.DOWN):
            self.setPosition(self.position.x + 1, self.position.y)
        if(direction == Direction.LEFT):
            self.setPosition(self.position.x, self.position.y - 1)
        if(direction == Direction.RIGHT):
            self.setPosition(self.position.x, self.position.y + 1)

    def instantMove(self, newPosition: Position):
        if(self.isPositionValid(newPosition)):
            self.setPosition(newPosition.x, newPosition.y)
        else:
            print("Selector::instantMove: newPosition out of bounds (invalid)")

    def toggleSelect(self, gameBoard, playerIndex):
        if(not self.isActive):
            # print("Pressed Enter while inactive")
            if(self.isInGrid()):
                cell = gameBoard.grid[self.position.x][self.position.y]
                if(cell.type == "Square" or cell.type == "Pawn"):
                    # print("Selected Square or owned Pawn in grid")
                    self.isActive = True
                    self.activeCell = gameBoard.grid[self.position.x][self.position.y]
                    return False
            elif(gameBoard.pawns[playerIndex][self.position.y].position is None):
                # print("Selected unused Pawn")
                self.isActive = True
                self.activeCell = gameBoard.pawns[playerIndex][self.position.y]
                return False
        else:
            # print("Pressed Enter while active")
            if(self.isInGrid()):
                if(gameBoard.grid[self.position.x][self.position.y].type == "Cell" and self.activeCell.position != None):
                    if(self.position.x == self.activeCell.position.x):
                        # move cells on same line to current Cell
                        if(self.position.y > self.activeCell.position.y):
                            # move to right
                            if(self.position.y - self.activeCell.position.y > 1):
                                if(not gameBoard.previousActionWasDoubleSlide):
                                    # move 2 to right
                                    gameBoard.move(Move(self.activeCell.position, self.position, MoveType.DOUBLE_SLIDE, Direction.RIGHT))
                                    self.isActive = False
                                    self.activeCell = None
                                    gameBoard.previousActionWasDoubleSlide = True
                                    return True
                                else:
                                    # cancel try to double move for 2nd time
                                    self.isActive = False
                                    self.activeCell = None
                                    return False
                            else:
                                # move 1 to right
                                gameBoard.move(Move(self.activeCell.position, self.position, MoveType.SIMPLE_SLIDE, Direction.RIGHT))
                                self.isActive = False
                                self.activeCell = None
                                gameBoard.previousActionWasDoubleSlide = False
                                return True
                        else:
                            # move to left
                            if(self.activeCell.position.y - self.position.y > 1):
                                if(not gameBoard.previousActionWasDoubleSlide):
                                    # move 2 to left
                                    gameBoard.move(Move(self.activeCell.position, self.position, MoveType.DOUBLE_SLIDE, Direction.LEFT))
                                    self.isActive = False
                                    self.activeCell = None
                                    gameBoard.previousActionWasDoubleSlide = True
                                    return True
                                else:
                                    # cancel try to double move for 2nd time
                                    self.isActive = False
                                    self.activeCell = None
                                    return False
                            else:
                                # move 1 to left
                                gameBoard.move(Move(self.activeCell.position, self.position, MoveType.SIMPLE_SLIDE, Direction.LEFT))
                                self.isActive = False
                                self.activeCell = None
                                gameBoard.previousActionWasDoubleSlide = False
                                return True
                    elif(self.position.y == self.activeCell.position.y):
                        # move cells on same column to current Cell
                        if(self.position.x > self.activeCell.position.x):
                            # move down
                            if(self.position.x - self.activeCell.position.x > 1):
                                if(not gameBoard.previousActionWasDoubleSlide):
                                    # move 2 down
                                    gameBoard.move(Move(self.activeCell.position, self.position, MoveType.DOUBLE_SLIDE, Direction.DOWN))
                                    self.isActive = False
                                    self.activeCell = None
                                    gameBoard.previousActionWasDoubleSlide = True
                                    return True
                                else:
                                    # cancel try to double move for 2nd time
                                    self.isActive = False
                                    self.activeCell = None
                                    return False
                            else:
                                # move 1 down
                                gameBoard.move(Move(self.activeCell.position, self.position, MoveType.SIMPLE_SLIDE, Direction.DOWN))
                                self.isActive = False
                                self.activeCell = None
                                gameBoard.previousActionWasDoubleSlide = False
                                return True
                        else:
                            # move up
                            if(self.activeCell.position.x - self.position.x > 1):
                                if(not gameBoard.previousActionWasDoubleSlide):
                                # move 2 up
                                    gameBoard.move(Move(self.activeCell.position, self.position, MoveType.DOUBLE_SLIDE, Direction.UP))
                                    self.isActive = False
                                    self.activeCell = None
                                    gameBoard.previousActionWasDoubleSlide = True
                                    return True
                                else:
                                    # cancel try to double move for 2nd time
                                    self.isActive = False
                                    self.activeCell = None
                                    return False
                            else:
                                # move 1 up
                                gameBoard.move(Move(self.activeCell.position, self.position, MoveType.SIMPLE_SLIDE, Direction.UP))
                                self.isActive = False
                                self.activeCell = None
                                gameBoard.previousActionWasDoubleSlide = False
                                return True
                    else:
                        # cancel after trying to move squares on grid
                        self.isActive = False
                        self.activeCell = None
                        return False
                
                elif(self.activeCell.type == "Pawn" and self.activeCell.color.value == playerIndex):
                    if(gameBoard.grid[self.position.x][self.position.y].type == "Square"):
                        if(self.activeCell.position is None):
                            # put unused pawn on square
                            yIndex = -1
                            for i in range(len(gameBoard.pawns[playerIndex])):
                                if(gameBoard.pawns[playerIndex][i].position == None):
                                    yIndex = i
                            gameBoard.move(Move(Position(playerIndex, yIndex), self.position, MoveType.PUT_UNUSED_PAWN_ON_SQUARE))
                            self.isActive = False
                            self.activeCell = None
                            gameBoard.previousActionWasDoubleSlide = False
                            return True
                        else:
                            # put used pawn on free square
                            gameBoard.move(Move(self.activeCell.position, self.position, MoveType.PUT_USED_PAWN_ON_SQUARE))
                            self.isActive = False
                            self.activeCell = None
                            gameBoard.previousActionWasDoubleSlide = False
                            return True
                    else:
                        # cancel try to put owned pawn on cell already containing a pawn
                        self.isActive = False
                        self.activeCell = None
                        return False
                else:
                    # cancel try to put enemy pawn somewhere on grid
                    self.isActive = False
                    self.activeCell = None
                    return False
                    
            else:
                # cancel selection when trying to put something outside grid
                self.isActive = False
                self.activeCell = None
                return False
        return False

    