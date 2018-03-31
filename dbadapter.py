from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
#clase dbAdapter para interactuar
#con la base de datos, yo usaria alchemy

class DbAdapter:
	
	#funciones
	def mostrar_recomendaciones(idUser):
		#mirar tabla de mas vistos por user
		#tags, categorias y demas

	def anyadir_valoracion(valoracion,proyecto):
		#anyadir valoracion a un proyecto
	
	def contar_visita(user,proyecto):	
		#aumentar numero de visitas en 1 en proyecto

	def contar_visitaUser(user,proyecto):
		#registrar que el user ha visto un proyecto

	def mejor_valorados():
		#mostrar los proyectos mejor valorados,p.e. 100

	def mas_visitados():	
		#mostrar los proyectos mas visitados,p.e. 100