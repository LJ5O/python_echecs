from Pion import Pion

class PionBasique(Pion):
    
    def __init__(self, is_white):
        super().__init__()#Récupère l'initialisation de l'objet parent
        self._type = "Pion Basique"
        self._white=is_white
        self._mouvement=((0, 1))#J'indique la portée de déplacement du pion, un vecteur x=0 y=1  Format : ( (1, 3), (-1, -3), ... ) )
        
    def __str__(self):
        if(self._white):
            return("Pion blanc")
        else:
            return ("Pion noir")
        
    def is_deplacement_correct(self, plateau, old_position: tuple, new_position: tuple):
        if(super().is_deplacement_correct(plateau, old_position, new_position)==False):return False#Appel de la fonction de l'objet parent
        
        if(self.is_white()):#Pas le même dépalcement en fonction de la couleur
            
            if(old_position[0]==new_position[0] and old_position[1]+1==new_position[1]):#Avance de 1
                return True
            elif((old_position[0]==new_position[0]+1 or old_position[0]==new_position[0]-1) and old_position[1]+1==new_position[1] and plateau[new_position[1]][new_position[0]]!=None):
                #Capture d'un ennemi, couleur déjà vérifiée dans la méthode parente
                return True
            else:#Incorrect
                return False
            
        else:
            
            if(old_position[0]==new_position[0] and old_position[1]-1==new_position[1]):#Avance de 1
                return True
            elif((old_position[0]==new_position[0]+1 or old_position[0]==new_position[0]-1) and old_position[1]-1==new_position[1] and plateau[new_position[1]][new_position[0]]!=None):
                #Capture d'un ennemi
                return True
            else:#Incorrect
                return False
            
