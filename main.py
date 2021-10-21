import pygame
from pygame.locals import *
import sys


from Plateau import Plateau

from PionBasique import PionBasique
from Tour import Tour
from Fou import Fou
from Cheval import Cheval
from Reine import Reine
from Roi import Roi

plateau_jeu = Plateau()#Plateau, enregistre tous les tours, la position des pièces, ect

pygame.init()
#####################FONCTIONS#####################

def plateauToPygame(plateau, fenetre, pygame):
    
    for i in range(len(plateau)):
        for j in range(len(plateau)):
            if(plateau[i][j]!=None):
                pass
                #Ajouter la pièce à l'interface
    







#####################PYGAME#####################


#Création de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((750,750), RESIZABLE)
fond = pygame.image.load("sprites/plateau.gif").convert()

#Récupération des sprites
pionNoir = pygame.image.load("sprites/PionNoir.gif").convert_alpha()
fouNoir = pygame.image.load("sprites/FouNoir.gif").convert_alpha()
TourNoire = pygame.image.load("sprites/TourNoire.gif").convert_alpha()
RoiNoir = pygame.image.load("sprites/RoiNoir.gif").convert_alpha()
ReineNoire = pygame.image.load("sprites/ReineNoire.gif").convert_alpha()

pionBlanc = pygame.image.load("sprites/PionBlanc.gif").convert_alpha()
fouBlanc = pygame.image.load("sprites/FouBlanc.gif").convert_alpha()
TourBlanche = pygame.image.load("sprites/TourBlanche.gif").convert_alpha()
ReineBlanche = pygame.image.load("sprites/ReineBlanche.gif").convert_alpha()
RoiBlanc = pygame.image.load("sprites/RoiBlanc.gif").convert_alpha()

clock = pygame.time.Clock()#Je crée la clock pour actualiser l'affichage à la même vitesse sur tout ordinateur

fenetre.blit(fond, (0,0))#Ajout du background
pygame.display.flip()#Rechargement affichage

#plateauToPygame(plateau_jeu.get_plateau(), fenetre, pygame)



#TODO : https://coderslegacy.com/python/pygame-mouse-click/
while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



#####################ECHECS#####################
            
            
tour_des_blancs = True#Détermine le joueur dont c'est le tour

while(True):
    print("**********Plateau**********")
    print(plateau_jeu)
    print("********************")
    if(tour_des_blancs): 
        print("****Tour des Blancs****")
    else:
        print("****Tour des Noirs****")
        
    while(True):
        depart=(int(input("Position X de la pièce à déplacer ?")), int(input("Position Y de la pièce à déplacer ?")))#Demande la position de la pièce à déplacer
    
        piece = plateau_jeu.get_piece(depart[0], depart[1])#Rècupère la pièce sur la case
        if(piece==None):#S'il n'y a rien
            print("Il n'y a rien ici")
        elif(piece.is_white() != tour_des_blancs):#Vérification de la couleur de cette pièce
            print("Ce n'est pas votre pièce")
        else:#Pièce valide, je sors de cette boucle
            break
    print(str(piece)+ " séléctionné")
    
    
    
    while(True):
        arrivee=(int(input("Position X où placer la pièce ?")), int(input("Position Y où placer la pièce ? 999 pour annuler")))#Nouvelle position de la pièce
        if(999 in arrivee): break#Fin du tour si 999
        
        if(piece.is_deplacement_correct(plateau_jeu.get_plateau(), depart, arrivee)):#Méthode vérifiant le placement correct de la pièce
            plateau_jeu.bouger_piece(depart[0], depart[1], arrivee[0], arrivee[1])
            break
        else:
            print("Vous ne pouvez pas faire ce déplacement !")
    
    
    
    
    
    if(tour_des_blancs):
        tour_des_blancs = False
    else:
        tour_des_blancs = True
