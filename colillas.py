total = 0
menos = 0
igual = 0
mayor = 0


for i in range (1,11):
	cantidad = int(input("ingrese cantidad de colillas encontradas: "))
	total += cantidad
	if cantidad < 100:
		menos += 1 
	elif cantidad < 200:
		igual +=1
	else:
		mayor +=1 
		 
print ("el porcentaje de menos de 100 colillas es: ",(menos / i) * 100)
print ("el porcentaje entre 100 y 200 colillas es: ",(igual / i) * 100)
print ("el porcentaje de mayores de 200 colillas es: ",(mayor / i) * 100)
print ("el total de colillas recolectas son : ", total)