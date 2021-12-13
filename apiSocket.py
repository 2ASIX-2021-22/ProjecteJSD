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
    print ("Opció 1. Obtenir la IP del meu dispositiu")
    print ("Opció 2. Obtenir la ip pública de un domini:")
    print ("Opció 3. Obtenir els ports oberts d'una IP pública:")
    print ("4. Tornar al menú")
    print ("------------------------")

    print ("Escull una opció")

    opcion = demanaNumeroEnter()

    if opcion == 1:
        exec(open("obtenirIpHostname.py").read())
    elif opcion == 2:
        exec(open("obtenirIpPublica.py").read())   
    elif opcion == 3:
        exec(open("obtenirPort.py").read()) 
    elif opcion == 4:
        print("Tornar al menú")
        exec(open("main.py").read())
    else:
        print ("Introduce un numero entre 1 y 4")

print ("Fi")