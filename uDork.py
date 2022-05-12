#!/bin/python
import subprocess
from bot_telegram import enviarDocumento
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("    Introdueix un número de l'1 al 6: "))
            correcto=True
        except ValueError:
            print('    Error, Introdueix una opció del menú:')
     
    return num
 
salir = False
opcion = 0

def menu_ajuda():
    print("    Opció 1")
    print("    ------------OPCIONS---------------")
    print("    -e <extension> / <all> : cerca fitxers per extensió. Utilitzeu-ho \"all\" per buscar fitxers en les extensions de la llista.")
    print("    -s <text> / <all>: cerca text al contingut del lloc web.")
    print("    -u <string> / <all> : localitza cadenes de text dins de l'URL.")
    print("    -t <string> / <all> : enumera la cadena de text al títol del lloc.")
    print("    -g <dork_name> / <all> : ataca un lloc amb una llista predefinida de dorks. Revisa la llista \"./uDork -l\".")
    print("    -l : Mostra la llista de dorks predefinits (Exploit-DB).")
    print("    -f <custom_list> : Utilitzeu la vostra pròpia llista personalitzada de dorks.")
    print("    -p <number> : nombre de pàgines per cercar a Google. (Per defecte 1 pàgina).")
    print("    -o <name_file> : exporta els resultats a un fitxer.")
    print("    ================================ EXEMPLE ===================================")
    print("    Exemple Ús: ./uDork.sh domini.com -e extensió")

def menu_extensio():
    print("    Opció 2")
    domini=input("    Introdueix un nom d'un domini: ")
    extensio=input("    Introdueix l'extensió dels fitxers que vols buscar (all, pdf, xml, xls, xlsx, doc, docx): ")
    pagines=input("    En quantes pàgines el vols buscar: ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -e {} -p {} -o extension.txt".format(domini, extensio, pagines), shell=True)
    enviarDocumento("./uDork/extension.txt")
def menu_pagina():
    print("    Opció 3")
    domini=input("    Introdueix un nom d'un domini: ")
    paraula=input("    Introdueix la paraula que vols buscar: ")
    pagines=input("    En quantes pàgines el vols buscar: ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -s {} -p {} -o pagines.txt".format(domini, paraula, pagines), shell=True)
    enviarDocumento("./uDork/pagines.txt")

def menu_url():
    print("    Opció 4")
    domini=input("    Introdueix un nom d'un domini: ")
    paraula=input("    Introdueix la paraula que vols buscar: ")
    pagines=input("    En quantes pàgines el vols buscar: ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -u {} -p {} -o urls.txt".format(domini, paraula, pagines), shell=True)
    enviarDocumento("./uDork/urls.txt")

def menu_titol():
    print("    Opció 5")
    domini=input("    Introdueix un nom de un domini: ")
    paraula=input("    Introdueix la paraula que vols buscar: ")
    pagines=input("    En quantes pàgines vols buscar: ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -t {} -p {} -o titols.txt".format(domini, paraula, pagines), shell=True)
    enviarDocumento("./uDork/titols.txt")

while not salir:
    print("    ------------------------")
    print("    Opció 1. Ajuda")
    print("    Opció 2. Buscar fitxers en extensió")
    print("    Opció 3. Buscar la paraula introduïda en les pàgines del domini introduït")
    print("    Opció 4. Buscar la paraula introduïda en les URLs del domini introduït")
    print("    Opció 5. Buscar la paraula introduïda en el títol del domini introduït")
    print("    Opció 6. Tornar al menú principal")
    print("    ------------------------")
    print("    Escull una opció")
    opcion = pedirNumeroEntero()
    
    if opcion == 1:
        menu_ajuda()
    elif opcion == 2:
        menu_extensio()
    elif opcion == 3:
        menu_pagina()
    elif opcion == 4:
        menu_url()
    elif opcion == 5:
        menu_titol()
    elif opcion == 6:
        salir = True
    else:
        print ("    Introdueix un número entre l'1 i 6")
 
print ("    Menú Principal:")
