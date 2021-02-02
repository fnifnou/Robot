class Terrain():
    """Classe qui définit un Vecteur"""

    temps = 1
    
    def __init__(self, grille, echel):
        self.grille = grille
        self.echel = echel
 

    #=============   Methode standard , de class , statique   ==================================
    def calculerDistance():
        return

    
    def __str__(self):
        return "je suis un Terrain , ma grille : {} , echel : {} ".format(self.grille,self.echel)


#Programme principal (=main)
matrisse = [[1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0],
            [1,0,0,0,0]]
v1 = Terrain( matrisse, 2)

print(v1)