from Pion import Pion

class Roi(Pion):
    
    def __init__(self, is_white):
        super().__init__()#Récupère l'initialisation de l'objet parent
        self._type = "Roi"
        self._white=is_white
        
        
    def __str__(self):
        if(self._white):
            return("Roi blanc")
        else:
            return ("Roi noir")

    def is_deplacement_correct(self, plateau, old_position: tuple, new_position: tuple):
            if(super().is_deplacement_correct(plateau, old_position, new_position)==False): return False#Appel de la fonction de l'objet parent. Si le déplacement y est faux, je l'arrête
            
            deplacement_x = new_position[0] - old_position[0]
            deplacement_y = new_position[1] - old_position[1]
            
            if((abs(deplacement_x) == 0 or abs(deplacement_x) == 1) and (abs(deplacement_y)==1 or abs(deplacement_y)==0)):#Déplacement en diagonale
                    return True
