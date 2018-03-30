from ProjectManager import ProjectManager


class ProjectColaborador(ProjectManager):
    def __init__(self,request):
        ProjectManager.__init__(self,request)

    @classmethod
    def delete_pista(cls):
        request = cls.request
        proyecto = request.form['id_proyecto']
        id_pista = request.pista['pista_nueva']
        if ProjectManager.allowed_audio(id_pista.filename):
            pr.delete_pista(id_pista, proyecto)
        else:
            return 'El formato de audio aceptado es MP3'
        db.delete_pista(id_pista, proyecto)

    @classmethod
    def add_colaborador(cls):
        request = cls.request
        proyecto = request.form['id_proyecto']
        idColaborador = request.pista['id_nuevo_colaborador']
        db.add_colaborador(proyecto, idColaborador)
