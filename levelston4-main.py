from levelston4 import Contacto, Agenda

def menu():
	print ("--------inicio menu--------")
	print ("1- Agregar Contacto")
	print ("2- Buscar Contacto")
	print ("3-  Mostrar Contactos")
	print ("4- Modificar Contacto")
	print ("5- Salir")
	return input("opcion: ")

def agregarContacto(agenda):
	print("vamos a cargar contactos")
	nombre = input("Ingrese Nombre")
	telefono = input ("Ingrese Telefono")
	email = input("ingrese Email")
	contacto_nuevo = Contacto(nombre, telefono, email)
	agenda.agregarContacto(contacto_nuevo)


def buscarContacto(agenda):
	quien = input("ingrese el nombre que quiere buscar")
	contacto = agenda.buscarContacto(quien)
	if contacto:
		print (contacto.getTelefono())
	else:
		print ("no existe")

def mostrarContactos(agenda):
	agenda.mostrarContactos()

agenda = Agenda("celu")

while True:
	op = menu()
	if op == "1":
		agregarContacto(agenda)
	elif op == "2":
		buscarContacto(agenda)
	elif op == "3":
		mostrarContactos(agenda)
	else:
		break 







    	



