import os
from flask import Flask, render_template, request

import ProjectControl
from ProjectAdmin import ProjectAdmin
from ProjectColaborador import ProjectColaborador
from ProjectManager import ProjectManager

UPLOAD_FOLDER = "/Users/pedroramonedafranco/PycharmProjects/mixcrowd/uploads"
ALLOWED_AUDIO_EXTENSIONS = set(['mp3'])
ALLOWED_IMAGE_EXTENSIONS = set(['JPEG'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/prueba')
def upload_html():
    return render_template('prueba1.html')


def allowed_audio(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_AUDIO_EXTENSIONS

def allowed_image(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS


def mezclar():
    os.system("ffmpeg -i " + UPLOAD_FOLDER + "/nombre1.mp3 -i " + UPLOAD_FOLDER +
              "/nombre2.mp3 -filter_complex amerge -ac 2 -c:a libmp3lame -q:a 4 " +
              UPLOAD_FOLDER + "/mezcla.mp3")


@app.route('/prueba_uploader', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        filename1 = "nombre1.mp3"
        filename2 = "nombre2.mp3"
        f1 = request.files['file1']
        f2 = request.files['file2']
        if allowed_file(f1.filename) and allowed_file(f2.filename):
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
@login_required
def new_project():
    pr = ProjectManager(request)
    pr.crear_proyecto()

"""
    peticion [Get] /delete_project/<int:id_project>
    formato: request http normal 
    Despues de  /delete_project/ se pone el entero que identifica el proyecto
"""
@app.route('/delete_project/<int:id_project>', methods=['GET'])
@login_required
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
@login_required
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
@login_required
def privacidad_project(id_project):
    if ProjectControl.es_admin(get_id_propio(), id_project):
        pa = ProjectAdmin(request)
        pa.modificar_proyecto()
    else:
        return "No se tienen los privilegios necesarios."


"""
    peticion [Post] /add_pista/<int:id_project>
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    pista_nueva = un archivo de audio con la pista nueva
"""
@app.route('/add_pista/<int:id_project>', methods=['POST'])
@login_required
def add_pista(id_project):
    if request.method == 'POST':
        id = get_id_propio()
        if ProjectControl.es_admin(id, id_project):
            pr = ProjectColaborador(request)
        elif ProjectControl.es_colaborador(id, id_project):
            pr = ProjectAdmin(request)
        else: #es publico
            pr = ProjectManager(request)
        pr.add_pista()

"""
    peticion [GET] /delete_pista/<int:id_project>
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    id_pista = el identificador de la pista que se quiere borrar
"""
@app.route('/delete_pista/<int:id_project>', methods=['GET'])
@login_required
def delete_pista(id_project):
    if request.method == 'POST':
        id = get_id_propio()
        if ProjectControl.es_admin(id, id_project):
            pr = ProjectColaborador(request)
        elif ProjectControl.es_colaborador(id, id_project):
            pr = ProjectAdmin(request)
        else:
            return 'No se tienen los privilegios necesarios para dicha accion'
        pr.delete_pista()

"""
    peticion [Post] /add_colaborador/<int:id_project>
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    id_nuevo_colaborador = id del colaborador que se desea añadir
"""
@app.route('/add_colaborador', methods=['GET'])
@login_required
def add_colaborador(id_project):
    if request.method == 'POST':
        if ProjectControl.es_admin(get_id_propio(), id_project)
            pr = ProjectAdmin(request)
        elif ProjectControl.es_colaborador(get_id_propio(), id_project):
            pr = ProjectColaborador(request)
        else:
            return 'No se tienen los privilegios necesarios para dicha accion'
        pr.add_pista()

"""
    peticion [Post] /set_comentario
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    id_mensaje = mensjae al que se comenta
    comentario = el texto del comentario
    
"""
@app.route('/set_comentario', methods=['GET'])
@login_required
def set_comentario():
    if request.method == 'POST':
        pr = ProjectManager(request)
        pr.comentar()


if __name__ == '__main__':
    app.run(debug=True)
