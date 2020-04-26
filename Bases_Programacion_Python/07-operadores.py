#!/usr/bin/python3
# Operadores en python

# Operadores aritmeticos

numero1 = 77
numero2 = 44

"""
= es un operador de asignacion
- operador de resta
+ operador de suma
/ operador de divison
* operacion de multiplicacion
% operador de modulo o residuo
"""

print("*************** Calculadora ******************")

print("El primer valor es {}".format(numero1))
print("El segundo valor es {}".format(numero2))

print("*******************************")

print(f"La suma de los numeros es: {numero1 + numero2}")
print(f"La resta de los numeros es: {numero1 - numero2}")
print(f"La multiplicacion de los numeros es: {numero1 * numero2}")
print(f"La division de los numeros es: {numero1 / numero2}")
print(f"El residuo de la division de los numeros es: {numero1 % numero2}")

# operadores de asignacion

edad = 29
print(edad)
edad += 5 # Esto equivale a hacer edad = edad + 5, el valor se suma a la variable
print(edad)
edad -= 10 # Este es igual al caso anterior pero resta.
print(edad) 
edad *= 2 # caso para multiplicar
print(edad) 
edad /= 4  # caso para dividir
print(edad)
edad %= 5 # caso para residuo
print(edad)

# Operadores de incremento y decremento

# Incrementan y decrementan en la cantidad especificada.

year = 2020
print(year)

# Incremento
year = year + 1
print(year)
# Decremento
year = year - 1
print(year)
# Pre incremento
year = 1 + year
print(year)
# Pre decremento
year = 1 - year
print(year)