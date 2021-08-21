#construya un agoritmo que la sea capaz de encontrar todas las cifras de 
for x in range (100,1000):
	c = x // 100
	d = (x // 10) % 10
	u = x % 10
	if (c**3 + d**3 + u**3 ) == x:
		print ("uno de los numeros es: ", x)