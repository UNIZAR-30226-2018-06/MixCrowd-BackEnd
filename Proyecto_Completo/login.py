from flask import Flask, render_template, redirect, url_for,request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy  import SQLAlchemy
#from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from sqlalchemy import create_engine
import psycopg2
from dbadapter import DbAdapter
from ProjectControl import ProjectControl
from ProjectAdmin import ProjectAdmin
from ProjectColaborador import ProjectColaborador
from ProjectManager import ProjectManager
from Mixer import Mixer
from buscador import Buscador

import random
import string
import datetime
import os
import json


app = Flask(__name__)
UPLOAD_FOLDER = "/home/dario/Escritorio/mixcrowd/completo/files/originales"
ALLOWED_AUDIO_EXTENSIONS = set(['mp3'])
ALLOWED_IMAGE_EXTENSIONS = set(['JPEG'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://admin:1234@localhost:2223/practica1'
#sqlite:////mnt/c/Users/antho/Documents/login-example/database.db
#engine=create_engine('postgresql://admin:1234@192.168.0.156:22/practica1')
#conn = psycopg2.connect("dbname=practica1 host=192.168.0.156 port=5432 user=admin password=1234 sslmode=require")
#cur = conn.cursor()

bootstrap = Bootstrap(app)
#db = SQLAlchemy(app)


#app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/login_db'
#sqlite:////mnt/c/Users/antho/Documents/login-example/database.db
#bootstrap = Bootstrap(app)
#db = SQLAlchemy(app)
login_manager = LoginManager()
#login_manager.init_app(app)
#login_manager.login_view = 'login'

#class User(UserMixin, db.Model):
 #   id = db.Column(db.Integer, primary_key=True)
 #   username = db.Column(db.String(15), unique=True)
 #   email = db.Column(db.String(50), unique=True)
 #   password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

#funcion para devolver el id del user, no se para
#que la quieres porque como ves se hace solo
def get_id():
    user_id = current_user.get_id()
    return user_id

@app.route('/', defaults={'idUser': 'None'}, methods=['GET'])
@app.route('/<idUser>',  methods=['GET'])
def index(idUser):
    return render_template('carousel.html',idUser=idUser)
#@user.route('/<user_id>', defaults={'username': None})
#user.route('/<user_id>/<username>')

@app.route('/signpag', defaults={'idUser': 'None'}, methods=['GET'])
@app.route('/signpag<idUser>',  methods=['GET'])
def sign_pag(idUser):
    return render_template('index.html',idUser=idUser)
#@user.route('/<user_id>', defaults={'username': None})
#user.route('/<user_id>/<username>')

@app.route('/login', methods=['GET','POST'])
def login():
    email=request.form['email']
    password=request.form['password']
    adapter=DbAdapter()
    respuesta=adapter.loguear(email,password)
    if respuesta=='0':
	    return "Debe introducir usuario y contrasena para poder realizar el login"
    elif respuesta=='1':
        return "Usuario o contrasena incorrectos"
    else:
        nombre=adapter.get_nombre(email)
        return redirect('mostrar_inicio/'+nombre)
        #return render_template('busqueda.html')

@app.route('/mostrar_inicio', defaults={'idUser': 'None'}, methods=['GET'])
@app.route('/mostrar_inicio/<idUser>', methods=['GET'])
def mostrar_inicio(idUser):
        return render_template('carousel.html', idUser=idUser)
	
@app.route('/signup', methods=['GET','POST'])
def signup():
	username=request.form['username']
	email=request.form['email']
	password=request.form['password']
	adapter=DbAdapter()
	adapter.signup(username,password,email)
	#return render_template('busqueda.html')
	return redirect('mostrar_inicio/'+username)

@app.route('/mostrar_busqueda', defaults={'idUser': 'None'}, methods=['GET'])
@app.route('/mostrar_busqueda/<idUser>', methods=['GET'])
def mostrar_busqueda(idUser):
        return render_template('busqueda.html', idUser=idUser)

@app.route('/inicio', defaults={'idUser': 'None'}, methods=['GET'])
@app.route('/inicio/<idUser>', methods=['GET'])
def inicio(idUser):
    proyect_real=idUser.split("_")
    return redirect('mostrar_inicio/'+proyect_real[1])

@app.route('/busqueda', defaults={'idUser': 'None'}, methods=['GET'])
@app.route('/busqueda/<idUser>', methods=['GET'])
def busqueda(idUser):
    proyect_real=idUser.split("_")
    return redirect('mostrar_busqueda/'+proyect_real[1])

@app.route('/index2', defaults={'idUser': 'None'})
@app.route('/index2/<idUser>')
def index2(idUser): 
    return render_template('index2.html',idUser=idUser)

@app.route('/projectnuevo', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/projectnuevo/<idUser>',  methods=['GET','POST'])
def projectnuevo(idUser):
    titulo=request.form['title']
    descp=request.form['descp']
    imgPro=request.form['imgPro']
    #total = request.form['estilo']
    # ,request.form['rock']
    # ,request.form['metal']
    # ,request.form['punk']
    # ,request.form['hiphop']
    # ,request.form['clasica']
    # ,request.form['otro']]
    total=request.form.getlist('estilo')
    pri=request.form.getlist('privacidad')
    pr = ProjectManager(request)
    pr.insertar_proyecto(titulo,descp,imgPro,idUser,pri)
    for x in total:
        if not x is None:
            pr.insertar_estilo(titulo,x)
    return redirect("http://mixcrowddb.sytes.net:5000/index2/"+idUser)

@app.route('/mostrar_user/<idUser>',  methods=['GET','POST'])
def mostrar_user(idUser):
    return redirect("http://mixcrowddb.sytes.net:5000/mostrar_user_final/"+ idUser)   

@app.route('/mostrar_user_final/<idUser>',  methods=['GET','POST'])
def mostrar_user_final(idUser):
    return render_template('config.html',idUser=idUser)    

@app.route('/borrar_proyecto/<id_proyecto>', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/borrar_proyecto/<id_proyecto>/<idUser>',  methods=['GET','POST'])
def borrar_proyecto(id_proyecto,idUser):
    borrador=ProjectAdmin(request)
    borrador.delete_proyecto(id_proyecto)
    return render_template('index2.html')

@app.route('/getProjectsUser', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/getProjectsUser/<idUser>',  methods=['GET','POST'])
def getProjectsUser(idUser):
    #user = request.args.get('iduser',default='*',type =str)
    search = Buscador()
    return search.buscar_p_usuario(idUser)

@app.route('/getSearch/<search1>', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/getSearch/<search1>/<idUser>',  methods=['GET','POST'])
def getSearch(search1,idUser):
    #user = request.args.get('iduser',default='*',type =str)
    search = Buscador()
    return search.buscarB(search1)

@app.route('/getSearchUser/<search1>', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/getSearchUser/<search1>/<idUser>',  methods=['GET','POST'])
def getSearchUser(search1,idUser):
    #user = request.args.get('iduser',default='*',type =str)
    search = Buscador()
    p=search.buscarU(search1)
    with open('info.txt', 'w') as the_file:
        the_file.write(p)
    return p

@app.route('/info_user/<idUser>',  methods=['GET','POST'])
def info_user(idUser):
    #user = request.args.get('iduser',default='*',type =str)
    search = Buscador()
    return search.buscarU(idUser)
    # with open('info.txt', 'w') as the_file:
    #     the_file.write(p)
    # return p

@app.route('/getStyles/<id_proyecto>', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/getStyles/<id_proyecto>/<idUser>',  methods=['GET','POST'])
def getStyles(id_proyecto,idUser):
    pr = ProjectManager(request)
    return pr.traer_estilos(id_proyecto)

@app.route('/mostrar_proyecto/<id_proyecto>', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/mostrar_proyecto/<id_proyecto>/<idUser>',  methods=['GET','POST'])
def mostrar_proyecto(id_proyecto,idUser):
    search = Buscador()
    pr=ProjectManager(request)
    # pr.sumar_visita(id_proyecto,idUser)
    return search.traer_proyecto(id_proyecto)

@app.route('/mezclador/<id_proyecto>', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/mezclador/<id_proyecto>/<idUser>',  methods=['GET','POST'])
def mezclador(id_proyecto,idUser):
    # id_proyecto=request.form['id_proyecto']
    # img=request.form['img']
    # desc=request.form['descripcion']
    # admin=request.form['administrador']
    return render_template('mezclador.html', name=id_proyecto,idUser=idUser);


"""
    peticion [Post] /add_pista/<int:id_project>
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    nombre_pista
    pista_nueva = un archivo de audio con la pista nueva
    instante = momento en el que se tiene que empezar a mezclar la pista
    panning = https://es.wikipedia.org/wiki/Panning /// entre el 0 y el 100 siendo 50 el centro
"""
@app.route('/add_pista', defaults={'idUser': 'None'},  methods=['POST'])
@app.route('/add_pista/<idUser>',  methods=['POST'])
def add_pista(idUser):
    if request.method == 'POST':
        pr = ProjectManager(request)
        audio = request.files['pista_nueva']
        filenameA = ''.join([random.choice(string.ascii_lowercase) for i in range(16)]) + ".mp3"
        audio.save(os.path.join(app.config['UPLOAD_FOLDER'], filenameA))
        pr.add_pista(request,filenameA)
        return 'ok'


@app.route('/mezclar_todo/', methods=['GET','POST'])
@app.route('/mezclar_todo/', methods=['GET','POST'])
def mezclar_todo():
    pr = ProjectManager(request)
    # pistas = json.loads(request.form["lista"], encoding="utf-8") # Just an example(request.files['lista']) json.loads(
    proyecto = request.form["proyecto"].split("_")[0]
    pistasSet = request.form["lista"]
    instante = request.form["instante"]
    panning = request.form["panning"]

    lista_pistas = pr.get_all_pistas_mezclar(proyecto)
    # with open('info.txt', 'w') as the_file:
    #     the_file.write(str(lista_pistas))
    audioP = pr.mezclar(proyecto,lista_pistas,pistasSet,panning,instante)
    
    return audioP


"""
    peticion [GET] /delete_pista/<int:id_project>
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    id_pista = el identificador de la pista que se quiere borrar
"""

@app.route('/delete_pista/<id_project>/<id_pista>', defaults={'idUser': 'None'}, methods=['GET'])
@app.route('/delete_pista/<id_project>/<id_pista>/<idUser>', methods=['GET','POST'])
def delete_pista(id_project,id_pista,idUser):
    pa = ProjectAdmin(request)
    pa.delete_pista(id_project,id_pista)
    return 'ok'


    # if request.method == 'POST':
    #     id = get_id_propio()
    #     if ProjectControl.es_admin(id, id_project):
    #         pr = ProjectColaborador(request)
    #     elif ProjectControl.es_colaborador(id, id_project):
    #         pr = ProjectAdmin(request)
    #     else:
    #         return 'No se tienen los privilegios necesarios para dicha accion'
    #     pr.delete_pista()


    """
        peticion [Post] /add_pista/<int:id_project>
        formato: formData de javascript
        id_proyecto = nuevo nombre del proyecto que está creando
        nombre_pista
        pista_nueva = un archivo de audio con la pista nueva
        instante = momento en el que se tiene que empezar a mezclar la pista
        panning = https://es.wikipedia.org/wiki/Panning /// entre el 0 y el 100 siendo 50 el centro
    """
@app.route('/get_todas_pistas/<id_project>', defaults={'idUser': 'None'}, methods=['GET'])
@app.route('/get_todas_pistas/<id_project>/<idUser>', methods=['GET'])
def get_todas_pistas(id_project,idUser):
    if request.method == 'GET':
        pr = ProjectManager(request)
        return pr.get_all_pistas(id_project)


"""
    peticion [Post] /set_comentario
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    id_mensaje = mensjae al que se comenta
    comentario = el texto del comentario
    
"""
# @app.route('/info_user', defaults={'idUser': 'None'}, methods=['GET'])
# @app.route('/info_user/<idUser>', methods=['GET'])
# def info_user(idUser):
#     return render_template('config.html',idUser=idUser)


@app.route('/set_comentario/', defaults={'info': 'None'}, methods=['POST'])
@app.route('/set_comentario/<info>', methods=['GET','POST'])
def set_comentario(info):
    proyect_real=info.split("_")
    pr = ProjectManager(request)
    pr.comentar(request,proyect_real[1],proyect_real[0])
    return redirect("http://mixcrowddb.sytes.net:5000/mezclador/"+info)

"""
    peticion [Post] /set_comentario
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    id_mensaje = mensjae al que se comenta
    comentario = el texto del comentario
    
"""
@app.route('/get_comentario/', defaults={'id_project': 'None'}, methods=['GET'])
@app.route('/get_comentario/<id_project>', methods=['GET'])
def get_comentario(id_project):
    nombreproyecto=id_project.split("_")
    pr = ProjectManager(request)
    return pr.get_comentario(nombreproyecto[0])


@app.route('/get_valoracion_usuario/<id_proyecto>', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/get_valoracion_usuario/<id_proyecto>/<idUser>',  methods=['GET','POST'])
def get_valoracion_usuario(id_proyecto,idUser):
    bus=Buscador()
    if idUser == 'None':
    	return '-1'
    else:
    	return bus.get_valoracion_usuario(id_proyecto,idUser)

@app.route('/set_valoracion_usuario/<id_proyecto>', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/set_valoracion_usuario/<id_proyecto>/<idUser>',  methods=['GET','POST'])
def set_valoracion_usuario(id_proyecto,idUser):
    val=request.form['val']
    with open('info.txt', 'w') as the_file:
      the_file.write(val)
    p=ProjectManager(request)
    p.set_valoracion_usuario(id_proyecto,idUser,val)
    return 'ok'
    


@app.route('/get_carousel_principal/', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/get_carousel_principal/<idUser>',  methods=['GET','POST'])
def get_carousel_principal(idUser):
    bus=Buscador()
    return bus.get_carousel_principal()

@app.route('/get_carousel_user1/', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/get_carousel_user1/<idUser>',  methods=['GET','POST'])
def get_carousel_user1(idUser):
    bus=Buscador()
    return bus.get_carousel_user1()

@app.route('/get_carousel_user2/', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/get_carousel_user2/<idUser>',  methods=['GET','POST'])
def get_carousel_user2(idUser):
    bus=Buscador()
    return bus.get_carousel_user2()

@app.route('/get_carousel_user_recomend/', defaults={'idUser': 'None'},  methods=['GET','POST'])
@app.route('/get_carousel_user_recomend/<idUser>',  methods=['GET','POST'])
def get_carousel_user_recomend(idUser):
    bus=Buscador()
    return bus.get_carousel_user_recomendado(idUser)


@app.route('/prueba_uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        filename1 = "nombre1.mp3"
        filename2 = "nombre2.mp3"
        f1 = request.files['file1']
        f2 = request.files['file2']
        if allowed_audio(f1.filename) and allowed_audio(f2.filename):
            f1.save(os.path.join(app.config['UPLOAD_FOLDER'], filename1))
            f2.save(os.path.join(app.config['UPLOAD_FOLDER'], filename2))
            return 'files uploaded successfully'
        else:
            return 'Alguno de los archivos subidos no tiene la extensión mp3.'
    elif request.method == 'GET':
        mezclar()
        os.system("mv " + UPLOAD_FOLDER +
                  "/mezcla.mp3 /Users/pedroramonedafranco/PycharmProjects/mixcrowd/static/mezcla1.mp3")
        return ''' <audio controls>
                         <source src="http://localhost:5000/static/mezcla1.mp3" type="audio/mpeg">
                        </audio> '''


# Project Manager



"""
    peticion [Post] /new_project
    formato: formData de javascript
    id = id del usuario que está subiendo el archivo
    proyecto = nuevo nombre del proyecto que está creando
    imagen = la imagen del proyecto.
    descripcion = la descripcion del proyecto
"""
@app.route('/new_project', methods=['POST'])

def new_project():
    pr = ProjectManager(request)
    pr.crear_proyecto()

"""
    peticion [Get] /delete_project/<int:id_project>
    formato: request http normal 
    Despues de  /delete_project/ se pone el entero que identifica el proyecto
"""
@app.route('/delete_project/<int:id_project>', methods=['GET'])

def delete_project(id_project):
    if ProjectControl.es_admin(get_id_propio(), id_project):
        pa = ProjectAdmin(request)
        pa.delete_proyecto(id_project)
    else:
        return "No se tienen los privilegios necesarios."


"""
    peticion [Post] /modify_project/<int:id_project>
    formato: formData de javascript
    id = id del usuario que está subiendo el archivo
    proyecto = nuevo nombre del proyecto que está creando
    imagen = la imagen del proyecto.
    descripcion = la descripcion del proyecto
"""
@app.route('/modify_project/<int:id_project>', methods=['POST'])

def modify_project(id_project):
    if ProjectControl.es_admin(get_id_propio(), id_project):
        pa = ProjectAdmin(request)
        pa.modificar_proyecto()
    else:
        return "No se tienen los privilegios necesarios."


"""
    peticion [Post] /privacidad_project/<int:id_project>
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    privacidad = un string con publico o privado.
"""
@app.route('/privacidad_project/<int:id_project>', methods=['POST'])

def privacidad_project(id_project):
    if ProjectControl.es_admin(get_id_propio(), id_project):
        pa = ProjectAdmin(request)
        pa.modificar_proyecto()
    else:
        return "No se tienen los privilegios necesarios."



"""
    peticion [Post] /add_colaborador/<int:id_project>
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    id_nuevo_colaborador = id del colaborador que se desea añadir
"""
@app.route('/add_colaborador', methods=['GET'])

def add_colaborador(id_project):
    if request.method == 'POST':
        if ProjectControl.es_admin(get_id_propio(), id_project):
            pr = ProjectAdmin(request)
        elif ProjectControl.es_colaborador(get_id_propio(), id_project):
            pr = ProjectColaborador(request)
        else:
            return 'No se tienen los privilegios necesarios para dicha accion'
        pr.add_pista()



"""
    peticion [GET] /mezclar/<int:id_project>
    devuelve la direccion de static donde está el audio mezclado.

"""
@app.route('/mezclador/<int:id_project>', methods=['GET'])
def mezclar(id_project):
    if request.method == 'GET':
        if ProjectControl.es_admin(get_id_propio(), id_project):
            pr = ProjectAdmin(request)
        elif ProjectControl.es_colaborador(get_id_propio(), id_project):
            pr = ProjectColaborador(request)
        else:
            pr = ProjectManager(request)
        audio=pr.mezclar(id_project)
        if not audio:
            return "No hay pistas en el proyecto"
        else:
            return audio







if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
