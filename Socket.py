#!/bin/python

# Import per cridar l'eina theHarvester
import asyncio
import subprocess



def demanaNumeroEnter():
    correcte=False
    num=0
    while(not correcte):
        try:
            num = int(input("    Introdueix un número de l'1 al 4: "))
            correcte=True
        except ValueError:
            print('    Error, introdueix una opció del menú:')

    return num

sortir = False
opcion = 0

while not sortir:
    print ("    ------------------------")
    print ("    Opció 1. Obtenir la IP del meu dispositiu")
    print ("    Opció 2. Obtenir la IP pública de un domini:")
    print ("    Opció 3. Obtenir els ports oberts d'una IP pública:")
    print ("    Opció 4. Tornar al menú")
    print ("    ------------------------")

    print ("    Escull una opció")

    opcion = demanaNumeroEnter()

    if opcion == 1:
        exec(open("obtenirIpHostname.py").read())
    elif opcion == 2:
        exec(open("obtenirIpPublica.py").read())   
    elif opcion == 3:
        exec(open("obtenirPort.py").read()) 
    elif opcion == 4:
        sortir = True
        print("    Menú principal:")
        exec(open("main.py").read())
    else:
        print ("    Introdueix un número entre l'1 i el 4")