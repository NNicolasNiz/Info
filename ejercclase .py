# Me permita agregar  la nota de los exámenes, teniendo en cuenta que hay dos módulos.
# Debe tener un menú interactivo que permita:
# 	Mostrar el alumno con mayor promedio
# 	Mostrar todos los que aprobaron ambos módulos
# 	Dado el DNI de un alumno, me muestre sus notas.


def menu():
	print ("1: Cargar un alumno")
	print ("2: Cargar una nota")
	print ("3: listar alumnos")
	print ("4: listar notas de un alumno")
	print ("5: mostrar alumno con mayor promedio")
	print ("6: Mostrar los que aprobaron ambos modulos")
	print ("0: Salir")
	return input()


def CargarAlumno():
    dni =input("ingrese el dni: ")
    if dni in alumnos.keys():
    	print ("Ya existe ese alumno")
    else:
    	nombre = input("ingrese el nombre")
    	localidad = input("ingrese localidad")
    	alu = dict()
    	alu["nombre"] = nombre
    	alu["localidad"] = localidad
    	alu["notasPW"] = list()
    	alu["notasBD"] = list()
    	alumnos[dni] = alu	
    return alumnos

def CargarNota(alumnos):
	if dni in alumnos.keys():
		alu = alumnos[dni]
		print ("vamos a cargar las notas de PW")
		n1 = int(input("ingrese la nota 1"))
		n2 = int(input("ingrese la nota 2"))
		n3 = int(input("ingrese la nota "))
		alu["notasPW"] = [n1, n2, n3]
		print ("vamos a cargar las notas de BD")
		n1 = int(input("ingrese la nota 1"))
		n2 = int(input("ingrese la nota 2"))
		n3 = int(input("ingrese la nota "))
		alu["notasBD"] = [n1, n2, n3]
	else:
		print ("El dni no es valido")

def Listar(alumnos):
	for k,v in alumnos:
		
def MostrarNotasALumno():
	pass

def MayorPromedio():
	pass

def MostrarAprobados():
	pass


def Main():
   print("Welcome")
   alumnos = dict()
   while True:
   	op = menu()
   	if op == "1":
   		alumnos = CargarAlumno(alumnos)
   	elif op == "2":
   		CargarNota()
   	elif op == "3":
   		Listar()
   	elif op == "4":
   	    MostrarNotasALumno()
   	elif op == "5":
   		MayorPromedio()
   	elif op == "6":
   		MostrarAprobados()
   	else:
   		break 

Main()  		
   		

	
   		






		
		