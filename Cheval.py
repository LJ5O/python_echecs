from Pion import Pion

class Cheval(Pion):
    
    def __init__(self, is_white):
        super().__init__()#Récupère l'initialisation de l'objet parent
        self._type = "Cheval"
        self._white=is_white
        
        
    def __str__(self):
        if(self._white):
            return("Cheval blanc")
        else:
            return ("Cheval noir")

    def is_deplacement_correct(self, plateau, old_position: tuple, new_position: tuple):
        if(super().is_deplacement_correct(plateau, old_position, new_position)==False):return False#Appel de la fonction de l'objet parent
        
        if((old_position[0]+2, old_position[1]+1)==new_position or (old_position[0]+2, old_position[1]-1)==new_position or
           (old_position[0]-2, old_position[1]+1)==new_position or (old_position[0]-2, old_position[1]-1)==new_position or
           (old_position[0]+1, old_position[1]+2)==new_position or (old_position[0]+1, old_position[1]-2)==new_position or
           (old_position[0]-1, old_position[1]+2)==new_position or (old_position[0]-1, old_position[1]-2)==new_position):
                return True