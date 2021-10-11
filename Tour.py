from Pion import Pion

class Tour(Pion):
    
    def __init__(self, is_white):
        super().__init__()#Récupère l'initialisation de l'objet parent
        self._type = "Tour"
        self._white=is_white
        self._mouvement=((0, '*'), ('*', 0))#J'indique la portée de déplacement du pion, un vecteur x=0 y=1  Format : ( (1, 3), (-1, -3), ... ) )
        
    def __str__(self):
        if(self._white):
            return("Tour blanche")
        else:
            return ("Tour noire")