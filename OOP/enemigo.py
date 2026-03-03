class Enemigo:
    tipo_enemigo: str
    puntos_energia: int=10
    ataque = 1

    def __init__(self, tipo_enemigo, puntos_enegia = 10, ataque = 1):
        self.__tipo_enemigo = tipo_enemigo
        self.puntos_energia = puntos_enegia
        self.ataque = ataque

    def get_tipo_enemigo(self,):
        return self.__tipo_enemigo
    
    def habla(self):
        print(f"yo soy {self.__tipo_enemigo}. preparado para pelear")

    def caminar(self):
        print(f"{self.tipo_enemigo} se mueve cerca de ti")

    def atacar(self):
        print(f"{self.__tipo_enemigo} ataca con un {self.ataque} de daño")
    
    def ataque_especia(self):
        print("el enemigo no tiene ataque especial")