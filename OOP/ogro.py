from enemigo import *
import random 

class ogro(Enemigo):
    def __init__(self, puntos_enegia=20, ataque=3):
        super().__init__(tipo_enemigo='Ogro', puntos_enegia=puntos_enegia, ataque=ataque)

    def habla(self):
        print("Ogro aplastar todo")

    def ataque_especial(self):
        print("ogro ataque especial")
        funcion_ataque_especial = random.random() < 0.20
        if funcion_ataque_especial:
            self.ataque <= 4
            print("ogro enojado y incremento su ataque por 4")
