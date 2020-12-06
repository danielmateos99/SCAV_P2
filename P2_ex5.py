import os

exit = True
while exit == True:

    print("Selecciona un ejercicio: ")
    print("[0]: Cortar 10 segundos del vídeo de BBB.avi")
    print("[1]: Obtener información del vídeo cut.avi")
    print("[2]: Cambiar el nombre de los outputs del ejercicio 3 del seminario 2")
    print("[3]: Cambiar la calidad del vídeo a la deseada")
    print("[4]: Cambiar el input a otro codec")
    print("[5]: Exit")

    a = input()
    x = int (a)
    print(" ")

    if x == 0:
        #Recortar una parte del vídeo BBB_full.avi a 10 segundos y llamarlo BBB con formato mp4
        os.system("ffmpeg -i BBB_full.avi -ss 00:00:20 -t 00:00:10 -async 1 BBB.mp4")
    elif x == 1:
        #Llamar al script de python que realiza el ejercicio 1
        os.system('python P2_ex1.py')
    elif x == 2:
        #Llamar al script de python que realiza el ejercicio 2
        os.system('python P2_ex2.py')
    elif x == 3:
        #Llamar al script de python que realiza el ejercicio 3
        os.system('python P2_ex3.py')
    elif x == 4:
        #Llamar al script de python que realiza el ejercicio 4
        os.system('python P2_ex4.py')
    elif x == 5:
        #Salir del menú
        exit = False
    else:
        #En caso de que no se elija ninguna de las opciones
        print('Error: Introduce alguno de los valores mencionados.')
