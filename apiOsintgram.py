#!/bin/python

# Import per cridar l'eina theHarvester
import asyncio
import subprocess
from bot_telegram import enviarMensaje, enviarDocumento
def propic():
    enviarMensaje("Imatge de perfil")
    usuari = input("Disme l'usuari d'Instagram que vols buscar: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c propic".format(usuari), shell=True)
    enviarDocumento("/app/Osintgram/output/{}_propic.jpg".format(usuari))
    subprocess.call("cd Osintgram/output/ && rm -rf ./*", shell=True)

def photos():
    enviarMensaje("Imatge pujades")
    usuari = input("Disme l'usuari d'Instagram que vols buscar: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c photos".format(usuari), shell=True)
    subprocess.call("cd /app/Osintgram/output && zip -r imatges.zip *",shell=True)
    enviarDocumento("/app/Osintgram/output/imatges.zip")
    subprocess.call("cd Osintgram/output/ && rm -rf ./*", shell=True)

def addrs():
    enviarMensaje("Adreces")
    usuari = input("Disme l'usuari d'Instagram del qual vols buscar les direccions a les imatges: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c addrs -f".format(usuari), shell=True)
    enviarDocumento("/app/Osintgram/output/{}_addrs.txt".format(usuari))
def fwersemail():
    enviarMensaje("Emails")
    usuari = input("Disme l'usuari d'Instagram del qual vols buscar el correu electrònic: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c fwersemail -f".format(usuari), shell=True)
    enviarDocumento("/app/Osintgram/output/{}_fwersemail.txt".format(usuari))

def info():
    enviarMensaje("Info")
    usuari = input("Disme l'usuari d'Instagram del qual vols obtenir informació: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c info -f".format(usuari), shell=True)

def fwingsnumber():
    enviarMensaje("Numeros de mobil")
    usuari = input("Disme l'usuari d'Instagram del qual vols obtenir el número de telèfon dels usuaris seguits de l'objectiu: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c fwingsnumber -f".format(usuari), shell=True)
    enviarDocumento("/app/Osintgram/output/{}_fwingsnumber.txt".format(usuari))

def followings():
    enviarMensaje("Nom d'usuari")
    usuari = input("Disme l'usuari d'Instagram del qual vols obtenir el nom dels usuaris seguits de l'objectiu: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c followings -f".format(usuari), shell=True)
    enviarDocumento("/app/Osintgram/output/{}_followings.txt".format(usuari))


def demanaNumeroEnter():
    correcte=False
    num=0
    while(not correcte):
        try:
            num = int(input("Introdueix un numero de l'1 al 8: "))
            correcte=True
        except ValueError:
            print('Error, Introdueix una opcio del menú:')

    return num

sortir = False
opcion = 0

while not sortir:
    print ("------------------------")
    print ("Opció 1. Opcions OSINTGRAM")
    print ("Opció 2. Veure foto perfil Instagram:")
    print ("Opció 3. Veure fotos públicades a Instagram:")
    print ("Opció 4. Obtenir totes les fotos registrades dirigides a les fotos de destinació")
    print ("Opció 5. Obteniu el correu electrònic dels seguidors de l'objectiu")
    print ("Opció 6. Obtenir l'informació de l'objectiu")
    print ("Opció 7. Obtenir el número de telèfon dels usuaris seguits de l'objectiu:")    
    print ("Opció 8. Obtenir el nom d'usuari dels usuaris seguits de l'objectiu:")    
    print ("9. Sortir")
    print ("------------------------")

    print ("Escull una opció")

    opcion = demanaNumeroEnter()

    if opcion == 1:
        print(" ")
        print("Opcions OSINTGRAM: ")
        print(" ")
        print(" - captions        Obteniu subtítols de les fotos de l'usuari       ")
        print(" - comments        Obteniu comentaris totals de les publicacions de l'objectiu   ")
        print(" - followers       Aconsegueix seguidors objectiu")
        print(" - followings      Aconsegueix que els usuaris segueixin l'objectiu")
        print(" - hashtags        Obteniu hashtags utilitzats per l'objectiu")
        print(" - likes           Aconsegueix el total de M'agrada de les publicacions de l'objectiu")
        print(" - mediatype       Obteniu el tipus de publicacions de l'usuari (foto o vídeo)")
        print(" - photodes        Obteniu una descripció de les fotos de l'objectiu ")
        print(" - stories         Descarregar històries d'usuari ")
        print(" - tagged          Obteniu una llista d'usuaris etiquetats per objectiu")
        print(" - wcommented      Obteniu una llista dels usuaris que han comentat les fotos de l'objectiu")
        print(" - wtagged         Obteniu una llista d'usuaris que han etiquetat l'objectiu")

    elif opcion == 2:
        propic()
    elif opcion == 3:
        photos()
    elif opcion == 4:
        addrs()
    elif opcion == 5:
        fwersemail()
    elif opcion == 6:
        info()
    elif opcion == 7:
        fwingsnumber()
    elif opcion == 8:
        followings()
    elif opcion == 9:
        sortir = True
    else:
        print ("Introdueix un numero entre 1 y 7")


print ("Fi osintgram")
exec(open("main.py").read())


