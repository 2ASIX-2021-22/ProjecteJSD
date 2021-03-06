#!/bin/python
import subprocess
from bot_telegram import enviarDocumento


def menu_extensio():
    print("    Opció 1")
    domini=input("    Introdueix un nom d'un domini: ")
    extensio=input("    Introdueix l'extensió dels fitxers que vols buscar (pdf, xml, xls, xlsx, doc, docx): ")
    pagines=input("    En quantes pàgines el vols buscar: ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -e {} -p {} -o extension.txt".format(domini, extensio, pagines), shell=True)
    enviarDocumento("./uDork/extension.txt")

def menu_pagines():
    print("    Opció 2")
    domini=input("    Introdueix un nom d'un domini: ")
    paraula=input("    Introdueix la paraula que vols buscar: ")
    pagines=input("    En quantes pàgines el vols buscar: ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -s {} -p {} -o pagines.txt".format(domini, paraula, pagines), shell=True)
    enviarDocumento("./uDork/pagines.txt")

def menu_url():
    print("    Opció 3")
    domini=input("    Introdueix un nom d'un domini: ")
    paraula=input("    Introdueix la paraula que vols buscar: ")
    pagines=input("    En quantes pàgines el vols buscar: ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -u {} -p {} -o urls.txt".format(domini, paraula, pagines), shell=True)
    enviarDocumento("./uDork/urls.txt")
    
def menu_titol():
    print("    Opció 4")
    domini=input("    Introdueix un nom d'un domini: ")
    paraula=input("    Introdueix la paraula que vols buscar: ")
    pagines=input("    En quantes pàgines el vols buscar: ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -t {} -p {} -o titols.txt".format(domini, paraula, pagines), shell=True)
    enviarDocumento("./uDork/titols.txt")

def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("    Introdueix un número de l'1 al 5: "))
            correcto=True
        except ValueError:
            print('    Error, Introdueix una opció del menú:')
     
    return num
 
salir = False
opcion = 0
while not salir:
    print("    ------------------------")
    print("    Opció 1. Buscar fitxers en extensió")
    print("    Opció 2. Buscar la paraula introduïda en les pàgines del domini introduït")
    print("    Opció 3. Buscar la paraula introduïda en les URLs del domini introduït")
    print("    Opció 4. Buscar la paraula introduïda en el títol del domini introduït")
    print("    Opció 5. Tornar al menú principal")
    print("    ------------------------")
    print("    Escull una opció")
    opcion = pedirNumeroEntero()
    
    if opcion == 1:
        menu_extensio()
    elif opcion == 2:
        menu_pagines()
    elif opcion == 3:
        menu_url()
    elif opcion == 4:
        menu_titol()
    elif opcion == 5:
        salir = True
        print ("    Menú Principal:")
    else:
        print ("    Introdueix un número entre l'1 i el 5")
 
