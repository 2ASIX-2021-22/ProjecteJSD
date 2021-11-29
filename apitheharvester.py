#!/bin/python

# Import per cridar l'eina theHarvester
import asyncio
import aiodns
import subprocess

def pedirNumeroEntero():
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
    print ("Opció 2. Ajuda")
    print ("3. Sortir")
    print ("------------------------")

    print ("Escull una opció")

    opcion = pedirNumeroEntero()

    if opcion == 1:
      domain=input("Disme el domini que vols buscar: ")
      subprocess.call("cd theHarvester && python3 ./theHarvester.py -d {} -l 10 -b google".format(domain), shell=True)
    elif opcion == 2:
        print("Ajuda sobre la Eina TheHarvester:")
        print("     -d busca per el domini")
        print("     -l limit sobre les busquedes (1=10)")
        print("     ")


    elif opcion == 3:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 3")

print ("Fi")


