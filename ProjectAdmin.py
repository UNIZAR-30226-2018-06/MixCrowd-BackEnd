from ProjectColaborador import ProjectColaborador
from ProjectManager import ProjectManager



class ProjectAdmin(ProjectColaborador):
    def __init__(self):
        ProjectColaborador.__init__(self)

    @classmethod
    def delete_proyecto( id_proyecto):
        db.delete_pista( proyecto)

    @classmethod
    def modificar_proyecto(id,proyecto,imagen,descripcion):
        db.modificar_proyecto(id,proyecto,imagen,descripcion)


    # privado es true y publico false
    @classmethod
    def set_privacidad(privacidad, proyecto):
        privado = 0 if "privado" == privacidad else 1
        db.update_privacidad_proyecto(privado, proyecto)



