# Un supermercado maneja el catálogo de los productos que vende. 
# De cada producto se conoce su nombre, precio, y si el mismo es
#  parte del programa Precios Cuidados o no. 
#  Por defecto, el producto no es parte del programa, 
#  a menos que se especifique lo contrario.

# Para ayudar a los clientes, el supermercado quiere realizar
#  descuentos en productos de Primera Necesidad.
#  Es por eso que al calcular el precio de un producto de
#   Primera Necesidad, se aplica un descuento del 10%. Es decir:


# precioProductoPrimeraNecesidad = precioBaseDelProducto * 0.9
# El supermercado, del cual se conoce el nombre y la dirección,
#  desea conocer la cantidad total de productos que comercializa y 
#  la suma total de los precios de los mismos.

class Producto():
	def __init__ (self, nombre, precio, precio_cuidado = None):
		self.nombre =nombre
		self.precio = precio
		self.precio_cuidado = precio_cuidado
		self.primera_necesidad = None
		self.EsPrimeraNecesidad()


		def getNormbre (self):
			return f'El nombre del producto es: {self.nombre}'

		def getPrecio (self):
			return f'su precio es: {self.precio}'


		def EsPrimeraNecesidad(self):
			ListaPrimeraNecesidad = ['leche', 'Papel', 'Queso']



			