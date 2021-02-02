from Point import Point 


class Vecteur():
    """Classe qui définit un Vecteur"""

    def __init__(self, depart, longueur , direction):
        self.depart = depart
        self.longueur = longueur
        self.direction = direction

 

    #=============   Methode standard , de class , statique   ==================================
    def addition(self, vecteur):
        return

    def soustraction(self, vecteur):
        return
    def __str__(self):
        return "je suis un vecteur de depart " + str(self.depart) + " , de longueure : {}  , et de direction {}".format(self.longueur , self.direction)



#Programme principal (=main)
v1 = Vecteur(Point(1,3) , 4 , 6)

print(v1)

