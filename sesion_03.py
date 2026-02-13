#loops

mi_lista = {1,2,3,4}

for i in mi_lista:
    print("el numero es: ",i)

resultado = 0
for i in mi_lista:
    resultado += i

print(f"el reslutado de la suma de mi lista es: {resultado}")

for i in range(2, 9):
    print(i)

mi_lista_2 = {"lunes","martes","miercoles","jueves","viernes"}

for i in mi_lista_2:
    if i != "lunes" :
       print(f"feliz {i}")

#while loop
i = 0

while i < 5 :
    if i == 3:
        continue
    print(i)
    if i ==4:
        break
    
else:
    print("i es es ahora mayor o igual a 5")

#practica 2
#dada la lista mi_lista2 = {"lunes","martes","miercoles","jueves","viernes"}
#impreime cada elemento de la lista 3 veces y cuando sea lunes no lo incluya
#pista: usa los 2 tipos de loops while y for en el mismo prigrama para lograrlo
