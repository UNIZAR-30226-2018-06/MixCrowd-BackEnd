from Mixer import Mixer
from dbadapter import DbAdapter
import base64
class ProjectManager(object):
    def __init__(self,request):
        self.db = DbAdapter()
        #self.id = obtener_id_propio()
        self.id = 'dario'
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
    def insertar_proyecto(self,titulo,descp,imgPro,idUser,privacidad):
        adapter=DbAdapter()
        adapter.insertar_proyecto(titulo,descp,imgPro,idUser,privacidad) 
    
    @classmethod
    def insertar_estilo(self,titulo,estilo):
        adapter=DbAdapter()
        adapter.insertar_estilo(titulo,estilo)    

    @classmethod
    def traer_estilos(self,idProyecto):
        adapter=DbAdapter()
        return adapter.traer_estilos(idProyecto)
	
    @classmethod
    def get_all_pistas(self,idProyecto):
        adapter=DbAdapter()
        return adapter.get_pistas_proyecto(idProyecto)   

    @classmethod
    def get_all_pistas_mezclar(self,idProyecto):
        adapter=DbAdapter()
        return adapter.get_pistas_mezclar(idProyecto)   

    @classmethod
    def add_pista(cls,req,file):
        adapter=DbAdapter()
        #id_usuario = get_id_propio()
        proyecto = req.form['id_proyecto']
        nombre = req.form['nombre_pista']
        
        pan = req.form['panning']
        instante = req.form['instante']
        #preprocesar pista
        mix=Mixer()
        pistaP = mix.pre_procesar_pista(file,0)
        adapter.set_pistas_proyecto(nombre, proyecto, file, instante, 0, pan)
        
    @classmethod
    def comentar(cls,request,idUser,idProyecto):
        adapter=DbAdapter()
        text = request.form['comentario']
        adapter.set_comentario(text, idProyecto, idUser)

    @classmethod
    def get_comentario(cls,id_project):
        adapter=DbAdapter()
        return adapter.get_comentarios(id_project)

    @classmethod
    def mezclar(cls, id_proyecto,listaP,listaSet,panning,instante):
        mx = Mixer()
        lista = []
        for pista in listaP:
            if pista[3].split(" ")[0] in listaSet:
                idP = pista[3].split(" ")[0]
                audioP = pista[0].split(" ")[0]
                durP = 0
                instP = pista[1]
                lista.append([idP,audioP,50,instP])
        file=open("texto.txt","w")
        file.write(str(lista))
        audio = mx.mezclar(lista,panning,instante)
        return audio


    @classmethod
    def set_valoracion_usuario(self,idProyecto,idUser,valoracion):
        adapter=DbAdapter()
        adapter.set_valoracion_usuario(idProyecto,idUser,valoracion)    

    @classmethod
    def sumar_visita(self,id_proyecto,id_user):
        adapter=DbAdapter()
        adapter.sumar_visita(id_proyecto,id_user)       