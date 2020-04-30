import numpy as np
import pygame
from pygame.locals import *
import math
import os

os.chdir("C:/Users/zerat/Onedrive/Documents/UTBm/S2/IA41/Force-3")
#             ----- Force 3 -----

#Initialisation des modules de pygame
pygame.init()


#Variables
couleur=[]
grillePion = np.zeros([2,2])
grilleCarres = np.zeros([2,2])
magicNumber = 0

#Classes
class Tablier:

	def __init__(self):
		self.grilleCarres=grilleCarres
		self.grillePion=grillePion

	def occuperCarre(self,i,j):
		if grilleCarres[i,j]==1:
			return True
		else:
			return False
		
	def occuperPion(self,i,j):
		if grillePion[i,j]==1:
			return True
		else:
			return False	

class Pion:

	def _init_(self,couleur):
		self.couleur=[]
		self.emplacementPion=[]
		self.numero=10
"""
	def right(self,i,j):
		if (Tablier.occuperCarre(i,j) == False):
			
	def left(self,i,j):
		if (Tablier.occuperCarre(i,j) == False):
	
	def up(self,i,j):
		if (Tablier.occuperCarre(i,j) == False):
	
	def down(self,i,j):
		if (Tablier.occuperCarre(i,j) == False):
"""

class carres:

	positions_carres=[(0,0),(50,0),(100,0),(0,50),(50,100),(100,0),(100,50),(100,100)] #Position départ carrés

	def __init__(self):
		
		self.imageCarre= pygame.image.load("carre.jpg")
		self.position_carre=carre.get_rect()
	
	def start(liste8carre,positions_carres):
		for i in range(8):
			liste8carre[i].position_carre=liste8carre[i].position_carre.move(positions_carres[i])

"""
	def right(self,tablier,i,j):
		if (tablier.occuperCarre(i,j) == False):
			
	def left(self,i,j):
		if (Tablier.occuperCarre(i,j) == False):
	
	def up(self,i,j):
		if (Tablier.occuperCarre(i,j) == False):
	
	def down(self,i,j):
		if (Tablier.occuperCarre(i,j) == False):
"""



#Disques blanc
disque_blanc_1 = Pion()
disque_blanc_2 = Pion()
disque_blanc_3 = Pion()
disque_blanc=[disque_blanc_1,disque_blanc_2,disque_blanc_3]
for i in disque_blanc:
	i.couleur=[0]
#Disques noir
disque_noir_1 = Pion()
disque_noir_2 = Pion()
disque_noir_3 = Pion()
disque_noir=[disque_noir_1,disque_noir_2,disque_noir_3]
for i in disque_noir:
	i.couleur=[1]
	
tablier=Tablier()





#Création fenêtre
fenetre = pygame.display.set_mode((840,680),RESIZABLE)
fond = pygame.image.load("Image/background.jpg").convert()
fenetre.blit(fond, (0,0)) #Colle l'image en haut à gauche de la fenêtre de tracé (ici, l'ecran)



#Affichage grille
grid = pygame.image.load("Image/grid.jpg")
grid.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
fenetre.blit(grid,(0,0))

#Affichage carré
carre1=pygame.image.load("Image/carre.jpg")
carre=pygame.transform.scale(carre1,(400,400))
position_carre=carre.get_rect()



fenetre.blit(carre,(-75,-75))
fenetre.blit(carre,(160,165))
fenetre.blit(carre,(560,560))


pygame.display.flip() #L'affichage devient effectif : l'image est rendue visible.

listecarres=[]
for i in range (8):
	cr=carre()
	listecarres.append(cr)

#Variable de la fenêtre
continuer = 1
loop = True
while loop: #Boucle d'événements
	"""
	#Jeu
	for i in range(2):
		for j in range(2):
			if emplacementsPion[i,j] == 1:
				break
			#else:

				
		magicNumber=0
	
	"""
	carres.start(listecarres,position_carre)

	#Afficher fênetre
	pygame.display.flip()
	#Fermer fênetre
	for event in pygame.event.get(): #parcours de la liste des événements

		if (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE):
			print("Espace !")

		if magicNumber == 30:
			loop=False
		if magicNumber != 30:
			magicNumber=0
		if(event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_ESCAPE)): #interrompt la boucle si nécessaire
			loop = False
pygame.quit()