from Pion import Pion
from VerifMouvementFouTour import Verif

class Fou(Pion):
    
    def __init__(self, is_white):
        super().__init__()#Récupère l'initialisation de l'objet parent
        self._type = "Fou"
        self._white=is_white
        
    def __str__(self):
        if(self._white):
            return("Fou blanc")
        else:
            return ("Fou noir")

    def is_deplacement_correct(self, plateau, old_position: tuple, new_position: tuple):
        if(super().is_deplacement_correct(plateau, old_position, new_position)==False): return False#Appel de la fonction de l'objet parent. Si le déplacement y est faux, je l'arrête
        
        if(Verif.fou(plateau, old_position, new_position)==True): return True
        else: return False