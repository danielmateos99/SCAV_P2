import os

print("Nombre del vídeo:")
name = input()
print("Extensión del vídeo (sin el punto, ej: mp4):")
ext = input()
print("Píxeles para el eje x (anchura):")
xsize = int(input())
print("Píxeles para el eje y (altura):")
ysize = int(input())

line = "ffmpeg -i {}.{} -vf scale={}:{},setsar=1:1 {}_{}:{}.{}".format(name,ext,xsize,ysize,name,xsize,ysize,ext)
os.system(line)
