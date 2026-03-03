from enemigo import *
from zombie import *
from ogro import *

zombie = zombie(10,1)
ogro = ogro(20,3)

def batalla(e1: Enemigo, e2 : Enemigo):
    e1.habla()
    e2.habla()

    while e1.puntos_energia > 0 and e2.puntos_energia > 0:
          print("################")
          e1.ataque_especial()
          e2.ataque_especial()
          print(f"{e1.get_tipo_enemigo()}: quedan: {e1.puntos_energia} puntos de eneguia")
          print(f"{e2.get_tipo_enemigo()}: quedan: {e2.puntos_energia} puntos de eneguia")
          print(f"ataque: {e2.ataque}") 
          e1.puntos_energia -= e2.ataque
          print("==================")
          print(f"ataque:{e1.ataque}")
          e2.puntos_energia -= e1.ataque
          
          print("==============")          
          if e1.puntos_energia > 0:
            print(f"{e1.get_tipo_enemigo()} gano")
          else:
              print(f"{e2.get_tipo_enemigo()} gano")
        
print("=============batalla=======================")
batalla( zombie,ogro )
print("=============fin de la batalla=======================")

#print(f"{zombie.get_tipo_enemigo()} tiene {zombie.puntos_energia} de energia y ataca con {zombie.ataque}") 
#print(f"{ogro.get_tipo_enemigo()} tiene {ogro.puntos_energia} de energia y ataca con {ogro.ataque}") 