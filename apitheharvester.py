#!/bin/python

# Import per cridar l'eina theHarvester
import asyncio
import subprocess

#Import per obrir un navegador
import webbrowser
from bot_telegram import enviarMensaje,enviarDocumento

def demanaNumeroEnter():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("    Introdueix un número de l'1 al 3: "))
            correcto=True
        except ValueError:
            print('    Error, introdueix una opcio del menú:')

    return num

salir = False
opcion = 0

while not salir:
    print ("    ------------------------")
    print ("    Opció 1. Execució")
    print ("    Opció 2. Mostra i envia els resultats")
    print ("    Opció 3. Tornar al menú")
    print ("    ------------------------")

    print ("    Escull una opció")

    opcion = demanaNumeroEnter()

    if opcion == 1:
      domain = input("    Disme el domini que vols buscar: ")
      limit = input("    Disme el limit de resultats: ")
      fontDades = "google"
      subprocess.call("cd theHarvester && python3 ./theHarvester.py -d {} -l {} -b {} -f resulttheharvester.html".format(domain, limit, fontDades), shell=True)
    elif opcion == 2:
        print("    Mostrar resultats al navegador: ")
        url=("./theHarvester/resulttheharvester.xml")
        enviarDocumento("./theHarvester/resulttheharvester.xml")
        chrome_path = '/usr/bin/google-chrome %s'
        webbrowser.get(chrome_path).open(url)     
    elif opcion == 3:
        salir = True
    else:
        print ("    Introdueix un número entre l'1 i el 3")

print ("    Menú principal: ")
exec(open("main.py").read())


