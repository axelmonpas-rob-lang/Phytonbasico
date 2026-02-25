from enemigo import *

class zombie(Enemigo):
    def __init__(self, puntos_enegia=10, ataque=1):
        super().__init__(tipo_enemigo='zombie', puntos_enegia = puntos_enegia, ataque = 1)

    def habla(self):
        print("*hummmmmmmmm...")
    
    def propagar_enfermedad(self):
        print("el zomnie esta tratando de propagar la enfermedad")