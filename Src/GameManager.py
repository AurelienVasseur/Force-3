import pygame
from GameBoard import GameBoard
from Player import Player
from Window import Window
from Color import Color
from Direction import Direction
from StatusType import StatusType
from copy import deepcopy
from GameType import GameType
from ArtificialIntelligence import ArtificialIntelligence

class GameManager:
    def __init__(self, gameType = GameType.PLAYER_VS_PLAYER):
        self.gameBoard = GameBoard()
        self.players = [None for i in range(2)]
        self.gameType = gameType
        if(self.gameType == GameType.PLAYER_VS_PLAYER):
            self.players[Color.BLACK.value] = Player(Color.BLACK)
            self.players[Color.WHITE.value] = Player(Color.WHITE)
        elif(self.gameType == GameType.PLAYER_VS_AI):
            self.players[Color.BLACK.value] = Player(Color.BLACK)
            self.players[Color.WHITE.value] = ArtificialIntelligence(Color.WHITE)
        else:
            self.players[Color.BLACK.value] = ArtificialIntelligence(Color.BLACK)
            self.players[Color.WHITE.value] = ArtificialIntelligence(Color.WHITE)
        self.players[Color.BLACK.value].isTurnActive = True


    def getActivePlayer(self):
        if(self.players[Color.BLACK.value].isTurnActive):
            return self.players[Color.BLACK.value]
        return self.players[Color.WHITE.value]

    def switchActivePlayer(self):
        if(self.players[Color.BLACK.value].isTurnActive):
            self.players[Color.BLACK.value].isTurnActive = False
            self.players[Color.WHITE.value].isTurnActive = True
        else:
            self.players[Color.BLACK.value].isTurnActive = True
            self.players[Color.WHITE.value].isTurnActive = False

    def checkVictory(self):
        gameStatus = self.gameBoard.getGameStatus()
        if(gameStatus.status != StatusType.END):
            return False
        print("{} wins by {} pawns alignment.".format(gameStatus.winner, gameStatus.winType))
        return True

    def start(self):        
        # display grid in console
        """ 
        for i in range(len(self.gameBoard.grid)):
            for j in range(len(self.gameBoard.grid[i])):
                print("{},".format(str(self.gameBoard.grid[i][j])), end="")
            print()
        """
        
        pygame.init()
        window = pygame.display.set_mode((Window.WIDTH.value, Window.HEIGHT.value), pygame.RESIZABLE)

        background = pygame.image.load("resources/images/background.jpg").convert()
        background = pygame.transform.scale(background, (Window.WIDTH.value, Window.HEIGHT.value))
        # window.blit(background, (0, 0))

        gridImage = pygame.image.load("resources/images/grid.jpg")
        gridImage = pygame.transform.scale(gridImage, (Window.GRID_WIDTH.value, Window.GRID_HEIGHT.value))
        # window.blit(gridImage, (Window.GRID_POSITION_X.value, Window.GRID_POSITION_Y.value))

        squareImage = pygame.image.load("resources/images/square.jpg")
        squareImage = pygame.transform.scale(squareImage, (Window.PIECE_WIDTH.value, Window.PIECE_HEIGHT.value))

        pawnWhiteImage = pygame.image.load("resources/images/pawn_white.png")
        pawnWhiteImage = pygame.transform.scale(pawnWhiteImage, (Window.PIECE_WIDTH.value, Window.PIECE_HEIGHT.value))
        # window.blit(pawnWhite, (Window.PAWN_WHITE_START_POSITION_X.value, Window.PAWN_WHITE_START_POSITION_Y.value))

        pawnBlackImage = pygame.image.load("resources/images/pawn_black.png")
        pawnBlackImage = pygame.transform.scale(pawnBlackImage, (Window.PIECE_WIDTH.value, Window.PIECE_HEIGHT.value))
        # window.blit(pawnBlack, (Window.PAWN_BLACK_START_POSITION_X.value, Window.PAWN_BLACK_START_POSITION_Y.value))

        selectorWhiteImage = pygame.image.load("resources/images/selector_white.png")
        selectorWhiteImage = pygame.transform.scale(selectorWhiteImage, (Window.CELL_WIDTH.value, Window.CELL_HEIGHT.value))
        selectorWhiteActiveImage = pygame.image.load("resources/images/selector_white_active.png")
        selectorWhiteActiveImage = pygame.transform.scale(selectorWhiteActiveImage, (Window.CELL_WIDTH.value, Window.CELL_HEIGHT.value))
        selectorBlackImage = pygame.image.load("resources/images/selector_black.png")
        selectorBlackImage = pygame.transform.scale(selectorBlackImage, (Window.CELL_WIDTH.value, Window.CELL_HEIGHT.value))
        selectorBlackActiveImage = pygame.image.load("resources/images/selector_black_active.png")
        selectorBlackActiveImage = pygame.transform.scale(selectorBlackActiveImage, (Window.CELL_WIDTH.value, Window.CELL_HEIGHT.value))
        

        play = True
        while play:
            window.blit(background, (0,0))
            window.blit(gridImage, (Window.GRID_POSITION_X.value, Window.GRID_POSITION_Y.value))

            for event in pygame.event.get():
                if(event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                    play = False

                
                if(self.gameType == GameType.PLAYER_VS_PLAYER or (self.gameType == GameType.PLAYER_VS_AI and self.getActivePlayer().color == Color.BLACK)):
                    if(event.type == pygame.KEYDOWN):
                        if(event.key == pygame.K_RETURN):
                            actionComplete = self.getActivePlayer().selector.toggleSelect(self.gameBoard, self.getActivePlayer().color.value)
                            if(actionComplete):
                                self.switchActivePlayer()
                                play = not self.checkVictory()
                        if(event.key == pygame.K_UP or event.key == pygame.K_w):
                            self.getActivePlayer().selector.move(Direction.UP)
                        if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                            self.getActivePlayer().selector.move(Direction.DOWN)
                        if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                            self.getActivePlayer().selector.move(Direction.LEFT)
                        if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                            self.getActivePlayer().selector.move(Direction.RIGHT)
                else:
                    self.getActivePlayer().playBestMove(self.gameBoard, self.players)
                    self.switchActivePlayer()
                    play = not self.checkVictory()


            for i in range(len(self.gameBoard.grid)):
                for j in range(len(self.gameBoard.grid[i])):
                    cell = self.gameBoard.grid[i][j]
                    if(cell.type == "Square"):
                        square = cell
                        squarePositionX = Window.GRID_POSITION_X.value + Window.GRID_OFFSET_X.value + Window.PIECE_OFFSET_X.value + square.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
                        squarePositionY = Window.GRID_POSITION_Y.value + Window.GRID_OFFSET_Y.value + Window.PIECE_OFFSET_Y.value + square.position.x * (Window.CELL_HEIGHT.value + Window.GRID_INNER_OFFSET_Y.value)
                        window.blit(squareImage, (squarePositionX, squarePositionY))
                    elif(cell.type == "Pawn"):
                        pawn = cell
                        pawnPositionX = Window.GRID_POSITION_X.value + Window.GRID_OFFSET_X.value + Window.PIECE_OFFSET_X.value + pawn.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
                        pawnPositionY = Window.GRID_POSITION_Y.value + Window.GRID_OFFSET_Y.value + Window.PIECE_OFFSET_Y.value + pawn.position.x * (Window.CELL_HEIGHT.value + Window.GRID_INNER_OFFSET_Y.value)
                        if(pawn.color == Color.BLACK):
                            window.blit(squareImage, (pawnPositionX, pawnPositionY))
                            window.blit(pawnBlackImage, (pawnPositionX, pawnPositionY))
                        else:
                            window.blit(squareImage, (pawnPositionX, pawnPositionY))
                            window.blit(pawnWhiteImage, (pawnPositionX, pawnPositionY))
            
            for j in range(len(self.gameBoard.pawns[0])):
                pawnBlack = self.gameBoard.pawns[0][j]
                pawnWhite = self.gameBoard.pawns[1][j]
                if(pawnBlack.position == None):
                    window.blit(pawnBlackImage, (Window.PAWN_BLACK_START_POSITION_X.value + j * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value), Window.PAWN_BLACK_START_POSITION_Y.value))
                if(pawnWhite.position == None):
                    window.blit(pawnWhiteImage, (Window.PAWN_WHITE_START_POSITION_X.value + j * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value), Window.PAWN_WHITE_START_POSITION_Y.value))

            selectorBlackPositionX = None
            selectorBlackPositionY = None
            if(self.players[0].selector.position.x != self.players[0].selector.maxLine):
                selectorBlackPositionX = Window.GRID_POSITION_X.value + Window.GRID_OFFSET_X.value + self.players[0].selector.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
                selectorBlackPositionY = Window.GRID_POSITION_Y.value + Window.GRID_OFFSET_Y.value + self.players[0].selector.position.x * (Window.CELL_HEIGHT.value + Window.GRID_INNER_OFFSET_Y.value)
            else:
                selectorBlackPositionX = Window.PAWN_BLACK_START_POSITION_X.value - Window.PIECE_OFFSET_X.value + self.players[0].selector.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
                selectorBlackPositionY = Window.PAWN_BLACK_START_POSITION_Y.value - Window.PIECE_OFFSET_Y.value
            
            if(self.players[Color.BLACK.value].selector.isActive):
                window.blit(selectorBlackActiveImage, (selectorBlackPositionX, selectorBlackPositionY))
            else:
                window.blit(selectorBlackImage, (selectorBlackPositionX, selectorBlackPositionY))

            selectorWhitePositionX = None
            selectorWhitePositionY = None
            if(self.players[1].selector.position.x != self.players[1].selector.minLine):
                selectorWhitePositionX = Window.GRID_POSITION_X.value + Window.GRID_OFFSET_X.value + self.players[1].selector.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
                selectorWhitePositionY = Window.GRID_POSITION_Y.value + Window.GRID_OFFSET_Y.value + self.players[1].selector.position.x * (Window.CELL_HEIGHT.value + Window.GRID_INNER_OFFSET_Y.value)
            else:
                selectorWhitePositionX = Window.PAWN_WHITE_START_POSITION_X.value - Window.PIECE_OFFSET_X.value + self.players[1].selector.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
                selectorWhitePositionY = Window.PAWN_WHITE_START_POSITION_Y.value - Window.PIECE_OFFSET_Y.value
            if(self.players[Color.WHITE.value].selector.isActive):
                window.blit(selectorWhiteActiveImage, (selectorWhitePositionX, selectorWhitePositionY))
            else:
                window.blit(selectorWhiteImage, (selectorWhitePositionX, selectorWhitePositionY))
            
            
            
            
            pygame.display.flip()
        pygame.quit()
        return



GameManager(GameType.PLAYER_VS_AI).start()
