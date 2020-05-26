#!/usr/bin/env python3
# Diccionarios dentro de listas

contactos = [

            {
            "nombre": "David",
            "email": "david@latorredev.com"
            },

            {
            "nombre": "Camilo",
            "email": "camilo@latorredev.com"
            },

            {
            "nombre": "Leonardo",
            "email": "leo@latorredev.com"
            }

        ]
print(contactos[2]["nombre"]) # Obtener un elemento especifico del diccionario dentro de la lista
print("------------------------------------")
for contacto in contactos: # Obtener todos los elementos de un diccionario dentro de la lista
    print(f"Nombre del contacto: {contacto['nombre']}")
    print(f"Mail del contacto: {contacto['email']}")
    print("-----------------------------------")
