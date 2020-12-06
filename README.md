### SCAV Lab 2
Daniel Mateos Manjón
NIA: 205514

## Introducción
En el Lab2 de la asignatura de SCAV se nos pide realizar diversos scripts de python para cada ejercicio.
Cada script tiene el nombre "P2_exX.py" donde "X" es el número del ejercicio, a continuación explicamos que hace cada uno de ellos.

## Ejercicio 1
Obtenemos información del vídeo BBB.mp4.

Con la línea "ffprobe -v error -select_streams v:0 -show_entries stream=width,height -of default=nw=1 BBB.mp4" obtenemos la calidad del vídeo.
Link: https://superuser.com/questions/841235/how-do-i-use-ffmpeg-to-get-the-video-resolution

Con la línea "ffprobe -i BBB.mp4 -show_entries format=size -v quiet -of csv="p=0"" obtenemos el tamaño del vídeo en bytes.
Link: https://stackoverflow.com/questions/8348830/ffmpeg-read-filesize

Con la línea "ffprobe -v error -select_streams v:0 -show_entries stream=nb_frames -of default=nokey=1:noprint_wrappers=1 BBB.mp4" obtenemos el numero de frames del vídeo.
Link: https://stackoverflow.com/questions/2017843/fetch-frame-count-with-ffmpeg


## Ejercicio 2
En este ejercicio se nos pide renombrar los 4 outputs del ejercicio 3 del seminario 2.
Estos outputs deben ser movidos a la carpeta donde se encuentran los scripts de este Lab para poder ser modificados.
Como no se indica a que nombre hay que cambiarlos, los modificamos los antiguos a los siguientes:
cut1280x720.avi ------> rename1.avi
cut720x480.avi  ------> rename2.avi
cut360x240.avi  ------> rename3.avi
cut160x120.avi  ------> pepe.avi
Para hacerlo utilizamos "os.rename("OLD_NAME.avi", "NEW_NAME")" en python, donde OLD_NAME es el nombre antiguo y NEW_NAME el nuevo.

## Ejercicio 3
Cambiamos la resolución de un input, para ello se pide indicar el nombre del input y su extensión junto con la resolución en píxeles deseada para cada eje (x,y).
Una vez indicados se aplican en la línea "ffmpeg -i INPUT.FORMATO -vf scale=X:Y,setsar=1:1 INPUT_X:Y.EXTENSION", siendo INPUT, EXTENSION, X y Y las variables indicadas.

Link used: https://stackoverflow.com/questions/22101931/passing-more-than-one-variables-to-os-system-in-python

## Ejercicio 4
Cambiamos el codec de un input a otro previamente visto en clase con "ffmpeg -i INPUT.EXT1 INPUT.EXT2", donde INPUT es el archivo al que le vamos a cambiar el codec y EXT1/EXT2 las extensiones original y nueva.
Link: https://opensource.com/article/17/6/ffmpeg-convert-media-file-formats

## Ejercicio 5
Creamos un script de python con un menú que puede llamar a todos los ejercicios anteriores. Además, al principio, añadimos una opción para crear el vídeo "BBB.mp4" como un recorte del original "BBB_full.avi" para que tarde menos en aplicarle otros ejercicios. También se ha añadido la opción de salir del menú.
