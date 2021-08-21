
from levelstone4 import Contacto, Agenda

def menu():
	print('----MENU-----')
	print('1-agregar Contacto')
	print('2-Buscar Contacto')
	print('3-Modificar')
	print('4-Mostrar')
	print('5-salir')
	return input("opcion: \t")

def agregar(agenda):
	print("-----HOLA VAMOS A CARGAR CONTACTOS----")
	nombre = input("Ingrese el nombre: \t")
	telefono = input("Ingrese el telefono: \t")
	email = input("ingrese el email: \t")
	contacto_nuevo = Contacto(nombre,telefono,email)
	agenda.agregarContacto(contacto_nuevo)

def mostrar(agenda):
	agenda.mostrarContactos()

def buscar(agenda):
	quien = input("que nombre desea buscar?? \t")
	contacto = agenda.buscarContacto(quien)
	if contacto:
		print(contacto.getTelefono())
	else:
		print("NO EXISTE ESE CONTACTO")

def modificar(agenda):
	pass


agenda = Agenda("Mi agenda")

while True:
	op = menu()
	if op == '1':
		agregar(agenda)
	elif op == '2':
		buscar(agenda)
	elif op == '3':
		modificar(agenda)
	elif op == '4':
		mostrar(agenda)
	else:
		break



