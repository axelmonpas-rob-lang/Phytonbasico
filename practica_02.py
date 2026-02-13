mi_lista_2 = {"lunes","martes","miercoles","jueves","viernes"}
f = 0

while f <= 12:
    for i in mi_lista_2:
        if i != "lunes" :
          print(f"{i}")
          f = f + 1
          continue
        
    if f ==12:
        break