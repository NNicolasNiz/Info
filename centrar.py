def centrar (texto,consola=88):
	espacios_totales = (consola - len(texto)) // 2
	espacio_adelante = espacios_totales // 2
	nuevo_texto = ""
	for i in range  (espacio_adelante):
		nuevo_texto+= " "
	nuevo_texto= nuevo_texto + texto
	
	return nuevo_texto
txt = input("ingrese el texto que desea centrar")

print(centrar(txt))		