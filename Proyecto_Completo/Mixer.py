import datetime
import random
import string

import os

import math


class Mixer(object):

    @classmethod
    def pre_procesar_pista(cls, filenameA, instante):
        carpeta = "files/originales/"
        # se cambia el sample rate a 44kh
        fmono = "mono"+ filenameA
        # se pasa a mono
        os.system("ffmpeg -y -i " + carpeta + filenameA + " -ac 1 " + carpeta + fmono)
        # se añaden los segundos necesarios
        silence = "silence_" + ''.join([random.choice(string.ascii_lowercase) for i in range(16)]) + ".mp3"
        os.system("ffmpeg -y -f lavfi -i anullsrc=channel_layout=5.1:sample_rate=44100 -t " + str(instante) + " " + carpeta + silence)
        # concateno el silencio
        os.system("ffmpeg -y -i \"concat:" + carpeta + silence + "|" + carpeta + fmono + "\" -acodec copy " + carpeta + filenameA)
        # guardo
        os.system("cp " + carpeta + filenameA + " files/Procesados/" + filenameA)
        # os.system("rm " + carpeta + fmono)
        # os.system("rm " + carpeta + silence)




    def mezclar(cls, pistas,panning,instante):

        if len(pistas)==1:
            # id,audio,pan,instante= pistas[0]
            # basename = ""
            # suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
            # nombre = "a".join([basename, suffix]) + ".mp3"
            # os.system("cp files/originales/" + audio.split(" ")[0] + " static/" + nombre.split(" ")[0])
            # audio_final = nombre.split(" ")[0]
            resultado = pistas[0],pistas[0]
            with open('info5.txt', 'w') as the_file:
                the_file.write(str(resultado))
        else:
            resultado = pistas
        basename = "myDirectory"
        ans_basename = "audioFinal_"
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        directory = "_".join([basename, suffix])
        rutaProcesados = "files/Procesados/"
        with open('info5.txt', 'w') as the_file:
            the_file.write(str(panning))
        with open('info6.txt', 'w') as the_file:
            the_file.write(str(instante))
        ruta = "files/temp/"
        os.system("mkdir " + ruta + directory)
        comandoIzq = "sox -m"
        comandoDcha = "sox -m"
        tracks = len(resultado)
        i = 0
        for pista in resultado:
            id, audio, pan, instant = pista
            if instante.split(",")[i] != "00:00:00":
                separado = instante.split(",")[i]
                with open('info6.txt', 'w') as the_file:
                    the_file.write(str(separado))
                total = int(separado.split(":")[0])*3600 + int(separado.split(":")[1])*60 + int(separado.split(":")[2])
                
                carpeta = "files/originales/"
                # se cambia el sample rate a 44kh
                fmono = "mono"+ audio
                # se pasa a mono
                os.system("ffmpeg -y -i " + carpeta + audio + " -ac 1 " + carpeta + fmono)
                # se añaden los segundos necesarios
                silence = "silence_" + ''.join([random.choice(string.ascii_lowercase) for i in range(16)]) + ".mp3"
                os.system("ffmpeg -y -f lavfi -i anullsrc=channel_layout=5.1:sample_rate=44100 -t " + str(total) + " " + carpeta + silence)
                # concateno el silencio
                os.system("ffmpeg -y -i \"concat:" + carpeta + silence + "|" + carpeta + fmono + "\" -acodec copy " + carpeta + audio)
                # guardo
                os.system("cp " + carpeta + audio + " files/Procesados/" + audio)
                # os.system("rm " + carpeta + fmono)
                # os.system("rm " + carpeta + silence)
            rutaInterna = ruta + directory + "/" + audio
            os.system("cp " + rutaProcesados + audio + " " + rutaInterna )
            # se añade cada una de las resultado al comando de la izquierda y la derecha
            VOLMODleft = (1 / 2) * (1 / math.sqrt(tracks)) * ((100 - int(panning.split(",")[i])) / 50 if (int(panning.split(",")[i]) > 50) else 1)
            VOLMODright = (1 / 2) * (1 / math.sqrt(tracks)) * ((int(panning.split(",")[i])) / 50 if (int(panning.split(",")[i]) < 50) else 1)
            comandoIzq = comandoIzq + " -v " + str(VOLMODleft) + " " + rutaInterna + " "
            comandoDcha = comandoDcha + " -v " + str(VOLMODright) + " " + rutaInterna + " "
            i = i + 1
        # se completa el comando con lo que se tenga que completar
        comandoIzq = comandoIzq + " " + ruta + directory + "/left.mp3 remix 1"
        os.system(comandoIzq)
        comandoDcha = comandoDcha + " " + ruta + directory + "/right.mp3 remix 1"
        os.system(comandoDcha)
        suffix = datetime.datetime.now().strftime("%y%m%d_%H%M%S")
        audio_final = "final_".join([ans_basename, suffix]) + ".mp3"
        comando_mezclar = "ffmpeg -y -i " + ruta + directory + "/left.mp3 -i " + ruta + directory + "/right.mp3" +\
                          " -filter_complex \"[0:a][1:a]amerge=inputs=2[aout]\" -map \"[aout]\" " + ruta + directory + "/" + audio_final
        #audioDecodeD = "\"$(lame --decode " +ruta + directory + "/right.mp3 " + ")\""
        #audioDecodeI = "\"$(lame --decode " +ruta + directory + "/left.mp3 " + ")\""
        #comando_mezclar = "sox -M "+audioDecodeI + audioDecodeD + ruta + directory + "/" + audio_final
        os.system(comando_mezclar)
        # lo guardo en el static
        os.system("cp " + ruta + directory + "/" + audio_final + " static/" + audio_final)
        # borro el directorio temporal
        #os.system("rm -r " + ruta + directory)
        with open('info.txt', 'w') as the_file:
            the_file.write(str(audio_final))
        return "static/" + audio_final

    # Pasamos una pista stereo a mono para que se pueda pannear después sin problemas
    # esto se hace antes de guardar una pista nueva en la base de datos
    """
    Acciones que se realizan:
    se pone el archivo en temp
    Se pasa a mono, el sample rate del mp3 se pasa a 44 khz y se añaden los segundos
    se devuelve el archivo para mandarlo a la base de datos
    """

