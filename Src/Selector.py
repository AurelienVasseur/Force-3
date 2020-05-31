from Position import Position
from Direction import Direction
from Square import Square
from Cell import Cell

class Selector:

    def __init__(self, position: Position, minLine, maxLine):
        self.position = position
        self.minLine = minLine
        self.maxLine = maxLine
        self.isActive = False
        self.activeCell = None

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

    def toggleSelect(self, gameBoard, playerIndex):
        if(not self.isActive):
            # print("Pressed Enter while inactive")
            if(self.isInGrid()):
                cell = gameBoard.grid[self.position.x][self.position.y]
                if(cell.type == "Square" or cell.type == "Pawn"):
                    # print("Selected Square or owned Pawn in grid")
                    self.isActive = True
                    self.activeCell = gameBoard.grid[self.position.x][self.position.y]
            elif(gameBoard.pawns[playerIndex][self.position.y].position is None):
                # print("Selected unused Pawn")
                self.isActive = True
                self.activeCell = gameBoard.pawns[playerIndex][self.position.y]
        else:
            # print("Pressed Enter while active")
            if(self.isInGrid()):
                if(gameBoard.grid[self.position.x][self.position.y].type == "Cell" and self.activeCell.position != None):
                    if(self.position.x == self.activeCell.position.x):
                        # move cells on same line to current Cell
                        if(self.position.y > self.activeCell.position.y):
                            # move to right
                            if(self.position.y - self.activeCell.position.y > 1):
                                # move 2 to right
                                activeCellOriginalPosition = Position(self.activeCell.position.x, self.activeCell.position.y)
                                gameBoard.grid[self.position.x][self.position.y] = gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y + 1]
                                gameBoard.grid[self.position.x][self.position.y].position = Position(self.position.x, self.position.y)
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y + 1] = gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y]
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y + 1].position = Position(activeCellOriginalPosition.x, activeCellOriginalPosition.y + 1)
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y] = Cell(Position(activeCellOriginalPosition.x, activeCellOriginalPosition.y))
                                self.isActive = False
                                self.activeCell = None
                                return True
                            else:
                                # move 1 to right
                                activeCellOriginalPosition = Position(self.activeCell.position.x, self.activeCell.position.y)
                                gameBoard.grid[self.position.x][self.position.y] = gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y]
                                gameBoard.grid[self.position.x][self.position.y].position = Position(self.position.x, self.position.y)
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y] = Cell(Position(activeCellOriginalPosition.x, activeCellOriginalPosition.y))
                                self.isActive = False
                                self.activeCell = None
                                return True
                        else:
                            # move to left
                            if(self.activeCell.position.y - self.position.y > 1):
                                # move 2 to left
                                activeCellOriginalPosition = Position(self.activeCell.position.x, self.activeCell.position.y)
                                gameBoard.grid[self.position.x][self.position.y] = gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y - 1]
                                gameBoard.grid[self.position.x][self.position.y].position = Position(self.position.x, self.position.y)
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y - 1] = gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y]
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y - 1].position = Position(activeCellOriginalPosition.x, activeCellOriginalPosition.y - 1)
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y] = Cell(Position(activeCellOriginalPosition.x, activeCellOriginalPosition.y))
                                self.isActive = False
                                self.activeCell = None
                                return True
                            else:
                                # move 1 to left
                                activeCellOriginalPosition = Position(self.activeCell.position.x, self.activeCell.position.y)
                                gameBoard.grid[self.position.x][self.position.y] = gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y]
                                gameBoard.grid[self.position.x][self.position.y].position = Position(self.position.x, self.position.y)
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y] = Cell(Position(activeCellOriginalPosition.x, activeCellOriginalPosition.y))
                                self.isActive = False
                                self.activeCell = None
                                return True
                    elif(self.position.y == self.activeCell.position.y):
                        # move cells on same column to current Cell
                        if(self.position.x > self.activeCell.position.x):
                            # move down
                            if(self.position.x - self.activeCell.position.x > 1):
                                # move 2 down
                                activeCellOriginalPosition = Position(self.activeCell.position.x, self.activeCell.position.y)
                                gameBoard.grid[self.position.x][self.position.y] = gameBoard.grid[activeCellOriginalPosition.x + 1][activeCellOriginalPosition.y]
                                gameBoard.grid[self.position.x][self.position.y].position = Position(self.position.x, self.position.y)
                                gameBoard.grid[activeCellOriginalPosition.x + 1][activeCellOriginalPosition.y] = gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y]
                                gameBoard.grid[activeCellOriginalPosition.x + 1][activeCellOriginalPosition.y].position = Position(activeCellOriginalPosition.x + 1, activeCellOriginalPosition.y)
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y] = Cell(Position(activeCellOriginalPosition.x, activeCellOriginalPosition.y))
                                self.isActive = False
                                self.activeCell = None
                                return True
                            else:
                                # move 1 down
                                activeCellOriginalPosition = Position(self.activeCell.position.x, self.activeCell.position.y)
                                gameBoard.grid[self.position.x][self.position.y] = gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y]
                                gameBoard.grid[self.position.x][self.position.y].position = Position(self.position.x, self.position.y)
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y] = Cell(Position(activeCellOriginalPosition.x, activeCellOriginalPosition.y))
                                self.isActive = False
                                self.activeCell = None
                                return True
                        else:
                            # move up
                            if(self.activeCell.position.x - self.position.x > 1):
                                # move 2 up
                                activeCellOriginalPosition = Position(self.activeCell.position.x, self.activeCell.position.y)
                                gameBoard.grid[self.position.x][self.position.y] = gameBoard.grid[activeCellOriginalPosition.x - 1][activeCellOriginalPosition.y]
                                gameBoard.grid[self.position.x][self.position.y].position = Position(self.position.x, self.position.y)
                                gameBoard.grid[activeCellOriginalPosition.x - 1][activeCellOriginalPosition.y] = gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y]
                                gameBoard.grid[activeCellOriginalPosition.x - 1][activeCellOriginalPosition.y].position = Position(activeCellOriginalPosition.x - 1, activeCellOriginalPosition.y)
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y] = Cell(Position(activeCellOriginalPosition.x, activeCellOriginalPosition.y))
                                self.isActive = False
                                self.activeCell = None
                                return True
                            else:
                                # move 1 up
                                activeCellOriginalPosition = Position(self.activeCell.position.x, self.activeCell.position.y)
                                gameBoard.grid[self.position.x][self.position.y] = gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y]
                                gameBoard.grid[self.position.x][self.position.y].position = Position(self.position.x, self.position.y)
                                gameBoard.grid[activeCellOriginalPosition.x][activeCellOriginalPosition.y] = Cell(Position(activeCellOriginalPosition.x, activeCellOriginalPosition.y))
                                self.isActive = False
                                self.activeCell = None
                                return True
                    else:
                        # cancel after trying to move squares on grid
                        self.isActive = False
                        self.activeCell = None
                
                elif(self.activeCell.type == "Pawn" and self.activeCell.color.value == playerIndex):
                    if(gameBoard.grid[self.position.x][self.position.y].type == "Square"):
                        if(self.activeCell.position is None):
                            # put unused pawn on square
                            self.activeCell.position = Position(self.position.x, self.position.y)
                            gameBoard.grid[self.position.x][self.position.y] = self.activeCell
                            self.isActive = False
                            self.activeCell = None
                            return True
                        else:
                            # put used pawn on free square
                            gameBoard.grid[self.activeCell.position.x][self.activeCell.position.y] = Square(Position(self.activeCell.position.x, self.activeCell.position.y))
                            self.activeCell.position = Position(self.position.x, self.position.y)
                            gameBoard.grid[self.position.x][self.position.y] = self.activeCell
                            self.isActive = False
                            self.activeCell = None
                            return True
                    else:
                        # cancel try to put owned pawn on cell already containing a pawn
                        self.isActive = False
                        self.activeCell = None
                else:
                    # cancel try to put enemy pawn somewhere on grid
                    self.isActive = False
                    self.activeCell = None
                    
            else:
                # cancel selection when trying to put something outside grid
                self.isActive = False
                self.activeCell = None
        return False

    