#!/usr/bin/env python3
# Capturar excepciones y manejar errores en codigo

try:
    nombre = input("Cual es tu nombre: ")

    if len(nombre) > 1:
        nombre_user = "El nombre es " + nombre

    print(nombre_user)

except:
    print("Ha ocurrido un error, por favor asegurese que introdujo un nombre valido")
else:
    print("Todo ha funcionado correctamente")
finally: # Detecta cuando ha terminado todo el try, except, else, etc
    print("Fin de la iteracion")

# Multiples excepciones
try:
    numero = int(input("numero para elevarlo al cuadrado: "))
    print(f"El cuadrado es: {numero*numero}")
except TypeError:
    print("Debes convertir tus cadenas en enteros dentro del codigo!!")
except ValueError:
    print("Asegurate que ingresaste un numero")
except Exception as error:
    print("Ha ocurrido un error", type(error).__name__)

# Excepciones personalizadas o lanzar expecion

nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))

try:
    if edad < 5 or edad > 110:
        raise ValueError("La edad introducidad no es real")
    elif len(nombre) <= 1:
        raise ValueError("Introduce un nombre valido")
    else:
        print(f"Bienvenido {nombre}")
except ValueError:
    print("Introduce los datos correctamente")

