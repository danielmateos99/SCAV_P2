import os

print("Nombre del vídeo (sin la extensión):")
name = input()
print("Extensión original (sin el punto):")
ext1 = input()
print("Extensión nueva (sin el punto):")
ext2 = input()

line = "ffmpeg -i {}.{} {}.{}".format(name,ext1,name,ext2)
os.system(line)
