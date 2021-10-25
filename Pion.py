class Pion():
    
    def __init__(self):
        self._type = None
        self._white = None
        
    def get_type(self):#Permet d'obtenir le type du pion
        return self._type
    
    def is_white(self):#Permet de savoir s'il est blanc ou non
        return self._white

    def is_deplacement_correct(self, plateau, old_position: tuple, new_position: tuple):#Positions : x,y
        largeur_plateau = len(plateau[0])
        longueur_plateau = len(plateau)
        if(old_position==new_position): return False
        
        if(old_position[0]+(new_position[0]-old_position[0])>largeur_plateau or old_position[1]+(new_position[1]-old_position[1])>longueur_plateau):#Je vérifie ici que la pièce ne sort pas du plateau
            #print("Déplacement hors du plateau")
            return False
        
        if(plateau[new_position[1]][new_position[0]] != None):#Vérifie la couleur et la présence d'un pion à l'endroit du déplacement
            if(plateau[new_position[1]][new_position[0]].is_white() == self.is_white()):  #Bloque uniquement si le pion est de la même couleur, pour permettre la capture de pions
                #print("Il y a déjà un pion ici")
                return False
        
    def __str__(self):
        return("Pion")#Ne devrait jamais s'afficher
