
#
contrania_real = '1234'
usuario_real = 'nico'


intentos = 5
logueado = False
while (intentos > 0):
	usuario = input("ingrese usuario:\t")
	pss = input("ingrese contraseña:\t")
	if pss == contrania_real and usuario == usuario_real:
		logueado = True
		intentos = 0
	else:
		intentos -= 1
		print("contraseña incorrecta, le quedan solamente: ",intentos," intentos")



if logueado == False:
	print("PERDIO TODOS LOS INTENTOS")
else:
	print("SE LOGUEO CORRECTAMENTE!!!!")

