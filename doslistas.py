#Escriba un programa que permita crear dos listas de palabras y que, a continuación, escriba las siguientes listas (en las que no debe haber repeticiones):

#Lista de palabras que aparecen en las dos listas.
#Lista de palabras que aparecen en la primera lista, pero no en la segunda.
#Lista de palabras que aparecen en la segunda lista, pero no en la primera.
#Lista de palabras que aparecen en ambas listas.


lista1 =input("ingrese lista 1")
lista2 =input("ingrese lista 2")


lista1 = (list(lista1.split()))
lista2 = (list(lista2.split()))
lista3 = []
lista4 = []
lista5 = []

for x in (lista1):
	if x in (lista2):
		lista3.append(x)
	else:
		lista4.append(x)

for i in  (lista2):
	if i  not in  (lista1):
		lista5.append(i)

print (lista3)
print (lista4)
print (lista5)

	 	

		

