from Point import Point 

class Robot:
  """Classe qui définit un Robot"""
  
  def __init__(self, position, vitesse):
    self.position = position
    self.vitesse = vitesse


 

  #=============   Methode standard , de class , statique   ==================================
  def bouger(self):
    return

  def setVitesse():  
    return

  def tourner(angle):
    return
  def __str__(self):
    return "je suis un Robot , position : {} , vitesse : {} ".format(self.position,self.vitesse)


#Programme principal (=main)
r1 = Robot(Point(4,5), 3)
print(r1)


