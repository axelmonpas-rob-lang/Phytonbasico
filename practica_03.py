r=0 
print("-----------calculadora expres-----------")
while r == 0:
    num_1 = float(input("ingrese su primer valor "))
    num_2 = float(input("ingrese su segundo valor "))
    operacion = input("que operacion decea hacer con esos datos? +, -, *, / -> ")

    if operacion == "+":
        resultado = (num_1+num_2)
        print("El resultado de la suma es: ", resultado)
    elif operacion == "-":
            resultado = (num_1-num_2)
            print("el resultado de su resta es ", resultado)
    elif operacion == "*":
            resultado = (num_1*num_2)
            print("el resultado de su multiplicacion es ", resultado)
    elif operacion == "/":
            resultado = (num_1/num_2)
            print("el resultado de su divicion es ", resultado)
    else:
        print("ese dato no es reconocible")

    otra = input("quieres volver a usar la calculadora ? ")
    if otra =="si":
        r = 0
    else:
        print("gracias por usar la calculadora :)")
        r = 1