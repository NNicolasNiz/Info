#A)Solicitar al usuario que ingrese números, los cuales se guardarán en una lista. 
#	Finalizar al ingresar el número 0, el cual no debe guardarse.
#B) Solicitar al usuario que ingrese un número y, si el número está en la lista, 
#	eliminar su primera ocurrencia. Mostrar un mensaje si no es posible eliminar.
#C) Recorrer la lista para imprimir la sumatoria de todos los elementos.
#D) Solicitar al usuario otro número y crear una lista con los elementos de la lista original 
#	que sean menores que el número dado. Imprimir esta nueva lista, iterando por ella.
#E) Generar e imprimir una nueva lista que contenga como elementos a tuplas de dos elementos, 
#	cada una compuesta por un número de la lista original y la cantidad de veces que aparece en ella. 
#	Por ejemplo, si la lista original es [5,16,2,5,57,5,2] la nueva lista contendrá: [(5,3), (16,1), (2,2), (57,1)]

n = input("ingrese los numero que desea agregar, para finalizar presione 0")

lista = []

while (n != 0):
	lista.append(n)
	n = input("ingrese los numero que desea agregar, para finalizar presione 0")
print (lista)	