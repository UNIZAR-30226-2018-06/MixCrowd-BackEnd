from flask import Flask
from dbadapter import DbAdapter

# clase recomendador, para hacer recomendaciones personalizadas
# a cada uno de los usuarios del sistema

class RecomNOAUT:
	#hemos pensado cascar aqui un adapter
	#para hacer las llamadas
	adapter=DbAdapter()
	#funciones
	
	#Mostrar proyectos mejor valorados	
	def mejor_valorados():
		return adapter.mejor_valorados()

	#Contar visitas a un proyecto,
	#independientemente del usuario	
	def contar_visita(proyecto):
		adpter.sumar_visita(proyecto)	

	def mas_visitados():
		return adapter.mejor_valorados()	