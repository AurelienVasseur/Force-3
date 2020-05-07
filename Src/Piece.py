from Image import Image
import pygame


class Piece:
    def __init__(self, _image):
        # self.position = [None, None] On a pas besoin de la position (on prend simplement la postion dans la matrice)
        self.image = pygame.image.load(_image.value[0])

        self.imageResize = pygame.transform.scale(self.image, _image.value[1])
        self.positionImage = self.imageResize.get_rect()
