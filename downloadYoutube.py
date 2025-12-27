import os
import yt_dlp


def descargar_videos(urls, destino='.'):
    ydl_opts = {
        'outtmpl': f'{destino}/%(playlist_index)s - %(title)s.%(ext)s',  # Ruta y nombre del archivo de salida
        'format': 'bestvideo+bestaudio/best',       # Selecciona la mejor calidad de video y audio
        'noplaylist': True,                         # Evita descargar listas de reproducción enteras si se proporciona una URL de lista
    }

    cookies_file = os.environ.get('YT_COOKIES_FILE')
    if cookies_file:
        ydl_opts['cookies'] = cookies_file

    cookies_from_browser = os.environ.get('YT_COOKIES_FROM_BROWSER')
    if cookies_from_browser:
        ydl_opts['cookiesfrombrowser'] = cookies_from_browser

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
        print("Descarga completada.")
    except Exception as e:
        print(f"Ocurrió un error al descargar los videos: {e}")


if __name__ == "__main__":
    urls = [
        "https://youtu.be/XXXXX",
        #"https://youtu.be/XXX"



        # Agrega más URLs según sea necesario
    ]
    descargar_videos(urls, destino='videos')
