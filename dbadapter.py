from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
#clase dbAdapter para interactuar
#con la base de datos, yo usaria alchemy
import json
import psycopg2
from psycopg2.extras import RealDictCursor

conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
cur = conn.cursor()

class DbAdapter:
	"""
	#funciones
	def mostrar_recomendaciones(idUser):
		#mirar tabla de mas vistos por user
		#tags, categorias y demas
		res=db.engine.execute('SELECT DISTINCT p.nombre, p.valoracion FROM proyecto p, etiqueta e WHERE e.proyecto_nombre=p.nombre AND e.categoria IN (SELECT t1.etiqueta FROM (SELECT t.etiqueta, t.suma FROM (SELECT e.categoria etiqueta, SUM(v.valor) suma FROM valoracion v, etiqueta e WHERE v.usuario_nombre=idUser AND v.proyecto_nombre=e.proyecto_nombre GROUP BY e.categoria) t ORDER BY suma DESC LIMIT 5) t1) ORDER BY p.valoracion DESC LIMIT 100;')
		return res

	def anyadir_valoracion(user,valoracion,proyecto):
		#lo del db engine es para conectarse a la base, lo pondremos en marcha mas adelante.
		#el execute te permite hacer sql puro
		cur.execute('INSERT INTO valoracion VALUES (proyecto,user,valoracion) ON CONFLICT (usuario,proyecto) DO UPDATE SET valoracion = Excluded.valoracion;')
		conn.commit()
		#ademas de esto hara falta un trigger para que al meter info en
		#la tabla ha valorado, se recalcule la valoracion media del proyecto

	def contar_visitaUser(user,proyecto):	
		#aumentar numero de visitas en 1 en proyecto
		#deberia haber una tabla que guarde user,proyecto,numVecesVisitado
		cur.execute('INSERT INTO visita VALUES (proyecto,user,NULL);')
		conn.commit()
		#es necesario tambien un trigger que actualice el numero de visitas totales al proyecto
		#aunque igual se puede apanyar algo, la consulta de abajo hace exactamente esto

	def contar_visita(proyecto):
		cur.execute('UPDATE proyecto SET numVisitas=numVisitas+1 WHERE proyecto.nombre=proyecto;')
		conn.commit()
	def mejor_valorados():
		#mostrar los proyectos mejor valorados,p.e. 100
		#no se si esto chutara pero es la idea jajajajaja
		res=cur.execute('SELECT * FROM proyecto ORDER BY valoracion DESC LIMIT 100;')	
		return res

	def mas_visitados():	
		#mostrar los proyectos mas visitados,p.e. 100
		cur.execute('SELECT * FROM proyecto ORDER BY numVisitas DESC LIMIT 100;')
		return res

	def es_administrador(idPropio,idProyecto):
		#saber si un user es administrador de un proyecto
		res=cur.execute('SELECT administrador FROM proyecto where nombre=idProyecto;')
		if idProyecto=idPropio
			return true
		else
			return false	

	def es_publico(idProyecto):
		#si es publico devuelve true, si no devuelve false
		res=cur.execute('SELECT privacidad FROM proyecto WHERE nombre=idProyecto;')
		return res
	
	def es_colaborador(idPropio,idProyecto):
		#devuelve true si idPropio es colaborador del proyecto idProyecto
		res=db.engine.execute('SELECT EXISTS (SELECT TRUE FROM colabora WHERE proyecto_nombre=idProyecto AND usuario=idPropio );')
		return res
	


	def buscar_proyecto(proyecto):
		#busca un proyecto
		res=cur.execute('SELECT * FROM proyecto WHERE nombre=proyecto AND privacidad='t';')
		return res

	def buscar_usuario(user):
		#na
		res=cur.execute('SELECT * FROM usuario WHERE nombre=user;')
		return res

	def buscar_amigos(user):
		#na
		res=cur.execute('SELECT usuario_2 FROM amistad WHERE usuario_1=user;')
		return res
		"""
	def traer_estilos(self,proyecto):
		cur.execute("SELECT categoria FROM etiqueta WHERE proyecto_nombre=%s",(proyecto,))
		return json.dumps(cur.fetchall(), default=str)	

	
	def buscar_proyectos(self):
		#na
		#"SELECT * FROM proyecto WHERE correo=%s",(email,)
		cur.execute("SELECT * FROM proyecto WHERE administrador='dario';")
		return json.dumps(cur.fetchall(), default=str)	
	
	def traer_proyecto(self, proyecto):
		#na
		#"SELECT * FROM proyecto WHERE correo=%s",(email,)
		cur.execute("SELECT * FROM proyecto WHERE nombre=%s",(proyecto,))
		return json.dumps(cur.fetchall(), default=str)	
	
	def borrar_proyecto(self, proyecto):
		#na
		#"SELECT * FROM proyecto WHERE correo=%s",(email,)
		cur.execute("DELETE FROM proyecto WHERE nombre=%s",(proyecto,))
		conn.commit()
		#return json.dumps(cur.fetchall(), default=str)	
		
	def set_pistas_proyecto(self,nombre,idProyecto,audio,instante,duracion,panning):
		#Inserta una nueva pista al proyecto idProyecto con la información proporcionada
		cur.execute('INSERT INTO pista VALUES (nombre,idProyecto,NULL,DEFAULT,instante,duracion,panning);')
		conn.commit()
			
	def get_pistas_proyecto(self,idProyecto):
		#devuelve una lista de pistas, Cada
		#[ [id,Audio,Panning,Instante],[],..]
		cur.execute("SELECT p.nombre, p.fecha, p.audio FROM pista p WHERE p.proyecto_nombre=%s",(proyecto,))
		return json.dumps(cur.fetchall(), default=str)	
		
	def mas_visitados():	
		#mostrar los proyectos mas visitados,p.e. 100



		cur.execute('SELECT * FROM proyecto ORDER BY numVisitas DESC LIMIT 100;')
		return json.dumps(cur.fetchall(), default=str)
