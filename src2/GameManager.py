import pygame
from .GameBoard import GameBoard
from .Player import Player
from .Window import Window
from .Color import Color
from .Direction import Direction
from .StatusType import StatusType
from .GameType import GameType
from .ArtificialIntelligence import ArtificialIntelligence
import time
from .View import View
from .Config import Config
import sys


class GameManager:
    def __init__(self):
        self.gameBoard = None
        self.players = [None for i in range(2)]
        self.gameType = None
        self.view = View()
        self.timeLastAIAction = time.time()

    def init(self, gameType):
        self.gameBoard = GameBoard()
        self.gameType = gameType
        if(self.gameType == GameType.PLAYER_VS_PLAYER):
            self.players[Color.BLACK.value] = Player(Color.BLACK, True)
            self.players[Color.WHITE.value] = Player(Color.WHITE, False)
        elif(self.gameType == GameType.PLAYER_VS_AI):
            self.players[Color.BLACK.value] = Player(Color.BLACK, False)
            self.players[Color.WHITE.value] = ArtificialIntelligence(Color.WHITE, True, None, Config.RESEARCH_DEPTH_PLAYER_VS_AI.value)
        else:
            self.players[Color.BLACK.value] = ArtificialIntelligence(Color.BLACK, True, None, Config.RESEARCH_DEPTH_AI_VS_AI.value)
            self.players[Color.WHITE.value] = ArtificialIntelligence(Color.WHITE, False, None, Config.RESEARCH_DEPTH_AI_VS_AI.value)


    def start(self):
        play = True
        while play:
            choice = self.showStartMenu()
            self.init(choice)
            self.showGame()
            quitGame = self.showEndMenu()
            if(quitGame):
                play = False
        self.view.quit()



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


    def showStartMenu(self):
        startMenu = True
        while startMenu:
            self.view.blitStartMenu()
            choice = self.handleStartMenuChoice()
            if(choice is not None):
                startMenu = False
        return choice

    def showGame(self):
        play = True
        while play:
            self.view.blitBackground()
            self.view.blitGrid()

            play = self.handleAI()
            if(play):
                play = self.handleUserControls()
                

            self.updateGUI()
            self.view.display()
    
    def showEndMenu(self):
        endMenu = True
        quitGame = None
        while endMenu:
            self.view.blitEndMenu()
            quitGame = self.handleEndMenuChoice()
            if(quitGame is not None):
                endMenu = False
        return quitGame


    def handleAI(self):
        if(self.gameType == GameType.AI_VS_AI or (self.gameType == GameType.PLAYER_VS_AI and self.getActivePlayer().color == Color.WHITE)):
            if(time.time() - self.timeLastAIAction > Config.AI_PAUSE_TIME.value):
                self.getActivePlayer().playBestMove(self.gameBoard, self.players)
                self.switchActivePlayer()
                self.timeLastAIAction = time.time()
                if(self.checkVictory()):
                    return False
        return True

    def handleStartMenuChoice(self):
        mouseX, mouseY = self.view.getMousePos()
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                self.view.quit()
                sys.exit()
            
            if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                if(mouseX >= Window.STARTMENU_PVP_POSITION_X.value and mouseX <= (Window.STARTMENU_PVP_POSITION_X.value + Window.BUTTON_WIDTH.value) and mouseY >= Window.STARTMENU_PVP_POSITION_Y.value and mouseY <= (Window.STARTMENU_PVP_POSITION_Y.value + Window.BUTTON_HEIGHT.value)):
                    # PVP button click
                    return GameType.PLAYER_VS_PLAYER
                elif(mouseX >= Window.STARTMENU_AIVP_POSITION_X.value and mouseX <= (Window.STARTMENU_AIVP_POSITION_X.value + Window.BUTTON_WIDTH.value) and mouseY >= Window.STARTMENU_AIVP_POSITION_Y.value and mouseY <= (Window.STARTMENU_AIVP_POSITION_Y.value + Window.BUTTON_HEIGHT.value)):
                    # AIVP button click
                    return GameType.PLAYER_VS_AI
                elif(mouseX >= Window.STARTMENU_AIVAI_POSITION_X.value and mouseX <= (Window.STARTMENU_AIVAI_POSITION_X.value + Window.BUTTON_WIDTH.value) and mouseY >= Window.STARTMENU_AIVAI_POSITION_Y.value and mouseY <= (Window.STARTMENU_AIVAI_POSITION_Y.value + Window.BUTTON_HEIGHT.value)):
                    # AIVP button click
                    return GameType.AI_VS_AI

    def handleEndMenuChoice(self):
        mouseX, mouseY = self.view.getMousePos()
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                self.view.quit()
                sys.exit()

            if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
                if(mouseX >= Window.ENDMENU_NEWGAME_POSITION_X.value and mouseX <= (Window.ENDMENU_NEWGAME_POSITION_X.value + Window.BUTTON_WIDTH.value) and mouseY >= Window.ENDMENU_NEWGAME_POSITION_Y.value and mouseY <= (Window.ENDMENU_NEWGAME_POSITION_Y.value + Window.BUTTON_HEIGHT.value)):
                    return False
                if(mouseX >= Window.ENDMENU_QUIT_POSITION_X.value and mouseX <= (Window.ENDMENU_QUIT_POSITION_X.value + Window.BUTTON_WIDTH.value) and mouseY >= Window.ENDMENU_QUIT_POSITION_Y.value and mouseY <= (Window.ENDMENU_QUIT_POSITION_Y.value + Window.BUTTON_HEIGHT.value)):
                    return True

    def handleUserControls(self):
        for event in pygame.event.get():
            if(event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE)):
                self.view.quit()
                sys.exit()

            if(self.gameType == GameType.PLAYER_VS_PLAYER or (self.gameType == GameType.PLAYER_VS_AI and self.getActivePlayer().color == Color.BLACK)):
                if(event.type == pygame.KEYDOWN):
                    if(event.key == pygame.K_RETURN):
                        actionComplete = self.getActivePlayer().selector.toggleSelect(self.gameBoard, self.getActivePlayer().color.value)
                        if(actionComplete):
                            self.switchActivePlayer()
                            return not self.checkVictory()
                    if(event.key == pygame.K_UP or event.key == pygame.K_w):
                        self.getActivePlayer().selector.move(Direction.UP)
                    if(event.key == pygame.K_DOWN or event.key == pygame.K_s):
                        self.getActivePlayer().selector.move(Direction.DOWN)
                    if(event.key == pygame.K_LEFT or event.key == pygame.K_a):
                        self.getActivePlayer().selector.move(Direction.LEFT)
                    if(event.key == pygame.K_RIGHT or event.key == pygame.K_d):
                        self.getActivePlayer().selector.move(Direction.RIGHT)
        return True

    def updateGUI(self):
        self.GuiUpdateGridCells()
        self.GuiUpdateHands()
        self.GuiUpdateSelectors()
        
        

        

    def GuiUpdateGridCells(self):
        for i in range(len(self.gameBoard.grid)):
            for j in range(len(self.gameBoard.grid[i])):
                cell = self.gameBoard.grid[i][j]
                if(cell.type == "Square"):
                    square = cell
                    squarePositionX = Window.GRID_POSITION_X.value + Window.GRID_OFFSET_X.value + Window.PIECE_OFFSET_X.value + square.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
                    squarePositionY = Window.GRID_POSITION_Y.value + Window.GRID_OFFSET_Y.value + Window.PIECE_OFFSET_Y.value + square.position.x * (Window.CELL_HEIGHT.value + Window.GRID_INNER_OFFSET_Y.value)
                    self.view.blitSquare(squarePositionX, squarePositionY)
                elif(cell.type == "Pawn"):
                    pawn = cell
                    pawnPositionX = Window.GRID_POSITION_X.value + Window.GRID_OFFSET_X.value + Window.PIECE_OFFSET_X.value + pawn.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
                    pawnPositionY = Window.GRID_POSITION_Y.value + Window.GRID_OFFSET_Y.value + Window.PIECE_OFFSET_Y.value + pawn.position.x * (Window.CELL_HEIGHT.value + Window.GRID_INNER_OFFSET_Y.value)
                    if(pawn.color == Color.BLACK):
                        self.view.blitSquare(pawnPositionX, pawnPositionY)
                        self.view.blitPawnBlack(pawnPositionX, pawnPositionY)
                    else:
                        self.view.blitSquare(pawnPositionX, pawnPositionY)
                        self.view.blitPawnWhite(pawnPositionX, pawnPositionY)

    def GuiUpdateHands(self):
        for j in range(len(self.gameBoard.pawns[0])):
            pawnBlack = self.gameBoard.pawns[0][j]
            pawnWhite = self.gameBoard.pawns[1][j]
            if(pawnBlack.position == None):
                self.view.blitPawnBlack(Window.PAWN_BLACK_START_POSITION_X.value + j * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value), Window.PAWN_BLACK_START_POSITION_Y.value)
            if(pawnWhite.position == None):
                self.view.blitPawnWhite(Window.PAWN_WHITE_START_POSITION_X.value + j * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value), Window.PAWN_WHITE_START_POSITION_Y.value)
    
    
    def GuiUpdateSelectors(self):
        if(self.gameType != GameType.AI_VS_AI):
            self.GuiUpdateSelectorBlack()

        if(self.gameType == GameType.PLAYER_VS_PLAYER):
            self.GuiUpdateSelectorWhite()

    def GuiUpdateSelectorBlack(self):
        selectorBlackPositionX = None
        selectorBlackPositionY = None
        if(self.players[0].selector.position.x != self.players[0].selector.maxLine):
            selectorBlackPositionX = Window.GRID_POSITION_X.value + Window.GRID_OFFSET_X.value + self.players[0].selector.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
            selectorBlackPositionY = Window.GRID_POSITION_Y.value + Window.GRID_OFFSET_Y.value + self.players[0].selector.position.x * (Window.CELL_HEIGHT.value + Window.GRID_INNER_OFFSET_Y.value)
        else:
            selectorBlackPositionX = Window.PAWN_BLACK_START_POSITION_X.value - Window.PIECE_OFFSET_X.value + self.players[0].selector.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
            selectorBlackPositionY = Window.PAWN_BLACK_START_POSITION_Y.value - Window.PIECE_OFFSET_Y.value
        
        if(self.players[Color.BLACK.value].selector.isActive):
            self.view.blitSelectorBlackActive(selectorBlackPositionX, selectorBlackPositionY)
        else:
            self.view.blitSelectorBlack(selectorBlackPositionX, selectorBlackPositionY)
    def GuiUpdateSelectorWhite(self):
        selectorWhitePositionX = None
        selectorWhitePositionY = None
        if(self.players[1].selector.position.x != self.players[1].selector.minLine):
            selectorWhitePositionX = Window.GRID_POSITION_X.value + Window.GRID_OFFSET_X.value + self.players[1].selector.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
            selectorWhitePositionY = Window.GRID_POSITION_Y.value + Window.GRID_OFFSET_Y.value + self.players[1].selector.position.x * (Window.CELL_HEIGHT.value + Window.GRID_INNER_OFFSET_Y.value)
        else:
            selectorWhitePositionX = Window.PAWN_WHITE_START_POSITION_X.value - Window.PIECE_OFFSET_X.value + self.players[1].selector.position.y * (Window.CELL_WIDTH.value + Window.GRID_INNER_OFFSET_X.value)
            selectorWhitePositionY = Window.PAWN_WHITE_START_POSITION_Y.value - Window.PIECE_OFFSET_Y.value
        if(self.players[Color.WHITE.value].selector.isActive):
            self.view.blitSelectorWhiteActive(selectorWhitePositionX, selectorWhitePositionY)
        else:
            self.view.blitSelectorWhite(selectorWhitePositionX, selectorWhitePositionY)




