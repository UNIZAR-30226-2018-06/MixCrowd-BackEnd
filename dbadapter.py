from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
#clase dbAdapter para interactuar
#con la base de datos, yo usaria alchemy

class DbAdapter:
	engine=create_engine('postgresql://admin:1234@localhost:2223/practica1')
	#funciones
	def mostrar_recomendaciones(idUser):
		#mirar tabla de mas vistos por user
		#tags, categorias y demas
		res=db.engine.execute('SELECT DISTINCT p.nombre, p.valoracion FROM proyecto p, etiqueta e WHERE e.proyecto_nombre=p.nombre AND e.categoria IN (SELECT t1.etiqueta FROM (SELECT t.etiqueta, t.suma FROM (SELECT e.categoria etiqueta, SUM(v.valor) suma FROM valoracion v, etiqueta e WHERE v.usuario_nombre=idUser AND v.proyecto_nombre=e.proyecto_nombre GROUP BY e.categoria) t ORDER BY suma DESC LIMIT 5) t1) ORDER BY p.valoracion DESC LIMIT 100;')
		return res

	def anyadir_valoracion(user,valoracion,proyecto):
		#lo del db engine es para conectarse a la base, lo pondremos en marcha mas adelante.
		#el execute te permite hacer sql puro
		db.engine.execute('INSERT INTO valoracion VALUES (proyecto,user,valoracion) ON CONFLICT (usuario,proyecto) DO UPDATE SET valoracion = Excluded.valoracion;')
		#ademas de esto hara falta un trigger para que al meter info en
		#la tabla ha valorado, se recalcule la valoracion media del proyecto

	def contar_visitaUser(user,proyecto):	
		#aumentar numero de visitas en 1 en proyecto
		#deberia haber una tabla que guarde user,proyecto,numVecesVisitado
		db.engine.execute('INSERT INTO visita VALUES (proyecto,user,NULL);')
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
		








		return res

	def es_administrador(idPropio,idProyecto):
		#saber si un user es administrador de un proyecto
		res=db.engine.execute('SELECT administrador FROM proyecto where nombre=idProyecto;')
		if idProyecto=idPropio
			return true
		else
			return false	

	def es_publico(idProyecto):
		#si es publico devuelve true, si no devuelve false
		res=db.engine.execute('SELECT privacidad FROM proyecto WHERE nombre=idProyecto;')
		return res
	
	def es_colaborador(idPropio,idProyecto):
		#devuelve true si idPropio es colaborador del proyecto idProyecto
		res=db.engine.execute('SELECT EXISTS (SELECT TRUE FROM colabora WHERE proyecto_nombre=idProyecto AND usuario=idPropio );')
		return res
	
	def get_pistas_proyecto(idProyecto):
		#devuelve una lista de pistas, Cada
		#[ [id,Audio,Panning,Instante],[],..]
		res=db.engine.execute('SELECT p.nombre, p.fecha, p.audio FROM pista p WHERE p.proyecto_nombre=idProyecto;')
		return res

	def buscar_proyecto(proyecto):
		#busca un proyecto
		res=db.engine.execute('SELECT * FROM proyecto WHERE nombre=proyecto AND privacidad='t';')
		return res

	def buscar_usuario(user):
		#na
		res=db.engine.execute('SELECT * FROM usuario WHERE nombre=user;')
		return res

	def buscar_amigos(user):
		#na
		res=db.engine.execute('SELECT usuario_2 FROM amistad WHERE usuario_1=user;')
		return res
