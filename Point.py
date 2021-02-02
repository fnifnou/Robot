class Point:
    """Classe qui définit un Robot"""
  
    def __init__(self, x, y):
        self.x = x
        self.y = y


 

    #=============   Methode standard , de class , statique   ==================================
    def bouger(self,w,z):
        self.x = w
        self.y = z


    def __str__(self):
        return "x : {} , y : {} ".format(self.x , self.y)


#Programme principal (=main)
P1 = Point(1, 2)
#print(P1)