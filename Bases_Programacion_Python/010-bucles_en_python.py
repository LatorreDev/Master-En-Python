#!/usr/bin/python3
# Bucles en python

# Bucle for
# Estructura iterativa que se repite X cantidad de veces
# Puede ser una lista, tupla, diccionario, rango, etc.

contador = 0
resultado = 0 

for contador in range(0, 5):
    print("voy por el " + str(contador))
    resultado += contador

print("El resultado es: " + str(resultado))

# Ejemplo con tablas de multiplicar

numero_usuario = int(input("Ingresa tu numero: "))

if numero_usuario < 1:
    print("No se puede multiplicar por un numero menor a 1")
else:
    print(f"--- Tabla de multiplicar del {numero_usuario} ---")

    for numero_tabla in range(1, 11):
        print(f"{numero_usuario} X {numero_tabla} = {numero_usuario * numero_tabla}")
    else:
        print("--- Tabla finalizada ---")

# Bucle while
# Itera tantas veces como sea necesario mientras su condicion sea verdadera

# Ejemplo mostrando numeros de 1 a 100

contador = 1

while contador <= 100:
    print(f"estoy en el numero {contador}")
    contador += 1