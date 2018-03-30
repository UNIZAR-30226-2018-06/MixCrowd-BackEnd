



class ProjectManager(object):
    def __init__(self):
        self.db = dbadapter()
        self.id = obtenerMiId()

    @classmethod
    def crear_proyecto(id,proyecto,imagen,descripcion):
        db.crear_proyecto(id,proyecto,imagen,descripcion)


    @classmethod
    def add_pista(pista, proyecto):
        db.add(pista,proyecto)

    @classmethod
    def comentar(text, proyecto, idRespondiendo):
        db.comentario(text, proyecto, idRespondiendo)

