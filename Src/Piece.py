from Image import Image
import pygame

class Piece:
    def __init__(self,_image):
        self.position=[None,None]
        self.image = pygame.image.load(_image.value[0])

        #Possible erreur: pygame.Surface ne connait pas 'Rezise'
        #self.image.Rezise = pygame.transform.scale(self.image,_image.value[1]) 
        #self.positionImage =self.image.Rezise.get_rect()

        #Solution
        self.image = pygame.transform.scale(self.image,_image.value[1]) 
        self.positionImage =self.image.get_rect()