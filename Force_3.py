import numpy as np
import pygame
import pygame.color
import pygame.gfxdraw
from pygame.locals import *
import math
import os

os.chdir("C:/Users/zerat/Onedrive/Documents/UTBm/S2/IA41/Force-3")
#             ----- Force 3 -----

#Initialisation des modules de pygame
pygame.init()


#Variables
couleur=0
grillePion = np.zeros([3,3])
grilleCarres = np.zeros([3,3])
magicNumber = 0
positions_carres_init=[(0,25),(250,25),(500,25),(0,275),(500,500),(500,275),(0,500),(250,500)] #Position départ carrés
positions_pion_init=[(750,50),(750,300),(750,550),(850,50),(850,300),(850,550)] #Position départ Pions
deplacement = 250
continuer = 1
loop = True

#Création fenêtre
fenetre = pygame.display.set_mode((1000,680),RESIZABLE)
fond = pygame.image.load("Image/background.jpg").convert()
fenetre.blit(fond, (0,0)) #Colle l'image en haut à gauche de la fenêtre de tracé (ici, l'ecran)



#Affichage grille
grid = pygame.image.load("Image/grid.jpg")
grid.set_colorkey((255,255,255)) #Rend le blanc (valeur RGB : 255,255,255) de l'image transparent
fenetre.blit(grid,(0,0))


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
	def __init__(self):

		self.imagePion = pygame.image.load("Image/pawnblack.png")
		self.Pion_rezise=pygame.transform.scale(self.imagePion,(100,100))
		self.position_Pion = self.Pion_rezise.get_rect()
		self.coord=[0,0]
		self.numero=10
		self.color=0

	def start(liste6Pion):
		for i in range(6):   # Mise en place des carrées ainsi que de leurs positions respectives
			liste6Pion[i].position_Pion = liste6Pion[i].position_Pion.move(positions_pion_init[i])
			print(liste6Pion[i].position_Pion)
	
	def couleur(self):
		if self.color==1:
			self.imagePion = pygame.image.load("Image/pawnblack.png")
			self.Pion_rezise=pygame.transform.scale(self.imagePion,(100,100))
		else:
			self.imagePion = pygame.image.load("Image/pawnwhite.png")
			self.Pion_rezise=pygame.transform.scale(self.imagePion,(100,100))			

	def right(self,tablier):
		i=self.coord[0]
		j=self.coord[1]
		if (tablier.occuperPion(i+1,j) == False):
			self.coord=[i+1,j]
			grillePion[i][j]=0
			grillePion[i+1][j]=1
			self.position_Pion.move(deplacement,0)

	def left(self,tablier):
		i=self.coord[0]
		j=self.coord[1]
		if (tablier.occuperPion(i-1,j) == False):
			self.coord=[i-1,j]
			grillePion[i][j]=0
			grillePion[i-1][j]=1
			self.position_Pion.move(-deplacement,0)

	def up(self,tablier):
		i=self.coord[0]
		j=self.coord[1]
		if (tablier.occuperPion(i,j+1) == False):
			self.coord=[i,j+1]
			grillePion[i][j]=0
			grillePion[i][j+1]=1
			self.position_Pion.move(0,deplacement)

	def down(self,tablier):
		i=self.coord[0]
		j=self.coord[1]
		if (tablier.occuperPion(i,j-1) == False):
			self.coord=[i,j-1]
			grillePion[i][j]=0
			grillePion[i][j-1]=1
			self.position_Pion.move(0,-deplacement)

class Carres:
	def __init__(self):
		
		self.imageCarre = pygame.image.load("Image/carre.jpg")
		self.carre_rezise=pygame.transform.scale(self.imageCarre,(200,200))
		self.position_carre = self.carre_rezise.get_rect()
		self.coord=[0,0]
	
	def start(liste8carre):
		h=0
		k=0
		for i in range(8):   # Mise en place des carrées ainsi que de leurs positions respectives
			liste8carre[i].position_carre = liste8carre[i].position_carre.move(positions_carres_init[i])
			if k>2:
				k=0
				h=h+1
			if k!=1 or h!=1:
				liste8carre[i].coord=[k,h]
			else:
				liste8carre[i].coord=[2,2]
			print(liste8carre[i].coord)
			k=k+1

		for i in range(3): #Remplissage grilleCarres (on met des 1 la ou sont placés les carrées dans la matrice des carrés)
			for j in range(3):
				if i!=1 or j!=1: 
					grilleCarres[i][j]=1
		print(grilleCarres)
		print("position initiale bien definie")


	def right(self,tablier):
		i=self.coord[0]
		j=self.coord[1]
		if (tablier.occuperCarre(i+1,j) == False):
			self.coord=[i+1,j]
			grilleCarres[i][j]=0
			grilleCarres[i+1][j]=1
			self.position_carre.move(deplacement,0)

	def left(self,tablier):
		i=self.coord[0]
		j=self.coord[1]
		if (tablier.occuperCarre(i-1,j) == False):
			self.coord=[i-1,j]
			grilleCarres[i][j]=0
			grilleCarres[i-1][j]=1
			self.position_carre.move(-deplacement,0)

	def up(self,tablier):
		i=self.coord[0]
		j=self.coord[1]
		if (tablier.occuperCarre(i,j+1) == False):
			self.coord=[i,j+1]
			grilleCarres[i][j]=0
			grilleCarres[i][j+1]=1
			self.position_carre.move(0,deplacement)

	def down(self,tablier):
		i=self.coord[0]
		j=self.coord[1]
		if (tablier.occuperCarre(i,j-1) == False):
			self.coord=[i,j-1]
			grilleCarres[i][j]=0
			grilleCarres[i][j-1]=1
			self.position_carre.move(0,-deplacement)



tablier=Tablier()

#Création carrés
listecarres=[]
for i in range (8):
	cr=Carres()
	listecarres.append(cr)

#Créations Pions
listePion=[]
for i in range (6):
	if i<3: #Pions blancs
		pi=Pion()
		pi.color=0
		pi.couleur()
		listePion.append(pi)
	else: #Pions noirs
		pi=Pion()
		pi.color=1
		pi.couleur()
		listePion.append(pi)


#Initialisation plateau de jeu carrés & pions

Carres.start(listecarres)
Pion.start(listePion)

while loop: #Boucle d'événements

	#Jeu
	for i in range(8):
		fenetre.blit(listecarres[i].carre_rezise,listecarres[i].position_carre)
	for i in range(6):
		fenetre.blit(listePion[i].Pion_rezise,listePion[i].position_Pion)
	


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