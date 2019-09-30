#!/usr/bin/python3

# guardar en la carpeta del proyecto
# E:\laragon\www\DWY4001_HelloWorld
# con el nombre 'functions_example.py'

# las funciones en python se definen con def :

def stupid_function(name):
	separator = " "
	message = separator.join(("Oh", name, "is an asshole"))
	print(message)

# una funcion un poco mas compleja: calculo del digito
# verificador de un rut chileno.
def digito_verificador(rut):
	digito = ""
	contador = 2
	suma = 0
	multiplo = 0
	while rut > 0:
		multiplo = ( rut % 10 ) * contador
		suma = suma + multiplo
		rut	= rut // 10 # division entera!
		contador = contador + 1 
		if contador == 8 :
			contador = 2
	digito = 11 - (suma % 11)
	if digito == 11 :
		digito = 0
	if digito == 10 :
		digito = 'K'
	return str(digito)

mi_rut = 20468488
print("-".join((str(mi_rut), digito_verificador(mi_rut))))

# y llamamos a la funcion...
stupid_function("Daniel Montero")
stupid_function("Seba")

# Para que los cambios se guarden en github master...
# git add functions_example.py
# git commit -m "Updating functions example"
# git checkout master
# git pull
# git merge dm_ejemplo_funciones
# git push