def ciudad (a,b):
	nombre1 = (input("ingrese el nombre de la primer ciudad"))
	nombre2 = (input("ingrese el nombre de la segunda ciudad"))
	a = (input("ingrese el numero reciclado de la primer ciudad"))
	b = (input("ingrese el numero reciclado de la segunda ciudad"))

	if a < b:
		print ("la ciudad mas reciclada es: ", nombre2)
		return b	
	elif a > b:
		print ("la ciudad mas reciclada es: ", nombre1)
		return a
	else:
		print ("las dos son iguales" , nombre1 + " " + nombre2)
		return a 
		return b 


print(ciudad(800,300))






		
				
		
