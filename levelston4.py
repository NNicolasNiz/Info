# Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.
# Además deberá mostrar un menú con las siguientes opciones.

# Añadir contacto

# Lista de contactos

# Buscar contacto

# Editar contacto

# Cerrar agenda


class Contacto:
	def __init__(self, nombre, telefono, email):
		self.__nombre = nombre
		self.__telefono = telefono
		self.__email = email


	def getNombre (self):
		return f'Mi nombre es: {self.__nombre}'

	def setNombre (self, n):
		self.__nombre = n 

	def getTelefono (self):
		return f'Mi telefono es: {self.__telefono}'

	def setTelefono (self, t ):
		self.__telefono = t
	
	def getEmail (self):
		return f'Mi Email es: {self.__email}'

	def setEmail (self, e ):
		self.__email = e 
	
	def soyYO (self, nombre):
		if self.__nombre == nombre:
			return True
		else:
			return False


class agenda:
	def __init__ (self, nombre):
		self.__nombre = nombre
		self.__contactos = list()


	def agregarContacto (self, c):
		self.__contactos.append(c)

	def mostrarContactos(self):
		print ("------Bienvenido-------")
		for c in self.__contactos:
			print (f'Contactos:\n {c.getNombre()} \n {c.getTelefono()}\n {c.getEmail()}')

			

		

		

			

