import os
from flask import Flask, render_template, request

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
    if request.method == 'POST':
        id = request.form['id']
        proyecto = request.form['proyecto']
        imagen = request.files['imagen']
        descripcion = request.form['descripcion']
        if allowed_image(imagen.filename):
            pr = ProjectManager()
            pr.crear_proyecto(id, proyecto, imagen, descripcion)
            return 'files uploaded successfully'
        else:
            return 'Alguno de los archivos subidos no tiene la extensión propicia.'

"""
    peticion [Get] /delete_project/<int:id_project>
    formato: request http normal 
    Despues de  /delete_project/ se pone el entero que identifica el proyecto
"""
@app.route('/delete_project/<int:id_project>', methods=['GET'])
@login_required
@administrador_required
def delete_project(id_project):
    if request.method == 'GET':
        pa = ProjectAdmin()
        pa.delete_proyecto(id_project)


"""
    peticion [Post] /modify_project
    formato: formData de javascript
    id = id del usuario que está subiendo el archivo
    proyecto = nuevo nombre del proyecto que está creando
    imagen = la imagen del proyecto.
    descripcion = la descripcion del proyecto
"""
@app.route('/modify_project', methods=['POST'])
@login_required
@administrador_required
def new_project():
    if request.method == 'POST':
        id = request.form['id']
        proyecto = request.form['proyecto']
        imagen = request.files['imagen']
        descripcion = request.form['descripcion']
        if allowed_image(imagen.filename):
            pr = ProjectAdmin()
            pr.modificar_proyecto(id, proyecto, imagen, descripcion)
            return 'files uploaded successfully'
        else:
            return 'Alguno de los archivos subidos no tiene la extensión propicia.'


"""
    peticion [Post] /privacidad_project
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    privacidad = un string con publico o privado.
"""
@app.route('/privacidad_project', methods=['POST'])
@login_required
@administrador_required
def privacidad_project():
    if request.method == 'POST':
        proyecto = request.form['id_proyecto']
        privacidad = request.form['privacidad']
        if privacidad == "publico" or privacidad == "privado":
            pr = ProjectAdmin()
            pr.set_privacidad(privacidad, proyecto)
        else:
            return 'La privacidad puede ser publica o privada'


"""
    peticion [Post] /add_pista
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    pista_nueva = un archivo de audio con la pista nueva
"""
@app.route('/privacidad_project', methods=['POST'])
@login_required
def privacidad_project():
    if request.method == 'POST':
        id_usuario = get_id_propio()
        proyecto = request.form['id_proyecto']
        pista = request.pista['pista_nueva']
        if ProjectManager.es_privado(proyecto) and ProjectManager.colaborador(proyecto,id_usuario):
            pr = ProjectColaborador()
        elif ProjectManager.es_privado(proyecto) and ProjectManager.administrador(proyecto, id_usuario):
            pr = ProjectAdmin()
        elif ProjectManager.es_privado(proyecto):
            pr = ProjectManager()
        else:
            return 'No se tienen los privilegios necesarios para dicha accion'

        if allowed_audio(pista.filename):
            pr.add_pista(pista, proyecto)
        else:
            return 'El formato de audio aceptado es MP3'
"""
    peticion [Post] /delete_pista
    formato: formData de javascript
    id_proyecto = nuevo nombre del proyecto que está creando
    pista_nueva = un archivo de audio con la pista nueva
"""
@app.route('/privacidad_project', methods=['GET'])
@login_required
def privacidad_project():
    if request.method == 'POST':
        id_usuario = get_id_propio()
        proyecto = request.form['id_proyecto']
        pista = request.pista['pista_nueva']
        if ProjectManager.es_privado(proyecto) and ProjectManager.colaborador(proyecto,id_usuario):
            pr = ProjectColaborador()
        elif ProjectManager.es_privado(proyecto) and ProjectManager.administrador(proyecto, id_usuario):
            pr = ProjectAdmin()
        elif ProjectManager.es_privado(proyecto):
            pr = ProjectManager()
        else:
            return 'No se tienen los privilegios necesarios para dicha accion'

        if allowed_audio(pista.filename):
            pr.add_pista(pista, proyecto)
        else:
            return 'El formato de audio aceptado es MP3'

if __name__ == '__main__':
    app.run(debug=True)
