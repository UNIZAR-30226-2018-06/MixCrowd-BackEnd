from flask import Flask
from dbadapter import DbAdapter
import json

# clase para realizar busquedas tanto de users como
# de proyectos.

class Buscador:
	
	#funciones
	def buscar_p_usuario(self,idUser):
		adapter=DbAdapter()
		ans=adapter.buscar_proyectos(idUser)
		print(ans)
		return ans 
	def traer_proyecto(self,proyecto):
		adapter=DbAdapter()
		return adapter.traer_proyecto(proyecto)
	
	def buscar_proyecto(proyecto):
		return adapter.buscar_proyecto(proyecto)

	def buscar_usuario(user):
		adpter.buscar_usuario(user)	

	def buscar_amigos(user):
		return adapter.buscar_amigos(user)

	def buscarB(self,search):
		adapter=DbAdapter()
		p=adapter.buscador(search)
		with open('info.txt', 'a') as the_file:
                    the_file.write(p)
		return p 	

	def buscarU(self,search):
		adapter=DbAdapter()
		p=adapter.buscadorU(search)
		return p 	
	def get_valoracion_usuario(self,idProject,idUser):
		adapter=DbAdapter()
		return adapter.get_valoracion_usuario(idProject,idUser)	

	def get_carousel_principal(self):
		adapter=DbAdapter()
		return adapter.mas_visitados()

	def	get_carousel_user1(self):
		adapter=DbAdapter()
		return adapter.mejor_valorados()

	def	get_carousel_user2(self):
		adapter=DbAdapter()
		return adapter.mas_comentados()

	def	get_carousel_user_recomendado(self,idUser):
		adapter=DbAdapter()
		return adapter.mostrar_recomendaciones(idUser)