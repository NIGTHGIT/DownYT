import os
import yt_dlp

'''
Descarga el video en formato mp3
'''

PATH = 'downloads'

def descargar_mp3(url):
   try:
        
    ydl_opts = {
        'format': 'bestaudio/best',  # Selecciona el mejor formato de audio
        'noplaylist': True,  # Evita descargar listas de reproducción
        'ffmpeg_location': r'C:\ffmpeg\bin',
        'outtmpl': f'{PATH}/%(title)s.%(ext)s',  # Define la plantilla para el nombre del archivo
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',  # Usar el convertidor de audio de FFmpeg
            'preferredcodec': 'mp3',  # Establecer el formato de salida como .mp3
            'preferredquality': '256',  # Calidad deseada para el mp3
        }],
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
     # Extraer información del video y descargar
     info_dict = ydl.extract_info(url, download=True)

     # Obtener el nombre del archivo generado
     audio_filename = ydl.prepare_filename(info_dict)

     # Asegurar que la extensión sea ".mp3"
     audio_filename = audio_filename.rsplit('.', 1)[0] + '.mp3'

    return audio_filename
   except Exception as e:
        return "❌ Error al descargar el video"


def descargar_mp4(url):
    try:
       ydl_opts = {
        'format': 'bestvideo[height<=1080]',  # Selecciona el mejor formato de 
        'outtmpl': F'{PATH}/%(title)s.%(ext)s',  # Define la plantilla para el nombre del archivo
       }
    
       with yt_dlp.YoutubeDL(ydl_opts) as ydl:
       # Extraer información del video y descargar
          info_dict = ydl.extract_info(url, download=True)

       # Obtener el nombre del archivo generado
       audio_filename = ydl.prepare_filename(info_dict)
       return audio_filename
    except Exception as e:
        return  "❌ Error downloading video"

