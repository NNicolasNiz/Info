
#Determinar si todos los alumnosde un curso reprueba, 
#sabiendo que aprobara si su promedio de tres calificaciones es mayor o igual a 70; desaprueba en caso contrario.
#CANTIDAD ALUMNOS
#CANTIDAD DE ALUMNOS QUE APROBARON
#CANTIDAD DE ALUMNOS QUE DESAPROBARON
#PROMEDIO GENERAL DE TODO EL CURSO

cantidad_total = 0
cantidad_aprobados = 0
cantidad_desaprobados = 0
promedio_general = 0

opcion = "si"
while (opcion == "si"):
	nota1 = int(input("Ingrese la nota numero 1: \t"))
	nota2 = int(input("Ingrese la nota numero 2: \t"))
	nota3 = int(input("Ingrese la nota numero 3: \t"))

	promedio = (nota1 + nota2 + nota3)/3

	if promedio >= 70 :
		cantidad_aprobados = cantidad_aprobados + 1
		print(cantidad_aprobados)
		print("Aprobo el curso con un promedio de: ", round(promedio,2))
	else:
		cantidad_desaprobados = cantidad_desaprobados + 1
		print("Desaprobo el curso")

	promedio_general = promedio_general + promedio
	cantidad_total = cantidad_total + 1
	
	opcion = input("QUIERE CARGAR UN NUEVO ALUMNO??").lower()


promedio_final = promedio_general / cantidad_total
print("------------------------------------------------------")
print("LA CANTIDAD DE ALUMNOS PROCESADOS ES DE:\t", cantidad_total)
print("LA CANTIDAD DE ALUMNOS ARPOBADOS ES DE:\t", cantidad_aprobados)
print("LA CANTIDAD DE ALUMNOS DESAPROBADOS ES DE:\t", cantidad_desaprobados)
print("EL PROMEDIO GENERAL ES DE:\t", promedio_final)
print("------------------------------------------------------")
print("GRACIAS POR USAR NUESTRO SISTEMA")