from ProjectManager import ProjectManager


class ProjectColaborador(ProjectManager):
    def __init__(self):
        ProjectManager.__init__(self)

    @classmethod
    def delete_pista(id_pista, proyecto):
        db.delete_pista(idPista, proyecto)

    @classmethod
    def add_colaborador(proyecto, idColaborador):
        db.update_proyecto(proyecto, idColaborador)