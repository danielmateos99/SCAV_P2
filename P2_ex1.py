import os

print("Calidad del vídeo:")
os.system('ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of default=nw=1 BBB.mp4')

print("Tamaño del vídeo (en bytes):")
os.system('ffprobe -i BBB.mp4 -show_entries format=size -v quiet -of csv="p=0"')

print("Número de frames del vídeo:")
os.system('ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 BBB.mp4')

print(" ")
