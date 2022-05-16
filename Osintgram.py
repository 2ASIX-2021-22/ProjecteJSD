#!/bin/python

# Import per cridar l'eina theHarvester
import asyncio
import subprocess
from bot_telegram import enviarFotos, enviarMensaje, enviarDocumento
def credentials():
#    usuari = input("Disme l'usuari de l'Instagram: ")
#    password = input("Disme la contrasenya de l'usuari de l'Instagram: ")
    subprocess.call("cd ./Osintgram && make setup", shell=True)
credentials()

    
def propic():
    usuari = input("    Disme l'usuari d'Instagram que vols buscar: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c propic".format(usuari), shell=True)
    enviarMensaje("Imatge de perfil")
    #enviarDocumento("/app/Osintgram/output/{}_propic.jpg".format(usuari))
    enviarFotos("./Osintgram/output/{}_propic.jpg".format(usuari))
    subprocess.call("cd Osintgram/output/ && rm -rf ./*", shell=True)

def photos():
    usuari = input("    Disme l'usuari d'Instagram que vols buscar: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c photos".format(usuari), shell=True)
    subprocess.call("cd ./Osintgram/output && zip -r imatges.zip *",shell=True)
    enviarMensaje("Imatge pujades")
    enviarDocumento("./Osintgram/output/imatges.zip")
    subprocess.call("cd Osintgram/output/ && rm -rf ./*", shell=True)

def addrs():
    usuari = input("    Disme l'usuari d'Instagram del qual vols buscar les direccions a les imatges: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c addrs -f".format(usuari), shell=True)
    enviarMensaje("Adreces")
    enviarDocumento("/app/Osintgram/output/{}_addrs.txt".format(usuari))
    subprocess.call("cd Osintgram/output/ && rm -rf ./*", shell=True)
def fwersemail():
    usuari = input("    Disme l'usuari d'Instagram del qual vols buscar el correu electrònic: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c fwersemail -f".format(usuari), shell=True)
    enviarMensaje("Emails")
    enviarDocumento("/app/Osintgram/output/{}_fwersemail.txt".format(usuari))
    subprocess.call("cd Osintgram/output/ && rm -rf ./*", shell=True)

def info():
    usuari = input("    Disme l'usuari d'Instagram del qual vols obtenir informació: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c info -f".format(usuari), shell=True)
    enviarMensaje("Info")
    subprocess.call("cd Osintgram/output/ && rm -rf ./*", shell=True)

def fwingsnumber():
    usuari = input("    Disme l'usuari d'Instagram del qual vols obtenir el número de telèfon dels usuaris seguits de l'objectiu: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c fwingsnumber -f".format(usuari), shell=True)
    enviarMensaje("Numeros de mobil")
    enviarDocumento("/app/Osintgram/output/{}_fwingsnumber.txt".format(usuari))
    subprocess.call("cd Osintgram/output/ && rm -rf ./*", shell=True)

def followings():
    usuari = input("    Disme l'usuari d'Instagram del qual vols obtenir el nom dels usuaris seguits de l'objectiu: ")
    subprocess.call("cd Osintgram && python3 ./main.py {} -c followings -f".format(usuari), shell=True)
    enviarMensaje("Nom d'usuari")
    enviarDocumento("/app/Osintgram/output/{}_followings.txt".format(usuari))
    subprocess.call("cd Osintgram/output/ && rm -rf ./*", shell=True)

def demanaNumeroEnter():
    correcte=False
    num=0
    while(not correcte):
        try:
            num = int(input("    Introdueix un numero de l'1 al 8: "))
            correcte=True
        except ValueError:
            print('    Error, Introdueix una opcio del menú:')

    return num

sortir = False
opcion = 0

while not sortir:
    print ("    ------------------------")
    print ("    Opció 1. Veure foto perfil Instagram:")
    print ("    Opció 2. Veure fotos públicades a Instagram:")
    print ("    Opció 3. Obtenir totes les fotos registrades dirigides a les fotos de destinació")
    print ("    Opció 4. Obteniu el correu electrònic dels seguidors de l'objectiu")
    print ("    Opció 5. Obtenir l'informació de l'objectiu")
    print ("    Opció 6. Obtenir el número de telèfon dels usuaris seguits de l'objectiu:")    
    print ("    Opció 7. Obtenir el nom d'usuari dels usuaris seguits de l'objectiu:")    
    print ("    Opció 8. Tornar al menú principal:")
    print ("    ------------------------")

    print ("    Escull una opció: ")

    opcion = demanaNumeroEnter()

    if opcion == 1:
        propic()
    elif opcion == 2:
        photos()
    elif opcion == 3:
        addrs()
    elif opcion == 4:
        fwersemail()
    elif opcion == 5:
        info()
    elif opcion == 6:
        fwingsnumber()
    elif opcion == 7:
        followings()
    elif opcion == 8:
        sortir = True
    else:
        print ("    Introdueix un número entre l'1 i 8")


print ("    Menú principal: ")
exec(open("main.py").read())


