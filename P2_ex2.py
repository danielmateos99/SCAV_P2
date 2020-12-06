import os

#primero miramos si existe el archivo y en ese caso le cambiamos el nombre
if os.path.isfile("cut1280x720.avi"):
    os.rename("cut1280x720.avi", "rename1")
if os.path.isfile("cut720x480.avi"):
    os.rename("cut720x480.avi", "rename2")
if os.path.isfile("cut360x240.avi"):
    os.rename("cut360x240.avi", "rename3")
if os.path.isfile("cut160x120.avi"):
    os.rename("cut160x120.avi", "pepe")

print("Nombres de los vídeos cambiados.")
print(" ")
