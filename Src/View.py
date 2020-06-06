import pygame
from .Window import Window

class View:

    def __init__(self):
        pygame.init()
        pygame.display.set_caption('Force3')

        self.window = pygame.display.set_mode((Window.WIDTH.value, Window.HEIGHT.value), pygame.RESIZABLE)

        self.background = pygame.image.load("resources/images/background.jpg").convert()
        self.background = pygame.transform.scale(self.background, (Window.WIDTH.value, Window.HEIGHT.value))
        

        self.gridImage = pygame.image.load("resources/images/grid.jpg")
        self.gridImage = pygame.transform.scale(self.gridImage, (Window.GRID_WIDTH.value, Window.GRID_HEIGHT.value))
        

        self.squareImage = pygame.image.load("resources/images/square.jpg")
        self.squareImage = pygame.transform.scale(self.squareImage, (Window.PIECE_WIDTH.value, Window.PIECE_HEIGHT.value))

        self.pawnWhiteImage = pygame.image.load("resources/images/pawn_white.png")
        self.pawnWhiteImage = pygame.transform.scale(self.pawnWhiteImage, (Window.PIECE_WIDTH.value, Window.PIECE_HEIGHT.value))
        

        self.pawnBlackImage = pygame.image.load("resources/images/pawn_black.png")
        self.pawnBlackImage = pygame.transform.scale(self.pawnBlackImage, (Window.PIECE_WIDTH.value, Window.PIECE_HEIGHT.value))
        

        self.selectorWhiteImage = pygame.image.load("resources/images/selector_white.png")
        self.selectorWhiteImage = pygame.transform.scale(self.selectorWhiteImage, (Window.CELL_WIDTH.value, Window.CELL_HEIGHT.value))
        self.selectorWhiteActiveImage = pygame.image.load("resources/images/selector_white_active.png")
        self.selectorWhiteActiveImage = pygame.transform.scale(self.selectorWhiteActiveImage, (Window.CELL_WIDTH.value, Window.CELL_HEIGHT.value))
        self.selectorBlackImage = pygame.image.load("resources/images/selector_black.png")
        self.selectorBlackImage = pygame.transform.scale(self.selectorBlackImage, (Window.CELL_WIDTH.value, Window.CELL_HEIGHT.value))
        self.selectorBlackActiveImage = pygame.image.load("resources/images/selector_black_active.png")
        self.selectorBlackActiveImage = pygame.transform.scale(self.selectorBlackActiveImage, (Window.CELL_WIDTH.value, Window.CELL_HEIGHT.value))

        self.startMenuPVP = pygame.image.load("resources/images/startmenu_pvp.png")
        self.startMenuPVP = pygame.transform.scale(self.startMenuPVP, (Window.BUTTON_WIDTH.value, Window.BUTTON_HEIGHT.value))
        self.startMenuPVPHover = pygame.image.load("resources/images/startmenu_pvp_hover.png")
        self.startMenuPVPHover = pygame.transform.scale(self.startMenuPVPHover, (Window.BUTTON_WIDTH.value, Window.BUTTON_HEIGHT.value))
        self.startMenuAIVP = pygame.image.load("resources/images/startmenu_aivp.png")
        self.startMenuAIVP = pygame.transform.scale(self.startMenuAIVP, (Window.BUTTON_WIDTH.value, Window.BUTTON_HEIGHT.value))
        self.startMenuAIVPHover = pygame.image.load("resources/images/startmenu_aivp_hover.png")
        self.startMenuAIVPHover = pygame.transform.scale(self.startMenuAIVPHover, (Window.BUTTON_WIDTH.value, Window.BUTTON_HEIGHT.value))
        self.startMenuAIVAI = pygame.image.load("resources/images/startmenu_aivai.png")
        self.startMenuAIVAI = pygame.transform.scale(self.startMenuAIVAI, (Window.BUTTON_WIDTH.value, Window.BUTTON_HEIGHT.value))
        self.startMenuAIVAIHover = pygame.image.load("resources/images/startmenu_aivai_hover.png")
        self.startMenuAIVAIHover = pygame.transform.scale(self.startMenuAIVAIHover, (Window.BUTTON_WIDTH.value, Window.BUTTON_HEIGHT.value))

        self.endMenuNewGame = pygame.image.load("resources/images/endmenu_newgame.png")
        self.endMenuNewGame = pygame.transform.scale(self.endMenuNewGame, (Window.BUTTON_WIDTH.value, Window.BUTTON_HEIGHT.value))
        self.endMenuNewGameHover = pygame.image.load("resources/images/endmenu_newgame_hover.png")
        self.endMenuNewGameHover = pygame.transform.scale(self.endMenuNewGameHover, (Window.BUTTON_WIDTH.value, Window.BUTTON_HEIGHT.value))
        self.endMenuQuit = pygame.image.load("resources/images/endmenu_quit.png")
        self.endMenuQuit = pygame.transform.scale(self.endMenuQuit, (Window.BUTTON_WIDTH.value, Window.BUTTON_HEIGHT.value))
        self.endMenuQuitHover = pygame.image.load("resources/images/endmenu_quit_hover.png")
        self.endMenuQuitHover = pygame.transform.scale(self.endMenuQuitHover, (Window.BUTTON_WIDTH.value, Window.BUTTON_HEIGHT.value))

    def blitBackground(self):
        self.window.blit(self.background, (0, 0))

    def blitGrid(self):
        self.window.blit(self.gridImage, (Window.GRID_POSITION_X.value, Window.GRID_POSITION_Y.value))

    def blitSquare(self, x, y):
        self.window.blit(self.squareImage, (x, y))

    def blitPawnBlack(self, x, y):
        self.window.blit(self.pawnBlackImage, (x, y))
    def blitPawnWhite(self, x, y):
        self.window.blit(self.pawnWhiteImage, (x, y))

    def blitSelectorBlack(self, x, y):
        self.window.blit(self.selectorBlackImage, (x, y))
    def blitSelectorBlackActive(self, x, y):
        self.window.blit(self.selectorBlackActiveImage, (x, y))
    def blitSelectorWhite(self, x, y):
        self.window.blit(self.selectorWhiteImage, (x, y))
    def blitSelectorWhiteActive(self, x, y):
        self.window.blit(self.selectorWhiteActiveImage, (x, y))
    
    def blitStartMenuPVP(self, x, y):
        self.window.blit(self.startMenuPVP, (x, y))
    def blitStartMenuAIVP(self, x, y):
        self.window.blit(self.startMenuAIVP, (x, y))
    def blitStartMenuAIVAI(self, x, y):
        self.window.blit(self.startMenuAIVAI, (x, y))
    def blitEndMenuNewGame(self, x, y):
        self.window.blit(self.endMenuNewGame, (x, y))
    def blitEndMenuQuit(self, x, y):
        self.window.blit(self.endMenuQuit, (x, y))
    def blitStartMenuPVPHover(self, x, y):
        self.window.blit(self.startMenuPVPHover, (x, y))
    def blitStartMenuAIVPHover(self, x, y):
        self.window.blit(self.startMenuAIVPHover, (x, y))
    def blitStartMenuAIVAIHover(self, x, y):
        self.window.blit(self.startMenuAIVAIHover, (x, y))
    def blitEndMenuNewGameHover(self, x, y):
        self.window.blit(self.endMenuNewGameHover, (x, y))
    def blitEndMenuQuitHover(self, x, y):
        self.window.blit(self.endMenuQuitHover, (x, y))

    def blitStartMenu(self):
        mouseX, mouseY = self.getMousePos()
        self.blitBackground()
        self.blitStartMenuPVP(Window.STARTMENU_PVP_POSITION_X.value, Window.STARTMENU_PVP_POSITION_Y.value)
        self.blitStartMenuAIVP(Window.STARTMENU_AIVP_POSITION_X.value, Window.STARTMENU_AIVP_POSITION_Y.value)
        self.blitStartMenuAIVAI(Window.STARTMENU_AIVAI_POSITION_X.value, Window.STARTMENU_AIVAI_POSITION_Y.value)
        if(mouseX >= Window.STARTMENU_PVP_POSITION_X.value and mouseX <= (Window.STARTMENU_PVP_POSITION_X.value + Window.BUTTON_WIDTH.value) and mouseY >= Window.STARTMENU_PVP_POSITION_Y.value and mouseY <= (Window.STARTMENU_PVP_POSITION_Y.value + Window.BUTTON_HEIGHT.value)):
            # PVP button hover
            self.blitStartMenuPVPHover(Window.STARTMENU_PVP_POSITION_X.value, Window.STARTMENU_PVP_POSITION_Y.value)
        elif(mouseX >= Window.STARTMENU_AIVP_POSITION_X.value and mouseX <= (Window.STARTMENU_AIVP_POSITION_X.value + Window.BUTTON_WIDTH.value) and mouseY >= Window.STARTMENU_AIVP_POSITION_Y.value and mouseY <= (Window.STARTMENU_AIVP_POSITION_Y.value + Window.BUTTON_HEIGHT.value)):
            # AIVP button hover
            self.blitStartMenuAIVPHover(Window.STARTMENU_AIVP_POSITION_X.value, Window.STARTMENU_AIVP_POSITION_Y.value)
        elif(mouseX >= Window.STARTMENU_AIVAI_POSITION_X.value and mouseX <= (Window.STARTMENU_AIVAI_POSITION_X.value + Window.BUTTON_WIDTH.value) and mouseY >= Window.STARTMENU_AIVAI_POSITION_Y.value and mouseY <= (Window.STARTMENU_AIVAI_POSITION_Y.value + Window.BUTTON_HEIGHT.value)):
            # AIVP button hover
            self.blitStartMenuAIVAIHover(Window.STARTMENU_AIVAI_POSITION_X.value, Window.STARTMENU_AIVAI_POSITION_Y.value)
        self.display()

    def blitEndMenu(self):
        mouseX, mouseY = self.getMousePos()
        self.blitBackground()
        self.blitEndMenuNewGame(Window.ENDMENU_NEWGAME_POSITION_X.value, Window.ENDMENU_NEWGAME_POSITION_Y.value)
        self.blitEndMenuQuit(Window.ENDMENU_QUIT_POSITION_X.value, Window.ENDMENU_QUIT_POSITION_Y.value)
        if(mouseX >= Window.ENDMENU_NEWGAME_POSITION_X.value and mouseX <= (Window.ENDMENU_NEWGAME_POSITION_X.value + Window.BUTTON_WIDTH.value) and mouseY >= Window.ENDMENU_NEWGAME_POSITION_Y.value and mouseY <= (Window.ENDMENU_NEWGAME_POSITION_Y.value + Window.BUTTON_HEIGHT.value)):
            # NewGame button hover
            self.blitEndMenuNewGameHover(Window.ENDMENU_NEWGAME_POSITION_X.value, Window.ENDMENU_NEWGAME_POSITION_Y.value)
        elif(mouseX >= Window.ENDMENU_QUIT_POSITION_X.value and mouseX <= (Window.ENDMENU_QUIT_POSITION_X.value + Window.BUTTON_WIDTH.value) and mouseY >= Window.ENDMENU_QUIT_POSITION_Y.value and mouseY <= (Window.ENDMENU_QUIT_POSITION_Y.value + Window.BUTTON_HEIGHT.value)):
            # Quit button hover
            self.blitEndMenuQuitHover(Window.ENDMENU_QUIT_POSITION_X.value, Window.ENDMENU_QUIT_POSITION_Y.value)
        self.display()

    def getMousePos(self):
        return pygame.mouse.get_pos()

    def display(self):
        pygame.display.flip()
        
    def quit(self):
        pygame.quit()
