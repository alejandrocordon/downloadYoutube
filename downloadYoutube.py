# remember :  pip install pytube
from pytube import YouTube

link = input("Introduce url de youtube:")
yt = YouTube(link)

stream = yt.streams.get_highest_resolution()

print("Iniciando descarga...")
stream.download()
print("Descarga finalizada.")
