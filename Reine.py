from Pion import Pion

class Reine(Pion):
    
    def __init__(self, is_white):
        super().__init__()#Récupère l'initialisation de l'objet parent
        self._type = "Reine"
        self._white=is_white
        self._mouvement=(('*', '*'))#J'indique la portée de déplacement du pion, un vecteur x=0 y=1  Format : ( (1, 3), (-1, -3), ... ) )
        
        
    def __str__(self):
        if(self._white):
            return("Reine blanche")
        else:
            return ("Reine noire")

    def is_deplacement_correct(self, plateau, old_position: tuple, new_position: tuple):
        if(super().is_deplacement_correct(plateau, old_position, new_position)==False): return False#Appel de la fonction de l'objet parent. Si le déplacement y est faux, je l'arrête
        
        deplacement_x = new_position[0] - old_position[0]
        deplacement_y = new_position[1] - old_position[1]
        
        if(deplacement_x == deplacement_y):#Déplacement en diagonale
                return True
        elif(old_position[0]==new_position[0] or old_position[1]==new_position[1]):#Avance ou recule
                return True