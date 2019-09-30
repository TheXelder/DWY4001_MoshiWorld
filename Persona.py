# !/usr/bin/python3

# guardar como Persona.py en la carpeta del proyecto

# vamos a definir una clase. primero una clase como las de Java.

class Persona:

	# en python hayn un solo "constructor", que se llama _init_
	# (doble underscore)init(doble underscore) debe recibir parametro self!!!
	# la gente en python se ha puesto de acuerdo para considerar si una variable lleva
	# delante un (underscore) _ se debe tratar como una variable privada
	def __init__(self, nombre, rut):
		self.nombre = nombre
		self.rut = rut

	def imprimir(self):
		texto = " ".join(("soy: ", self.nombre, " ; mi rut es: ", self.rut))
		print(texto)