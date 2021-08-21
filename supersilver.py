# class Producto():
# 	def __init__ (self, nombre, precio, precio_cuidado=None, primera_necesidad=None):
# 		self.nombre = nombre
# 		self.precio = precio
# 		self.precio_cuidado = precio_cuidado
# 		self.primera_necesidad = primera_necesidad

# 	def getNombre (self):
# 		return self.nombre

# 	def setNombre(self, n):
# 		self.nombre = n

# 	def precioCuidado(self):
# 		if precio_cuidado != None:
# 			self.precio = self.precio * 0.9
# 			return self.precio


# class Almacen():
# 	def __init__ (self, nombre, direccion):
# 		self.nombre = nombre
# 		self.direccion = direccion
# 		self.lista_productos = list()

# 	def agregarProductos(self, producto):
# 		self.lista_productos.append(producto)


# 	def sumaPrecio (self):
# 		precio = 0 
# 		for i in self.lista_productos:
# 			precio = precio + i.precio
# 		return precio 
		
# 	def totalProductos (self):
# 		return len(self.lista_productos)

class Producto():
	def __init__(self, nombre, precio, precio_cuidado= None ):
	 self.nombre = nombre
        self.precio = precio
        self.precio_cuidado = precio_cuidado
        self.EsPrecioCuidado()
        self.primera_necesidad = None
        self.EsPrimeraNecesidad()

    
		
	def EsPrimeraNecesidad(self):
		ListaPrimeraNecesidad = ['leche', 'Papel', 'Queso']
		if self.nombre in ListaPrimeraNecesidad:
			self.primera_necesidad = True
			self.precio = self.precio * 0.9











			


Fideos = producto('Fideos', 40)
Carne_Molida = producto('Carne Molida' , 300)
Harina = producto('Harina', 150)
Manteca = producto('Manteca', 120)
Detergente = producto('Detergente', 110)
Dulce_de_leche = producto('Dulce De Leche', 90)


Chino.agregarProducto(Arroz)
Chino.agregarProducto(Fideos)
Chino.agregarProducto(Carne_Molida)
Chino.agregarProducto(Harina)
Chino.agregarProducto(Manteca)
Chino.agregarProducto(Detergente)
Chino.agregarProducto(Dulce_de_leche)
# def EsPrecioCuidado(self):
#         ListaPrecioCuidado = ['Arroz', 'Fideos', 'Dulce de leche']    
#         if self.nombre in ListaPrecioCuidado:
#             self.precio_cuidado = True