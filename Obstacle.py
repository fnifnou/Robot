from Point import Point 

class Obstacle():
    """Classe qui définit un Obstacle"""

    def __init__(self, position):
        self.position = position



 

    #=============   Methode standard , de class , statique   ==================================
    def bouger(self, nouvposi):
        self.position = nouvposi

    def __str__(self):
        return "je suis un obstacle en position " + str(self.position)





#Programme principal (=main)
o1 = Obstacle(Point(3,5))

print(o1)
