from ProjectColaborador import ProjectColaborador
from ProjectManager import ProjectManager



class ProjectAdmin(ProjectColaborador):
    def __init__(self,request):
        ProjectColaborador.__init__(self, request)

    @classmethod
    def delete_proyecto(cls, id_proyecto):
        db.delete_proyecto(id_proyecto)

    @classmethod
    def modificar_proyecto(cls):
        request = cls.request
        if request.method == 'POST':
            id = request.form['id']
            proyecto = request.form['proyecto']
            imagen = request.files['imagen']
            descripcion = request.form['descripcion']
            if ProjectManager.allowed_image(imagen.filename):
                db.modificar_proyecto(id, proyecto, imagen, descripcion)
            else:
                return 'Alguno de los archivos subidos no tiene la extensión propicia.'


    # privado es true y publico false
    @classmethod
    def set_privacidad(cls, privacidad, proyecto):
        request = cls.request
        if request.method == 'POST':
            proyecto = request.form['id_proyecto']
            privacidad = request.form['privacidad']
            if privacidad == "publico" or privacidad == "privado":
                privado = 0 if "privado" == privacidad else 1
                db.update_privacidad_proyecto(privado, proyecto)
            else:
                return 'La privacidad puede ser publica o privada'



