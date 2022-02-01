#!/bin/python

# Import per cridar l'eina theHarvester
import asyncio
import subprocess

#Import per obrir un navegador
import webbrowser


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
    print ("Opció 1. Execució")
    print ("Opció 2. Mostrar resultats:")
    print ("3. Tornar al menú")
    print ("------------------------")

    print ("Escull una opció")

    opcion = demanaNumeroEnter()

    if opcion == 1:
      domain = input("Disme el domini que vols buscar: ")
      limit = input("Disme el limit de resultats: ")
      fontDades = input("Disme la font a la qual farem la busqueda: (google, googleCSE, bing, bingapi, pgp, linkedin, google-profile, people123, jigsaw, twitter, googleplus, all)")
      subprocess.call("cd theHarvester && python3 ./theHarvester.py -d {} -l {} -b {} -f resulttheharvester.html".format(domain, limit, fontDades), shell=True)
    elif opcion == 2:
        print("Mostrar resultats al navegador: ")
        url=("./theHarvester/resulttheharvester.xml")
        chrome_path = '/usr/bin/google-chrome %s'
        webbrowser.get(chrome_path).open(url)     
    elif opcion == 3:
        exec(open("main.py").read())
    else:
        print ("Introduce un numero entre 1 y 3")

print ("Fi")


