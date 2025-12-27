import yt_dlp

def descargar_videos(urls, destino='.'):
    ydl_opts = {
        'outtmpl': f'{destino}/%(playlist_index)s - %(title)s.%(ext)s',  # Ruta y nombre del archivo de salida
        'format': 'bestvideo+bestaudio/best',       # Selecciona la mejor calidad de video y audio
        'noplaylist': True,                         # Evita descargar listas de reproducción enteras si se proporciona una URL de lista
        'retries': 3,                               # Reintentos para errores temporales de red
        'fragment_retries': 3,                      # Reintentos para fragmentos (HLS/DASH)
        'http_headers': {
            'User-Agent': (
                'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/120.0.0.0 Safari/537.36'
            ),
        },
        'extractor_args': {
            'youtube': {
                'player_client': ['android', 'web'],
            },
        },
    }
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
