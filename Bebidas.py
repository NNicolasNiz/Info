# En un depósito se guardan las bebidas a comercializar.

# Estos productos son bebidas como agua mineral y gaseosas. 

# De los productos nos interesa saber su identificador (cada uno tiene uno distinto), cantidad de litros, precio y marca.

# Si es agua mineral nos interesa saber también el origen (Manantial, Ciudad, etc).

# Si es una gaseosa queremos saber el porcentaje que tiene de azúcar y si tiene o no alguna promoción (si la tiene tendrá un descuento 
#del 10% en el precio).

# Las operaciones del almacén son las siguientes:

# Calcular precio de todas las bebidas: calcula el precio total de todos los productos del almacén.

# Calcular el precio total de una marca de bebida: dada una marca, calcular el precio total de esas bebidas.

# Agregar producto: agrega un producto, si el identificador esta repetido en alguno de las bebidas, no se agregará esa bebida.

# Eliminar un producto: dado un ID, eliminar el producto del depósito.

# Mostrar información: mostramos para cada bebida toda su información.



class bebida:
	def __init__ (self, id, ca_litros, precio, marca):
		self.__id = id 
		self.__ca_litros = ca_litros
		self.__precio = precio
		self.__marca = marca

	def getPrecio (self):
		return self.__precio

	def ver_info(self):
		print ("ID: %s" % (self.__id))
		print ("Cantidad de litros: %s" % (self.__ca_litros))
        print ("Precio : %s" % (self.__precio))
        pritn ("Marca %s" % (self.__marca))



class aguaMineral(bebida):
	def __init__ (self,id, ca_litros, precio, marca , origen ):
		super().__init__(id , ca_litros, precio, marca)
		self.__origen = origen


	def ver_info():
		super().ver_info()
		pritn ("Es de Origen %s" % (self.__origen))


class Gaseosa (bebida):
	def __init__ (self , id, ca_litros, precio, marca,p_azucar, tiene_desc ):
		super().__init__(id, ca_litros, precio, marca)
		self.__p_azucar = p_azucar
		self.__tiene_desc = tiene_desc
		self.__descuento = 0.1


	def getPrecio():
		if self.__precio:
			return self.__precio *(1 - self.__descuento)
		else:
			return self.__precio



	def ver_info():
		super().ver_info()
		print("El porcentage de azucar es: %s" % (self.__p_azucar))
		if tiene_desc:
			print("El descuento es: ")

		
		




		




		
		