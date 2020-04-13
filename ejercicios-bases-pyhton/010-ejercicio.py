#!/usr/bin/python3
# Ejercicio 10 de fundamentos de python

"""
Ejercicio apra pedir la nota de 15 alumnos
y sacar por pantalla cuantos han reprobado y cuantos han suspendido
"""

aprobados = 0
reprobados = 0

numero_de_alumnos = int(input("Ingresa el numero de alumnos: "))

for contador in range (1,(numero_de_alumnos +1)):
    nota_del_alumno = int(input(f"Dame la nota del alumno No {contador}: "))

    if nota_del_alumno >= 6:
        aprobados += 1
    else:
        reprobados += 1

print (f"La cantidad de alumnos aprobados es: {aprobados}")
print (f"La cantidad de alumnos reprobados es: {reprobados}")
