alumnos = dict()

op = input("Desea cargar alumno? prisione SI o NO")

while op.lower() == "si":
	nya = input("ingrese nombre y apellido")
	nota = int(input("ingrese la nota"))
	alumnos[nya] = nota

	op = input("Desea cargar alumno? prisione SI o NO")

for k,v in alumnos.items():
	print ("el alumno es: " ,k, "su no es: ", v )



