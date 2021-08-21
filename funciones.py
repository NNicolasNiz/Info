import time
def sumar (a,b):
	r = a + b
	return r
def restar(a,b):	
	r = a - b
	return r 
def multiplicar(a,b):
	r = a * b
	return r 
def dividir(a,b):
	r = a / b 
	return r 
def menu():
	print ("--------------MENU------------")
	time.sleep(10)
	print("SELECCIONE LA OPERACION QUE DESEE REALIZAR ")
	print ("1-SUMAR, 2 RESTAR, 3 MULTIPLICAR, 4 DIVIDIR, 5 SALIR")
	op = input()
	return op
operacion = menu()

while operacion != "5":
	if operacion == "5":
		break
	n1 = int(input("INGRESE EL PREMER VALOR"))
	n2 = int(input("INGRESE EL SEGUNDO VALOR"))
	if operacion == "1":
		r = sumar(n1,n2)
	elif operacion == "2":
		r = restar(n1,n2)
	elif operacion == "3":
		r = multiplicar(n1,n2)
	elif operacion == "4":
		r =  dividir(n1,n2)
	else:
		print ("NO INGRESO UNA OPCION VALIDA")
	print ("EL RESULTADO DE LA OPERACION ES: ", r )
	operacion = menu()	

		

		



