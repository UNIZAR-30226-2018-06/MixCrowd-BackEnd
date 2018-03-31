from flask import Flask
from dbadapter import DbAdapter

# clase recomendador, para hacer recomendaciones personalizadas
# a cada uno de los usuarios del sistema

class RecomAUT:
	#hemos pensado cascar aqui un adapter
	#para hacer las llamadas
	adapter=DbAdapter()

	#funciones
	#funcion para mostrar las recomendaciones concretas
	#del usuario con ID idUser.
	def mostrar_recomendaciones(idUser):
		adapter.mostrar_recomendaciones(idUser)
	
	#funcion para anaydir una valoracion
	# a un poryecto	
	def anyadir_valoracion(valoracion,proyecto):
		adapter.anaydir_valoracion(valoracion,proyecto)
	#contar una visita de un user concreto
	#a un proyecto. Hay que tenerlo en cuenta
	#en las recomendaciones.	
	def contar_visitaUser(user,proyecto):
		#query del id del proyecto
		#incrementar visitas del proyecto
		adapter.contar_visitaUser(user,proyecto)