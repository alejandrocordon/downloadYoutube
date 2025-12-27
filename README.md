# downloadYoutube

Script para descargar videos con `yt-dlp`.

## Uso básico

1. Edita `downloadYoutube.py` y agrega tus URLs en la lista `urls`.
2. Ejecuta:

```bash
python downloadYoutube.py
```

## Cookies (autenticación o evitar bloqueos)

Si ya tienes un archivo de cookies llamado `cookies.txt` en la **raíz del proyecto**, entonces puedes usarlo con la variable `YT_COOKIES_FILE`.

- **`YT_COOKIES_FILE`** **sí** se refiere a la ruta de ese archivo (por ejemplo `./cookies.txt`).
- **`YT_COOKIES_FROM_BROWSER`** **no** usa el archivo `cookies.txt`. Esta opción le dice a `yt-dlp` que lea las cookies directamente desde tu navegador instalado (por ejemplo `chrome` o `firefox`).

### Ejemplo usando `cookies.txt`

```bash
export YT_COOKIES_FILE=./cookies.txt
python downloadYoutube.py
```

### Ejemplo usando cookies del navegador

```bash
export YT_COOKIES_FROM_BROWSER=chrome
python downloadYoutube.py
```

## Cabeceras opcionales

Puedes enviar cabeceras HTTP si tu descarga lo requiere:

```bash
export YT_USER_AGENT="Mozilla/5.0 ..."
export YT_REFERER="https://www.youtube.com/"
python downloadYoutube.py
```

## Player clients (opcional)

Para ajustar el cliente del extractor de YouTube:

```bash
export YT_PLAYER_CLIENTS=web,mweb
python downloadYoutube.py
```

## Docker

Construye y ejecuta la imagen:

```bash
docker build -t downloadyoutube .
docker run --rm -e YT_COOKIES_FILE=/app/cookies.txt \
  -v "$(pwd)/cookies.txt:/app/cookies.txt:ro" \
  downloadyoutube
```
