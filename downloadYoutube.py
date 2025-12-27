import json
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

    http_headers = {}
    user_agent = os.environ.get('YT_USER_AGENT')
    if user_agent:
        http_headers['User-Agent'] = user_agent

    referer = os.environ.get('YT_REFERER')
    if referer:
        http_headers['Referer'] = referer

    if http_headers:
        ydl_opts['http_headers'] = http_headers

    player_clients = os.environ.get('YT_PLAYER_CLIENTS')
    if player_clients:
        ydl_opts['extractor_args'] = {
            'youtube': {
                'player_client': [client.strip() for client in player_clients.split(',') if client.strip()],
            },
        }

    extra_opts_json = os.environ.get('YT_DLP_OPTS_JSON')
    if extra_opts_json:
        try:
            extra_opts = json.loads(extra_opts_json)
        except json.JSONDecodeError as exc:
            print(f"YT_DLP_OPTS_JSON no es un JSON válido: {exc}")
        else:
            if isinstance(extra_opts, dict):
                ydl_opts.update(extra_opts)
            else:
                print("YT_DLP_OPTS_JSON debe ser un objeto JSON con opciones de yt-dlp.")

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
