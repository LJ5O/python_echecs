from Pion import Pion

class Cheval(Pion):
    
    def __init__(self, is_white):
        super().__init__()#Récupère l'initialisation de l'objet parent
        self._type = "Cheval"
        self._white=is_white
        self._mouvement=(('*', '*'))#J'indique la portée de déplacement du pion, un vecteur x=0 y=1  Format : ( (1, 3), (-1, -3), ... ) )
        
        
    def __str__(self):
        if(self._white):
            return("Cheval blanc")
        else:
            return ("Cheval noir")
