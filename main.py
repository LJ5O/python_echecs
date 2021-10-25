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

musique = True#De la musique en jouant ? ( +20 points d'intelligence )

plateau_jeu = Plateau()#Plateau, enregistre tous les tours, la position des pièces, ect

pygame.init()
#####################FONCTIONS#####################

def plateauToPygame(plateau, fenetre, pygame):
    
    for i in range(len(plateau)):
        for j in range(len(plateau)):
            if(plateau[i][j]!=None):
                #Ajouter la pièce à l'interface. Une case = 100 pixels
                if(type(plateau[i][j]) is PionBasique):
                    if(plateau[i][j].is_white()):
                        fenetre.blit(pionBlanc, (j*100,i*100))
                    else:
                        fenetre.blit(pionNoir, (j*100,i*100))
                elif(type(plateau[i][j]) is Fou):
                    if(plateau[i][j].is_white()):
                        fenetre.blit(fouBlanc, (j*100,i*100))
                    else:
                        fenetre.blit(fouNoir, (j*100,i*100))
                elif(type(plateau[i][j]) is Cheval):
                    if(plateau[i][j].is_white()):
                        fenetre.blit(chevalBlanc, (j*100,i*100))
                    else:
                        fenetre.blit(chevalNoir, (j*100,i*100))
                elif(type(plateau[i][j]) is Tour):
                    if(plateau[i][j].is_white()):
                        fenetre.blit(tourBlanche, (j*100,i*100))
                    else:
                        fenetre.blit(tourNoire, (j*100,i*100))
                elif(type(plateau[i][j]) is Roi):
                    if(plateau[i][j].is_white()):
                        fenetre.blit(roiBlanc, (j*100,i*100))
                    else:
                        fenetre.blit(roiNoir, (j*100,i*100))
                elif(type(plateau[i][j]) is Reine):
                    if(plateau[i][j].is_white()):
                        fenetre.blit(reineBlanche, (j*100,i*100))
                    else:
                        fenetre.blit(reineNoire, (j*100,i*100))
    pygame.display.flip()



def calculerCoupsPossibles(plateau, position_depart: tuple):#Calcule tous les déplacement possibles par force brute
    
    coupsPossibles = []
    piece = plateau[position_depart[1]][position_depart[0]]
    
    for i in range(len(plateau)):
        for j in range(len(plateau)):
            if(piece.is_deplacement_correct(plateau, position_depart, (j,i))):
                coupsPossibles.append((j,i))
    return coupsPossibles


def afficherCoupsPossibles(fenetre, coups):
    if(coups==[]): return
    for e in coups:
        fenetre.blit(emplacementPossible, (e[0]*100, e[1]*100))
        
def resetAffichage(fenetre):
    fenetre.fill((0,0,0))
    fenetre.blit(fond, (0,0))
    pygame.display.flip()
    
def isPartieTerminee(plateau):#Recherche les deux rois sur le plateau. S'ils sont tous les deux là, la partie continue. S'il en manque un, la partie est finie.
    roiBlanc = False
    roiNoir = False
    for i in range(len(plateau)):
        for j in range(len(plateau)):
            if(type(plateau[i][j])==Roi):
                if(plateau[i][j].is_white()):
                    roiBlanc = True
                else:
                    roiNoir = True
    if(not roiBlanc):
        print("Les noirs gagnent !")
        return True
    elif(not roiNoir):
        print("Les blancs gagnent !")
        return True
    else:
        return False



#####################PYGAME#####################


#Création de la fenêtre Pygame (carré : largeur = hauteur)
fenetre = pygame.display.set_mode((800,800)) #
fond = pygame.image.load("sprites/plateau.gif").convert()

#Récupération des sprites https://www.deviantart.com/atskaheart/art/Chess-Pieces-208065294
pionNoir = pygame.image.load("sprites/PionNoir.gif").convert_alpha()
fouNoir = pygame.image.load("sprites/FouNoir.gif").convert_alpha()
tourNoire = pygame.image.load("sprites/TourNoire.gif").convert_alpha()
roiNoir = pygame.image.load("sprites/RoiNoir.gif").convert_alpha()
reineNoire = pygame.image.load("sprites/ReineNoire.gif").convert_alpha()
chevalNoir = pygame.image.load("sprites/ChevalNoir.gif").convert_alpha()

