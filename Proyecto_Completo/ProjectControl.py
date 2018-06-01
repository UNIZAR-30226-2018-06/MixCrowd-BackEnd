


class ProjectControl(object):
    def __init__(self):
        self.db = DbAdapter()

    #es colaborador y privado
    @staticmethod
    def es_colaborador(id_propio,id_proyecto):
        ans = db.es_colaborador(id_propio,id_proyecto)
        if ans == None:
            return True
        else:
            return False


    # es admin y privado
    @staticmethod
    def es_admin(id_propio,id_proyecto):
        ans = db.es_colaborador(id_propio,id_proyecto)
        if ans == None:
            return True
        else:
            return False

    # es publico
    @staticmethod
    def es_publico(id_propio,id_proyecto):
        ans = db.es_publico(id_propio, id_proyecto)
        if ans == None:
            return True
        else:
            return False


