from pytube import YouTube
from pytube.exceptions import RegexMatchError, HTMLParseError
from pydub import AudioSegment
from urllib.error import HTTPError
import os

# Obtener la ruta absoluta del directorio actual
ruta = os.getcwd()

def descargar_video(url, ruta):
    try:
        yt = YouTube(url)
        # Comprobar si se encontró un video
        if yt.streams:
            # Seleccionar la mejor calidad disponible
            video = yt.streams.filter(only_audio=True).first()
            # Descargar el video
            video.download(ruta)
            return video.default_filename
        else:
            # No se encontró ningún video
            raise ValueError("No se encontró ningún video para el URL proporcionado.")
    except HTTPError as e:
        # Error HTTP al intentar descargar el video
        raise ValueError(f"Error HTTP al descargar el video: {str(e)}")
    except RegexMatchError:
        # El URL no es válido para un video de YouTube
        raise ValueError("El URL proporcionado no es válido para un video de YouTube.")
    except Exception as e:
        # Otro tipo de error
        raise ValueError(f"Error al descargar el video: {str(e)}")




def convertir_a_mp3(video_file, ruta):
    """
    Convierte un archivo de video a formato mp3.

    Args:
    video_file (str): Nombre del archivo de video a convertir.

    Returns:
    str: Nombre del archivo mp3 generado.
    """
    try:
        # Construir la ruta completa al archivo de video
        video_file_path = os.path.join(ruta, video_file)
        print("Convirtiendo:", video_file_path)
        # Cargar el archivo de audio usando pydub
        audio = AudioSegment.from_file(video_file_path)
        print("Audio cargado")
        # Crear el nombre del archivo mp3
        mp3_file = os.path.splitext(video_file)[0] + '.mp3'
        mp3_file_path = os.path.join(ruta, mp3_file)
        print("Nombre del archivo mp3:", mp3_file_path)
        # Exportar el archivo de audio a mp3
        audio.export(mp3_file_path, format='mp3')
        print("Archivo mp3 generado en la ruta:", mp3_file_path)
        # Eliminar el archivo de video
        os.remove(video_file_path)
        print("Archivo de video eliminado")
        return mp3_file
    except Exception as e:
        print("Error al convertir el video a mp3:", str(e))
        return None
