# CASO 4
# Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email.
# Además deberá mostrar un menú con las siguientes opciones.

# Añadir contacto

# Lista de contactos

# Buscar contacto

# Editar contacto

# Cerrar agenda


#Contacto = list()

# class Contacto:
# 	def __init__ (self, nombre, telefono, email):
# 		self.nombre = nombre
# 		self.telefono = telefono
# 		self.email = email


# 	def getNombre (self):
# 		return f"mi nombre es: {self.__nombre}"

# 	def setNombre (self, nuevoNombre):
# 		self.__nombre = nuevoNombre

# 	def getTelefono (self):
# 		return f"mi telefono es: {self.__telefono}"

# 	def setTelefono (self, nuevoTelefono):
# 		self.__telefono = nuevoTelefono

# 	def getEmail(self):
# 		return f"mi email es: {self.__email}"

# 	def setTelefono (self, nuevoEmail):
# 		self.__email = nuevoEmail

# 	def soyYo (self, nombre):
# 		if nombre == __nombre:
# 			True 
# 		else:
# 			False 



# class Agenda:
# 	def __init__(self, nombre):
# 		self.nombre = nombre
# 		self.__contactos = list()


#     def agregarContacto(self, c):
#     	self.__contactos.append(c)

#     def mostrarContactos (self):
#     	print ("----------inicio--------")
#     	for c in self.__contactos:
#     		print (f"contacto:{c.getNombre()} {c.getTelefono()} {c.getEmail()}")
#     		print ("-------fin------")


#     def buscarContacto(self, nombre):
#     	for c in self.__contactos:
#     		if soyYo(nombre):
#     			return c 


    	




			

		



class Contacto():
	def __init__(self,nombre,telefono,email):
		self.__nombre = nombre
		self.__telefono = telefono
		self.__email = email

	def getNombre(self):
		return f'Mi nombre es:{self.__nombre}'

	def setNombre(self,nuevoNombre):
		self.__nombre = nuevoNombre

	def getTelefono(self):
		return f'Mi telefono es:{self.__telefono}'

	def setTelefono(self,nuevoTelefono):
		self.__telefono = nuevoTelefono

	def getEmail(self):
		return f'Mi Email es:{self.__email}'

	def setEmail(self,nuevoEmail):
		self.__email = nuevoEmail

	def soyYO(self,nombre):
		if self.__nombre == nombre:
			return True
		else:
			return False


class Agenda():
	def __init__(self,nombre):
		self.__nombre = nombre
		self.__contactos = list()

	def agregarContacto(self, c):
		self.__contactos.append(c)

	def mostrarContactos(self):
		print('----------INICIO------------')
		for c in self.__contactos:
			print(f'Contaco: \n {c.getNombre()} \n {c.getTelefono()} \n {c.getEmail()}')
		print('----------FIN------------')

	def buscarContacto(self,nombre):
		for c in self.__contactos:
			if c.soyYO(nombre):
				return c

		





		








		

