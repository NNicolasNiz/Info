class Vehiculo:
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

	def getColor(self):
		return self.color
	def setColor(self, c):
		self.color = c
	def getRuedas(self):
		return self.ruedas
	def setRuedas(self, r):
		self.ruedas = r
		



		


class Coche(Vehiculo):
	def __init__(self, velocidad, cilindrada, color ,ruedas = 4):
		self.velocidad = velocidad
		self.cilindrada= cilindrada
		super().__init__(color,ruedas)


	def getVelocidad(self):
		return self.velocidad
	def setVelocidad(self, vel):
		self.velocidad = vel
	def getCilindrada(self):
		return self.cilindrada
	def setRuedas(self, cil):
		self.cilindrada = cil  	



	  




class Camioneta(Coche):
	def __ini__ (self, carga, velocidad, cilindrada , color , ruedas = 4):
		self.carga = carga
		super().__init__(velocidad , cilindrada, color, ruedas)

	def  getCarga (self):
		return self.carga
	def setCarga (self, carga):
		self.carga = setCarga

		

class Bicicleta(Vehiculo):
	def __init__(color, ruedas, tipo)
	self.tipo = tipo
	super().__init__(color, ruedas)

	def getTipo(self):
		return self.tipo
	def setTipo(self, tipo):
		self.tipo = setTipo 
		









# c = Coche(150,200, "rojo",4)

# print(c.getColor())		


# lista_autos = list()

# for x in range (3):
# 	print ("Vamos a cargar 5 autos")
# 	color = input("ingrese el color")
# 	velocidad = input ("ingrese la velocidad")
# 	cilindrada = input("ingrese la cilindrada")
# 	nuevo = Coche(velocidad, cilindrada, color)
# 	lista_autos.append(nuevo)

# for x in lista_autos:
# 	print(f"el color de este auto es {x.getColor()}.... ")
