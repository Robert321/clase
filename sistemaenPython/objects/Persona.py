import datetime
class Persona():
	nombre=""
	apellido=""
	edad=0
	__fechanacimiento=0
	def __init__(self,nom,app,edad):
		self.nombre=nom
		self.apellido=app
		self.edad=edad
		print "Se ha creado la instancia persona"
	def cambiarnombre(self,nom):
		self.nombre=nom
	def guardar(self):
		nombre="%s_%s.txt"%(self.nombre,datetime.datetime.now().day)
		ruta="Registros/%s"%(nombre)
		archivo=open(ruta,"w+")
		archivo.write("Nombre %s"%(self.nombre))
		archivo.write("Apellido %s"%(self.apellido))
		archivo.write("Edad %s"%(self.edad))
		archivo.close()