class Verif():
    @staticmethod
    def fou(plateau, old_position, new_position):
        deplacement_x = new_position[0] - old_position[0]
        deplacement_y = new_position[1] - old_position[1]
        
        if(abs(deplacement_x) == abs(deplacement_y)):#Déplacement en diagonale
            
            if(deplacement_x==deplacement_y and deplacement_x>0):#Vers nord-est
                for i in range(1, deplacement_x):
                    if(plateau[old_position[1]+i][old_position[0]+i]!=None):
                        return False
                return True
            elif(deplacement_x==deplacement_y and deplacement_x<0):#Vers sud-ouest
                for i in range(1, abs(deplacement_x)):
                    if(plateau[old_position[1]-i][old_position[0]-i]!=None):
                        return False
                return True
            elif(deplacement_x!=deplacement_y and deplacement_y<0):#Vers sud-est
                for i in range(1, abs(deplacement_x)):
                    if(plateau[old_position[1]-i][old_position[0]+i]!=None):
                        return False
                return True
            elif(deplacement_x!=deplacement_y and deplacement_x<0):#Vers nord-ouest
                for i in range(1, abs(deplacement_x)):
                    if(plateau[old_position[1]+i][old_position[0]-i]!=None):
                        return False
                return True
        
        else:
            return False
    
    @staticmethod
    def tour(plateau, old_position, new_position):
        if(old_position[0]==new_position[0]):#Change y
            
            if(new_position[1]-old_position[1]>0):#Si j'avance
                for i in range(old_position[1]+1, new_position[1], +1):#Boucle sur toutes les cases traversées
                    if(plateau[i][old_position[0]]!=None):#S'il y a quelque chose sur le chemin, déplacement annulé
                        return False
                return True
            else:#Je recule
                for i in range(old_position[1]-1, new_position[1], -1):#Boucle sur toutes les cases traversées
                    if(plateau[i][old_position[0]]!=None):#S'il y a quelque chose sur le chemin, déplacement annulé
                        return False
                return True
                               
                               
        elif(old_position[1]==new_position[1]):#Change x
            if(new_position[0]-old_position[0]>0):#Si j'avance
                for i in range(old_position[0]+1, new_position[0], +1):#Boucle sur toutes les cases traversées
                    if(plateau[old_position[1]][i]!=None):#S'il y a quelque chose sur le chemin, déplacement annulé
                        return False
                return True
            else:#Je recule
                for i in range(old_position[0]-1, new_position[0], -1):#Boucle sur toutes les cases traversées
                    if(plateau[old_position[1]][i]!=None):#S'il y a quelque chose sur le chemin, déplacement annulé
                        return False
                return True