# !/usr/bin/python3

# del archivo Persona.py importa la clase Persona
from Persona import Persona

# ahora el "main", que esta fuera de la clase.
perrin = Persona("Juan Eduardo Lopez", "12345678-9")
perrin.imprimir()

# En python, los atributos son publicos... Por lo tanto se pueden modificar directamente

perrin.rut = "12345678-9"
perrin.imprimir()

# Las clases parten con Mayusculas y usan camel, mientras que las funciones usan minusculas y
# se conectan con underscore
# ej clase: (mal) alumno_duoc ; AlumnoDuoc (bien)
# ej funcion: (mal) ImprimirDetalles ; imprimir_detalles (bien)

# Ej: crear una persona leyendo desde consola:
nombre = input("Ingrese un name: ")
rut = input("Ingrese el rut: ")
personaIngresada = Persona(nombre,rut)
personaIngresada.imprimir()