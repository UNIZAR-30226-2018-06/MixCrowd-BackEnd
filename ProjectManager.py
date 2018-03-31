



class ProjectManager(object):
    def __init__(self,request):
        self.db = dbadapter()
        self.id = obtener_id_propio()
        self.request = request

    @staticmethod
    def allowed_audio(filename):
        ALLOWED_AUDIO_EXTENSIONS = set(['mp3'])
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_AUDIO_EXTENSIONS

    @staticmethod
    def allowed_image(filename):
        ALLOWED_IMAGE_EXTENSIONS = set(['JPEG'])
        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS

    @classmethod
    def crear_proyecto(cls):
        request = cls.request
        if request.method == 'POST':
            id = request.form['id']
            proyecto = request.form['proyecto']
            imagen = request.files['imagen']
            descripcion = request.form['descripcion']
            if ProjectManager.allowed_image(imagen.filename):
                db.crear_proyecto(id, proyecto, imagen, descripcion)
            else:
                return 'Alguno de los archivos subidos no tiene la extensión propicia.'


    @classmethod
    def add_pista(cls):
        request = cls.request
        id_usuario = get_id_propio()
        proyecto = request.form['id_proyecto']
        pista = request.file['pista_nueva']
        if ProjectManager.allowed_audio(pista.filename):
            db.add(pista, proyecto, id_usuario)
        else:
            return 'El formato de audio aceptado es MP3'

    @classmethod
    def comentar(cls):
        request = cls.request
        idRespondiendo = request.form['id_mensaje']
        proyecto = request.form['id_proyecto']
        text = request.form['comentario']
        db.comentario(text, proyecto, idRespondiendo)

