from PionBasique import PionBasique
from Tour import Tour
from Fou import Fou
from Cheval import Cheval
from Reine import Reine
from Roi import Roi
class Plateau():
    
    def __init__(self, largeur=8, longueur=8):#Création du plateau
        self._plateau = [[None for j in range(longueur)] for i in range(largeur)]
        self._historique = []#Historique des états du plateau
        
        for i in range(len(self._plateau[1])):#INstallation des pions
            self._plateau[1][i] = PionBasique(True)
        for i in range(len(self._plateau[6])):
            self._plateau[6][i] = PionBasique(False)
            
        self._plateau[0][0] = Tour(True)
        self._plateau[0][7] = Tour(True)
        self._plateau[7][0] = Tour(False)
        self._plateau[7][7] = Tour(False)
        
        self._plateau[0][1] = Cheval(True)
        self._plateau[0][6] = Cheval(True)
        self._plateau[7][1] = Cheval(False)
        self._plateau[7][6] = Cheval(False)
        
        self._plateau[0][2] = Fou(True)
        self._plateau[0][5] = Fou(True)
        self._plateau[7][2] = Fou(False)
        self._plateau[7][5] = Fou(False)
        
        self._plateau[0][3] = Roi(True)
        self._plateau[0][4] = Reine(True)
        self._plateau[7][3] = Reine(False)
        self._plateau[7][4] = Roi(False)
        
    def get_plateau(self):#Getter du plateau
        return self._plateau
    
    def set_plateau(self, plateau: list):
        self._historique.append(self._plateau)
        self._plateau=plateau
        
    def get_piece(self, x, y):
        return(self._plateau[y][x])
    
    def set_piece(self, x, y, piece):
        self._plateau[y][x]=piece
        
    def bouger_piece(self, x, y, x2, y2):
        self._historique.append(self._plateau)
        self._plateau[y2][x2]=self._plateau[y][x]
        self._plateau[y][x]=None
        
    def __str__(self):
        retour=""
        for i in range(len(self._plateau)-1, -1, -1):
            for j in range(len(self._plateau)):
                retour+=str(self._plateau[i][j])+","
            retour+="\n"
        return(retour)

