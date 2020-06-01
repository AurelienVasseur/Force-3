import pygame
from Window import Window

class View:

    def __init__(self):
        pygame.init()

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

    def display(self):
        pygame.display.flip()
        
    def quit(self):
        pygame.quit()
