from CoordinatesPrintGraphic import CoordinatesPrintGraphic
from Image import Image
import pygame
from Movement import Movement


class Selector:
    def __init__(self, _limit, _image, _coordinatesPrintGraphic):
        self.position = [None, None]
        self.inPawn = False
        self.active = False
        self.limit = _limit  # List = [Xmin, Xmax, Ymin, Ymax]
        self.image = pygame.image.load(_image.value[0])
        self.imageRezise = pygame.transform.scale(self.image, _image.value[1])
        self.positionImage = self.imageRezise.get_rect()
        self.coordinatesPrintGraphic = _coordinatesPrintGraphic

    def movementSelector(self, _movement):
        if _movement == Movement.RIGHT:
            x = self.position[0]
            y = self.position[1]
            if self.checkPossibilitiesMovementSelector(_movement):
                self.position = [x+1, y]
                self.positionImage[0] = self.coordinatesPrintGraphic.value[x+1, y][0]
                self.positionImage[1] = self.coordinatesPrintGraphic.value[x+1, y][1]

        if _movement == Movement.LEFT:
            x = self.position[0]
            y = self.position[1]
            if self.checkPossibilitiesMovementSelector(_movement):
                self.position = [x-1, y]
                self.positionImage[0] = self.coordinatesPrintGraphic.value[x-1, y][0]
                self.positionImage[1] = self.coordinatesPrintGraphic.value[x-1, y][1]

        if _movement == Movement.UP:
            x = self.position[0]
            y = self.position[1]
            if self.checkPossibilitiesMovementSelector(_movement):
                self.position = [x, y-1]
                self.positionImage[0] = self.coordinatesPrintGraphic.value[x, y-1][0]
                self.positionImage[1] = self.coordinatesPrintGraphic.value[x, y-1][1]

        if _movement == Movement.DOWN:
            x = self.position[0]
            y = self.position[1]
            if self.checkPossibilitiesMovementSelector(_movement):
                self.position = [x, y+1]
                self.positionImage[0] = self.coordinatesPrintGraphic.value[x, y+1][0]
                self.positionImage[1] = self.coordinatesPrintGraphic.value[x, y+1][1]

    def checkPossibilitiesMovementSelector(self, _movement):
        if _movement == Movement.RIGHT:
            newX = self.position[0]+1
            newY = self.position[1]
            if newX < self.limit[1]:
                return True
            else:
                return False

        if _movement == Movement.LEFT:
            newX = self.position[0]-1
            newY = self.position[1]
            if newX >= self.limit[0]:
                return True
            else:
                return False

        if _movement == Movement.UP:
            newX = self.position[0]
            newY = self.position[1]-1
            if newY >= self.limit[2]:
                return True
            else:
                return False

        if _movement == Movement.DOWN:
            newX = self.position[0]
            newY = self.position[1]+1
            if newY < self.limit[3]:
                return True
            else:
                return False