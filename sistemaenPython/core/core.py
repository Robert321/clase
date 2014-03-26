from objects.Persona import Persona
class Principal():
	def mostrarMenu(self):
		print "(1) Guardar Registro"
		print "(2) Borrar Registro"
		print "(3) Salir"
	def crearRegistroNuevo(self):
		print "Ingrese el nombre"
		nombre=raw_input()
		print "Ingrese el Apellido"
		apellido=raw_input()
		print "Ingrese la edad"
		edad=raw_input()
		print "Desea Guardar los datos s/n"
		opcion=raw_input()
		if(opcion=="s"):
			p=Persona(nombre,apellido,edad)
			p.guardar()
			print "Informacion guardada!"
			raw_input()
			self.mostrarMenu()
			self.accion()
	def accion(self):
		opcion=raw_input()
		if(opcion=="1"):
			self.crearRegistroNuevo()
		elif(opcion=="2"):
			self.borrarRegistro()
		else:
			exit()
	def borrarRegistro(self):
		print"Borrar Registro"
	def __init__(self):
		self.mostrarMenu()
		self.accion()