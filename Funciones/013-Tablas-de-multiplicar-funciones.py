#!/usr/bin/python
# Tablas de multiplicar con funciones

print("***** Tablas de multiplicar con funciones *****")

numero = int(input("Dame el numero de la tabla: "))

def tabla(numero):
    print(f"***** Tabla de multiplicar del numero {numero}")
    print("\n")

    for contador in range(11):
        operacion = numero * contador
        print(f"{numero} * {contador} = {operacion}")

    print("\n")    

tabla(numero)

