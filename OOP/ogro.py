from enemigo import *

class ogro(Enemigo):
    def __init__(self, puntos_enegia=20, ataque=3):
        super().__init__(tipo_enemigo='Ogro', puntos_enegia=puntos_enegia, ataque=ataque)

    def habla(self):
        print("Ogro aplastar todo")