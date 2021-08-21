x = int(input("ingrese numero a evaluar"))

for i in range(1,x+1):
	if x % i == 0:
		print (i, end= "/ ")
		