#Tuplas
mi_tupla = (2, 4)
print("Mi tupla. ",mi_tupla)

#lista
mi_lista =[1, 3.1416, "Aaron", mi_tupla]
print("El primer elemento de mi lista: ", mi_lista[0])
print("El cuarto elemento de mi lista: ", mi_lista[3])
print("El tercer elemento de mi lista: ", mi_lista[2])

#Diccionario
mi_diccionario = {"mi_lista":mi_lista,
               "Nombre": "Aaron",
               "pi": 3.1416,
               "Tel": "664-2334455"}
print("llave para acceder a mi diccionario mi_lista",mi_diccionario["mi_lista"])
print("llave para acceder a pi",mi_diccionario["pi"])
print("llave para acceder a Tel",mi_diccionario["Tel"])