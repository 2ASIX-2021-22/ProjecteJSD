#!/bin/python

# Import per cridar l'eina theHarvester
import asyncio
import subprocess

def demanaNumeroEnter():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introdueix un numero de l'1 al 3: "))
            correcto=True
        except ValueError:
            print('Error, Introdueix una opcio del menú:')

    return num

salir = False
opcion = 0

while not salir:
    print ("------------------------")
    print ("Opció 1. Opcions OSINTGRAM")
    print ("Opció 2. Veure foto perfil instagram:")
    print ("3. Sortir")
    print ("------------------------")

    print ("Escull una opció")

    opcion = demanaNumeroEnter()

    if opcion == 1:
        print(" ")
        print("Opcions OSINTGRAM: ")
        print(" ")
        print(" - addrs           Obteniu totes les fotos registrades dirigides a les fotos de destinació       ")
        print(" - captions        Obteniu subtítols de les fotos de l'usuari       ")
        print(" - comments        Obteniu comentaris totals de les publicacions de l'objectiu   ")
        print(" - followers       Aconsegueix seguidors objectiu")
        print(" - followings      Aconsegueix que els usuaris segueixin l'objectiu")
        print(" - fwersemail      Obteniu el correu electrònic dels seguidors objectiu")
        print(" - fwingsemail     Obteniu el correu electrònic dels usuaris seguits per l'objectiu")
        print(" - fwersnumber     Obteniu el número de telèfon dels seguidors objectiu")
        print(" - fwingsnumber    Obteniu el número de telèfon dels usuaris seguit de l'objectiu")
        print(" - hashtags        Obteniu hashtags utilitzats per l'objectiu")
        print(" - info            Obteniu informació de l'objectiu")
        print(" - likes           Aconsegueix el total de M'agrada de les publicacions de l'objectiu")
        print(" - mediatype       Obteniu el tipus de publicacions de l'usuari (foto o vídeo)")
        print(" - photodes        Obteniu una descripció de les fotos de l'objectiu ")
        print(" - photos          Baixeu les fotos de l'usuari a la carpeta de sortida")
        print(" - propic          Descarrega la foto de perfil de l'usuari")
        print(" - stories         Descarregar històries d'usuari ")
        print(" - tagged          Obteniu una llista d'usuaris etiquetats per objectiu")
        print(" - wcommented      Obteniu una llista dels usuaris que han comentat les fotos de l'objectiu")
        print(" - wtagged         Obteniu una llista d'usuaris que han etiquetat l'objectiu")

    elif opcion == 2:
        usuari = input("Disme l'usuari d'instagram que vols buscar: ")
        subprocess.call("cd Osintgram && python3 ./main.py {} -c propic".format(usuari), shell=True)
        subprocess.call("cd Osintgram/output && ls")
    elif opcion == 3:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")

print ("Fi")


