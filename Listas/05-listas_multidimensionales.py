#!/usr/bin/python3
# Listas multidimensionales

"""
Una lista multidimensional es una lista que
contiene otras listas dentro
"""

def linea_div():
    print("************************")

linea_div()
print("Lista de contactos")
linea_div()

# Lista multidimensional
contactos = [
    [
        "Antonio",
        "antonio@antonio.com"
    ],
    [
        "Luis",
        "luis@luis.com"
    ],
    [
        "Salvador",
        "salvador@salvador.com"
    ]
]

print(contactos)

# Acceder a un elemento especifico, en este caso al email de Luis
print(contactos[1][1]) # Accede al indice numero 1 y la vez al su sub indice 1

print("\n")
linea_div()
for contacto in contactos: # Accede a cada indice
    for elemento in contacto: # Accede a cada subindice
        if contacto.index(elemento) == 0: # Si el subindice es igual a posicion 0
            print(f"Nombre: {elemento}")
        else:
            print(f"Email: {elemento}") # Si el subindice no es es igual a posicion 0
    print("\n")
