'''
A)Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. 
	Finalizar al ingresar el número 0, el cual no debe guardarse.
B) Solicitar al usuario que ingrese un número y, si el número está en la lista, 
	eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original 
	que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, 
	cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 
	Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]
'''
### FUNCIONES

def menu():
	print(" MENU ")
	print(" A:Cargar lista")
	print(" B:Eliminar primera ocurrencia")
	print(" C:Mostrar Sumatoria")
	print(" D:Generar lista con valores menores al ingresado")
	print(" E:Generar tupla con ocurrencias de cada valor")
	print(" ingrese cualquier otra letra para salir")
	return input()
	
def A(lista_numeros):
	numero = int(input("INGRESE un Numeros, y si quiere finalizaringrese 0: "))
	while numero != 0:
		lista_numeros.append(numero)
		numero = int(input("INGRESE un Numeros, y si quiere finalizaringrese 0: "))

	return lista_numeros

def B(lista_numeros):
	eliminar = int(input("Ingrese el valor que desa eliminar: "))

	if eliminar in lista_numeros:
		lista_numeros.remove(eliminar)
	else:
		print("no se puede eliminar el valor ingresado, ya que el mismo no se encuentra en la lista: ")

	return lista_numeros

def C(lista_numeros):
	suma = 0
	for elto in lista_numeros:
		suma += elto
	print("La suma de los elementos de la lista es igual a: ", suma)


def D(lista_numeros):
	nuevo = int(input("ingrese un numero: "))
	nueva_lista = list()
	for elto in lista_numeros:
		if elto < nuevo:
			nueva_lista.append(elto)

	for elto in nueva_lista:
		print(elto, end=" ")

def E(lista_numeros):
	nueva = list()
	for elto in lista_numeros:
		tupla = (elto,lista_numeros.count(elto))
		if tupla not in nueva:
			nueva.append(tupla)

	print(nueva)


### PROGRAMA

numeros = list()
while True:
	op = menu()
	if op.lower() == 'a':
		numeros = A(numeros)
	elif op.lower() == 'b':
		numeros = B(numeros)
	elif op.lower() == 'c':
		C(numeros)
	elif op.lower() == 'd':
		D(numeros)
	elif op.lower() == 'e':
		E(numeros)
	else:
		break
	print("LA LISTA TIENE ESTOS VALORES: ",numeros)




