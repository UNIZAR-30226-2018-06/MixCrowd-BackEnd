from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
#clase dbAdapter para interactuar
#con la base de datos, yo usaria alchemy

class DbAdapter:
	
	#funciones
	def mostrar_recomendaciones(idUser):
		#mirar tabla de mas vistos por user
		#tags, categorias y demas

	def anyadir_valoracion(user,valoracion,proyecto):
		#lo del db engine es para conectarse a la base, lo pondremos en marcha mas adelante.
		#el execute te permite hacer sql puro
		db.engine.execute('INSERT INTO ha_valorado VALUES (user,valoracion,proyecto) ON CONFLICT (usuario,proyecto) DO UPDATE SET valoracion = Excluded.valoracion;')
		#ademas de esto hara falta un trigger para que al meter info en
		#la tabla ha valorado, se recalcule la valoracion media del proyecto


	def contar_visitaUser(user,proyecto):	
		#aumentar numero de visitas en 1 en proyecto
		#deberia haber una tabla que guarde user,proyecto,numVecesVisitado
		db.engine.execute('UPDATE ha_visitado SET numVeces=numVeces+1 WHERE ha_visitado.user=user AND ha_visitado.proyecto=proyecto;')
		#es necesario tambien un trigger que actualice el numero de visitas totales al proyecto
		#aunque igual se puede apanyar algo, la consulta de abajo hace exactamente esto

	def contar_visita(proyecto):
		db.engine.execute('UPDATE proyecto SET numVisitas=numVisitas+1 WHERE proyecto.nombre=proyecto;')
	
	def mejor_valorados():
		#mostrar los proyectos mejor valorados,p.e. 100
		#no se si esto chutara pero es la idea jajajajaja
		res=db.engine.execute('SELECT * FROM proyecto ORDER BY valoracion DESC LIMIT 100;')	
		return res

	def mas_visitados():	
		#mostrar los proyectos mas visitados,p.e. 100
		res=db.engine.execute('SELECT * FROM proyecto ORDER BY numVisitas DESC LIMIT 100;')

	def es_publico(idPropio,idProyecto):
		#si no es se devuelve null
	
	def es_colaborador(idPropio,idProyecto):
		#si no es se devuelve null
	
	def get_pistas_proyecto(idProyecto):
		#devuelve una lista de listas, Cada
		#[ [id,Audio,Panning,Instante],[],..]
	
	def buscar_proyecto(proyecto):
		#na

	def buscar_usuario(user):
		#na

	def buscar_amigos(user):
		#na