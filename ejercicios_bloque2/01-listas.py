#!/usr/bin/env python3
# Ejercicio con listas en python3

"""
Un programa que tiene 8 numeros enteros
Recorrerla y mostrarla, ordenarla y mostrarla
buscar un elemento en la lista en base a lo que
el usuario nos pida por input
"""

my_list=[8,7,6,1,2,3,5,4]
# Mostrar la lista
print(my_list)
# Ordenar la lista
my_list.sort()
print(my_list)

looking = int(input("Numero a buscar: "))
search = my_list.index(looking)
print(f"el elemento ESTA en la lista y es el indice {search}")
"""
for index in range(0,len(my_list)):
    if (my_list[index] == looking):
        print(f"el elemento ESTA en la lista, en la posicion {my_list[index]}")
        break
    else:
        pass
 #print("El elemento NO ESTA en la lista")
 """
