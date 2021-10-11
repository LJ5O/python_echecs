from Pion import Pion

class Roi(Pion):
    
    def __init__(self, is_white):
        super().__init__()#Récupère l'initialisation de l'objet parent
        self._type = "Roi"
        self._white=is_white
        self._mouvement=(('*', '*'))#J'indique la portée de déplacement du pion, un vecteur x=0 y=1  Format : ( (1, 3), (-1, -3), ... ) )
        
        
    def __str__(self):
        if(self._white):
            return("Roi blanc")
        else:
            return ("Roi noir")
