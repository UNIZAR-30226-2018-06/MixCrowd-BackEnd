from flask import Flask
from flask_sqlalchemy  import SQLAlchemy
#clase dbAdapter para interactuar
#con la base de datos, yo usaria alchemy
import json
import psycopg2
from psycopg2.extras import RealDictCursor
import base64


class DbAdapter:
	
	#funciones
	def mostrar_recomendaciones(self,idUser):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		#mirar tabla de mas vistos por user
		#tags, categorias y demas
		res=cur.execute("SELECT DISTINCT p.nombre,p.fechacreacion,p.fechaultimamod,p.numvisitas,p.imagen,p.privacidad,p.valoracionTotal,p.descripcion,p.administrador FROM proyecto p, etiqueta e WHERE e.proyecto_nombre=p.nombre AND e.categoria IN (SELECT t1.etiqueta FROM (SELECT t.etiqueta, t.suma FROM (SELECT e.categoria etiqueta, SUM(v.valor) suma FROM valoracion v, etiqueta e WHERE v.usuario_nombre=%s AND v.proyecto_nombre=e.proyecto_nombre GROUP BY e.categoria) t ORDER BY suma DESC LIMIT 5) t1) ORDER BY p.valoracionTotal DESC LIMIT 100;",(idUser,))
		ret = json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()
		return ret
	"""
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
	def loguear(self,email,password):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		if email=='' or password=='':
			cur.close()
			conn.close()
			return '0'
		else:
			cur.execute("SELECT contrasena FROM usuario WHERE correo=%s;",(email,))
			if cur.rowcount==0:
				cur.close()
				conn.close()
				return '1'	
			else:
				p =cur.fetchone()[0]
				spaces_added=40-len(password)	
				password=password.ljust(40)
				if p==password:
					cur.close()
					conn.close()
					return '2'

	def signup(self,username,password,email):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		cur.execute("""INSERT INTO usuario(nombre,contrasena,correo) VALUES (%s, %s, %s);""",(username,password,email ))
		conn.commit()
		cur.close()
		conn.close()
	
	#aqui estaria bien mirar si hay uno con el mismo nombre para que no pete
	def insertar_proyecto(self,titulo,descp,imgPro,idUser,privacidad):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		pri=(privacidad[0]=='public')
		with open('info.txt', 'a') as the_file:
                    the_file.write(str(privacidad))
		cur.execute("""INSERT INTO proyecto(nombre,fechaCreacion,fechaUltimaMod,numVisitas,imagen,privacidad,valoracionTotal,descripcion,administrador) VALUES (%s, DEFAULT, DEFAULT, %s, %s, %s, %s, %s, %s);""",    (titulo,'0',imgPro,pri,'0',descp,idUser))
		#cur.execute("""INSERT INTO etiqueta(categoria,proyecto_nombre) VALUES (%s, %s);""", (stl,titulo))
		conn.commit()
		cur.close()
		conn.close()
	
	def insertar_estilo(self,idProyecto,estilo):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()		
		cur.execute("""INSERT INTO etiqueta(categoria,proyecto_nombre) VALUES (%s, %s);""", (estilo,idProyecto))
		conn.commit()
		cur.close()
		conn.close()

	def traer_estilos(self,proyecto):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()		
		cur.execute("SELECT categoria FROM etiqueta WHERE proyecto_nombre=%s",(proyecto,))
		ret = json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()
		return ret
	
	def buscar_proyectos(self,idUser):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		#na
		#"SELECT * FROM proyecto WHERE correo=%s",(email,)
		cur.execute("SELECT * FROM proyecto WHERE administrador=%s",(idUser,))
		ret = json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()
		return ret	
	
	def traer_proyecto(self, proyecto):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur1 = conn.cursor()
		cur2= conn.cursor()
		#na
		#"SELECT * FROM proyecto WHERE correo=%s",(email,)
		cur1.execute("SELECT * FROM proyecto WHERE nombre=%s",(proyecto,))
		cur2.execute("SELECT categoria FROM etiqueta WHERE proyecto_nombre=%s",(proyecto,))
		# ret1 = json.dumps(cur1.fetchall(), default=str)
		# ret2= json.dumps(cur2.fetchall(), default=str)
		#ret=+ret1
		ret=cur1.fetchall()+cur2.fetchall()
		retdevolver = json.dumps(ret, default=str)
		cur1.close()
		cur2.close()
		conn.close()
		return retdevolver
	
	def borrar_proyecto(self, proyecto):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		#na
		#"SELECT * FROM proyecto WHERE correo=%s",(email,)
		cur.execute("DELETE FROM etiqueta WHERE proyecto_nombre=%s;",(proyecto,))
		cur.execute("DELETE FROM pista WHERE proyecto_nombre=%s;",(proyecto,))
		cur.execute("DELETE FROM proyecto WHERE nombre=%s;",(proyecto,))
		conn.commit()
		#return json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()	
		
	def set_pistas_proyecto(self,nombre,idProyecto,audio,instante,duracion,panning):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		#Inserta una nueva pista al proyecto idProyecto con la información proporcionada
		cur.execute("""INSERT INTO pista(nombre,proyecto_nombre,audio,fecha,instante,duracion,panning) VALUES (%s,%s,%s,DEFAULT,%s,%s,%s);""", (nombre,idProyecto,audio,instante,duracion,panning))
		conn.commit()
		cur.close()
		conn.close()
			
	def get_pistas_proyecto(self,idProyecto):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		#devuelve una lista de pistas, Cada
		#[ [id,Audio,Panning,Instante],[],..]
		cur.execute("SELECT nombre, instante, duracion, panning FROM pista WHERE proyecto_nombre=%s",(idProyecto,))
		ret = json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()
		return ret	

	def get_pistas_mezclar(self,idProyecto):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		#devuelve una lista de pistas, Cada
		#[ [id,Audio,Panning,Instante],[],..]
		cur.execute("SELECT audio, instante, panning, nombre FROM pista WHERE proyecto_nombre=%s;",(idProyecto,))
		lista=cur.fetchall()
		cur.close()
		conn.close()
		return lista
		
	def borrar_pista(self,idProyecto,nombrePista):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		cur.execute("DELETE FROM pista WHERE nombre=%s AND proyecto_nombre=%s;",(nombrePista,idProyecto))
		conn.commit()
		cur.close()
		conn.close()

	def mas_visitados():
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()	
		#mostrar los proyectos mas visitados,p.e. 100
		
		cur.execute('SELECT * FROM proyecto ORDER BY numVisitas DESC LIMIT 100;')
		ret = json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()
		return ret
		
	def get_comentarios(self,idProyecto):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
	 	#devuelve una lista de pistas, Cada
	 	#[ [id,Audio,Panning,Instante],[],..]
		cur.execute("SELECT fecha, comentador, texto  FROM comentario WHERE proyecto_nombre=%s",(idProyecto,))
		ret = json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()
		return ret

	def set_comentario(self,text, proyecto, idUser):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		#devuelve una lista de pistas, Cada
		#[ [id,Audio,Panning,Instante],[],..]
		cur.execute("""INSERT INTO comentario(id,fecha,texto,proyecto_nombre,comentador) VALUES (DEFAULT,DEFAULT,%s,%s,%s);""",(text, proyecto, idUser,))
		conn.commit()
		cur.close()
		conn.close()

	def get_nombre(self,correo):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		cur.execute("SELECT nombre FROM usuario WHERE correo=%s;",(correo,))
		p =cur.fetchone()[0]
		lista=p.split()
		cur.close()
		conn.close()
		return lista[0]

	def buscador(self,proyecto):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		#busca un proyecto
		res=cur.execute("SELECT DISTINCT (nombre), descripcion, imagen, administrador FROM proyecto,etiqueta WHERE nombre=proyecto_nombre AND (nombre=%s OR categoria=%s) AND privacidad=%s ;",(proyecto,proyecto,'True'))
		ret = json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()
		return ret

	def buscadorU(self,user):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		#busca un proyecto
		res=cur.execute("SELECT DISTINCT (nombre), correo, contrasena FROM usuario WHERE nombre=%s;",(user,))
		ret = json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()
		return ret


	def get_valoracion_usuario(self,idProyecto,idUser):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		cur.execute("SELECT valor FROM valoracion WHERE proyecto_nombre=%s AND usuario_nombre=%s",(idProyecto,idUser,))
		if cur.rowcount == 0:
			p='0'
		else:
			p=cur.fetchone()[0]
		cur.close()
		conn.close()
		return str(p)	

	def set_valoracion_usuario(self,idProyecto,idUser,valoracion):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		cur.execute("SELECT COUNT(*) FROM valoracion WHERE proyecto_nombre=%s AND usuario_nombre=%s;",(idProyecto,idUser))
		cuenta=cur.fetchone()[0]
		if cuenta==0:
			cur.execute("""INSERT INTO valoracion(proyecto_nombre,usuario_nombre,valor) VALUES (%s, %s,%s);""",(idProyecto,idUser,valoracion))
		else:
			cur.execute("""UPDATE valoracion SET valor=%s WHERE proyecto_nombre=%s AND usuario_nombre=%s;""",(valoracion,idProyecto,idUser))
		conn.commit()
		cur.close()
		conn.close()

	def sumar_visita(self,idProyecto,idUser):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		cur.execute("""INSERT INTO visita(proyecto_nombre,usuario_nombre,fecha) VALUES (%s, %s,DEFAULT);""",(idProyecto,idUser))
		conn.commit()
		cur.close()
		conn.close()

	def mas_visitados(self):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		res=cur.execute("SELECT * FROM proyecto ORDER BY numvisitas DESC LIMIT 3;")
		ret = json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()
		return ret

	def mejor_valorados(self):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		cur.execute("SELECT * FROM proyecto ORDER BY valoracionTotal DESC LIMIT 10;")	
		ret = json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()
		return ret

	def mas_comentados(self):
		conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
		cur = conn.cursor()
		#saco los proyectos mas comentados,ordenados descendente
		# cur.execute("SELECT proyecto_nombre,COUNT(*) FROM comentario GROUP BY proyecto_nombre;")
		# Proyectosdevueltos=cur.fetchall()
		# lista=list()
		# for p in Proyectosdevueltos:
		# 	cur.execute("SELECT * FROM proyecto WHERE nombre=%s;",(p[0]))
		# 	lista.append(cur.fetchall()) 
		cur.execute("SELECT p.nombre,p.fechacreacion,p.fechaultimamod,p.numvisitas,p.imagen,p.privacidad,p.valoracionTotal,p.descripcion,p.administrador FROM proyecto p, (SELECT proyecto_nombre,COUNT(*) cuenta FROM comentario GROUP BY proyecto_nombre) t WHERE p.nombre=t.proyecto_nombre ORDER BY cuenta DESC LIMIT 10;")
		ret = json.dumps(cur.fetchall(), default=str)
		cur.close()
		conn.close()
		return ret