pionBlanc = pygame.image.load("sprites/PionBlanc.gif").convert_alpha()
fouBlanc = pygame.image.load("sprites/FouBlanc.gif").convert_alpha()
tourBlanche = pygame.image.load("sprites/TourBlanche.gif").convert_alpha()
reineBlanche = pygame.image.load("sprites/ReineBlanche.gif").convert_alpha()
chevalBlanc = pygame.image.load("sprites/ChevalBlanc.gif").convert_alpha()
roiBlanc = pygame.image.load("sprites/RoiBlanc.gif").convert_alpha()

emplacementPossible = pygame.image.load("sprites/EmplacementValide.gif").convert_alpha()

clock = pygame.time.Clock()#Je crée la clock pour actualiser l'affichage à la même vitesse sur tout ordinateur

fenetre.blit(fond, (0,0))#Ajout du background

plateauToPygame(plateau_jeu.get_plateau(), fenetre, pygame)
pygame.display.flip()#Rechargement affichage

######Musique######
if(musique):
    pygame.mixer.init()
    pygame.mixer.music.load("musique/musique.mp3")
    pygame.mixer.music.play(-1)#Joue la musique indéfiniment


tour_des_blancs = True#Détermine le joueur dont c'est le tour
piece_selection = ()#Enregistre la pièce actuellement utilisée
pygame.display.set_caption("Tour des blancs")


#####################BOUCLE PYGAME#####################


while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            x = pygame.mouse.get_pos()[0]//100
            y = pygame.mouse.get_pos()[1]//100
            
            if(pygame.mouse.get_pressed()[0]==True):#Si click gauche, voir mouvements
                
                resetAffichage(fenetre)
                plateauToPygame(plateau_jeu.get_plateau(), fenetre, pygame)
                
                if(plateau_jeu.get_plateau()[y][x]!=None):
                    if(tour_des_blancs == plateau_jeu.get_plateau()[y][x].is_white()):#Vérifie que le bon joueur prend les bonnes pièces
                        
                        afficherCoupsPossibles(fenetre, calculerCoupsPossibles(plateau_jeu.get_plateau(), (x,y)))
                        piece_selection = (x,y)
                    
                    else:#Un joueur essaie d'utiliser des pièces qui ne sont pas les siennes
                        print("Ce n'est pas votre pièce !")
                        
                        
            elif(pygame.mouse.get_pressed()[2]==True):#Si click droit, valider le mouvement
                if(piece_selection != () ):#Une pièce doit être séléctionnée avant de déplacer
                    if((x,y) in calculerCoupsPossibles(plateau_jeu.get_plateau(), piece_selection)):#Si tout est bon, pièce déplacée et changement de tour
                           
                        #S'il s'agit d'un pion, j'enregistre le fait que le déplacement de deux cases n'est plus valable
                        if(type(plateau_jeu.get_plateau()[piece_selection[1]][piece_selection[0]]) is PionBasique):
                            plateau_jeu.get_plateau()[piece_selection[1]][piece_selection[0]].premier_mouvement_fait()
                            
                        #Déplacement enregistré
                        plateau_jeu.bouger_piece(piece_selection[0], piece_selection[1], x, y)
                        
                        #Rechargement complet de la fenêtre
                        resetAffichage(fenetre)
                        plateauToPygame(plateau_jeu.get_plateau(), fenetre, pygame)
                        
                        #Partie terminée ?
                        if(isPartieTerminee(plateau_jeu.get_plateau())):
                            pygame.quit()
                            sys.exit()
                            break
                        
                        #Changement de tour
                        piece_selection = ()
                        if(tour_des_blancs):
                            tour_des_blancs = False
                            pygame.display.set_caption("Tour des noirs")
                        else:
                            tour_des_blancs = True
                            pygame.display.set_caption("Tour des blancs")
                            
                    else:#Sinon, reclic
                        print("Placement invalide")
                else:
                    print("Séléctionnez une pièce avant !")
            
            
    pygame.display.flip()#Recharge l'affichage, okaou