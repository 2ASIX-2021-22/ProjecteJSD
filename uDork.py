#!/bin/python
import subprocess
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introdueix un numero de l'1 al 6: "))
            correcto=True
        except ValueError:
            print('Error, Introdueix una opcio del menú:')
     
    return num
 
salir = False
opcion = 0

def menu_ajuda():
    print("Opció 1")
    print("------------OPCIONS---------------")
    print("-e <extension> / <all> : cerca fitxers per extensió. Utilitzeu-ho \"all\" per buscar fitxers en les extensions de la llista.")
    print("-s <text> / <all>: cerca text al contingut del lloc web.")
    print("-u <string> / <all> : llista la cadena de text al títol del lloc.")
    print("-t <cadena> / <tot> : enumera la cadena de text al títol del lloc.")
    print("-g <dork_name> / <all> : ataca un lloc amb una llista predefinida de dorks. Revisa la llista \"./uDork -l\".")
    print("-l : Mostra la llista de dorks predefinits (Exploit-DB).")
    print("-f <custom_list> : Utilitzeu la vostra pròpia llista personalitzada de idiotes.")
    print("-p <number> : nombre de pàgines per cercar a Google. (Per defecte 1 pàgina).")
    print("-o <name_file> : exporta els resultats a un fitxer.")
    print("================================ EXEMPLE ===================================")
    print("Exemple Ús: ./uDork.sh domini.com -e extensió")

def menu_extensio():
    print ("Opció 2")
    domini=input("introdueix un nom de un domini: ")
    extensio=input("introdueix la extensio dels fitxers que vols buscar (all, pdf, xml, xls, xlsx, doc, docx): ")
    pagines=input("En quantes pagines el vols buscar: ")
    exportar=input("Vols exportar els resultats? ")
    if exportar == "si":
        nom_fitxer=input("Introdueix el nom del fitxer: ")
        subprocess.call("cd uDork &&  ./uDork.sh {} -e {} -p {} -o {}".format(domini, extensio, pagines, nom_fitxer), shell=True)
    elif exportar == "no":
        subprocess.call("cd uDork &&  ./uDork.sh {} -e {} -p {}".format(domini, extensio, pagines), shell=True)
    else:
        print("Introdueix \"si\" o \"no\"")
def menu_pagina():
    print ("Opció 3")
    domini=input("introdueix un nom de un domini: ")
    paraula=input("introdueix la paraula que vols buscar: ")
    pagines=input("En quantes pagines el vols buscar: ")
    exportar=input("Vols exportar els resultats? ")
    if exportar == "si":
        nom_fitxer=input("Introdueix el nom del fitxer: ")
        subprocess.call("cd uDork &&  ./uDork.sh {} -s {} -p {} -o {}".format(domini, paraula, pagines, nom_fitxer), shell=True)
    elif exportar == "no":
        subprocess.call("cd uDork &&  ./uDork.sh {} -s {} -p {}".format(domini, paraula, pagines), shell=True)
    else:
        print("Introdueix \"si\" o \"no\"")
def menu_url():
    print ("Opció 4")
    domini=input("introdueix un nom de un domini: ")
    paraula=input("introdueix la paraula que vols buscar: ")
    pagines=input("En quantes pagines el vols buscar: ")
    exportar=input("Vols exportar els resultats? ")
    if exportar == "si":
        nom_fitxer=input("Introdueix el nom del fitxer: ")
        subprocess.call("cd uDork &&  ./uDork.sh {} -u {} -p {} -o {}".format(domini, paraula, pagines, nom_fitxer), shell=True)
    elif exportar == "no":
        subprocess.call("cd uDork &&  ./uDork.sh {} -u {} -p {}".format(domini, paraula, pagines), shell=True)
    else:
        print("Introdueix \"si\" o \"no\"")
def menu_titol():
    print ("Opció 5")
    domini=input("introdueix un nom de un domini: ")
    paraula=input("introdueix la paraula que vols buscar: ")
    pagines=input("En quantes pagines el vols buscar: ")
    exportar=input("Vols exportar els resultats? ")
    if exportar == "si":
        nom_fitxer=input("Introdueix el nom del fitxer: ")
        subprocess.call("cd uDork &&  ./uDork.sh {} -t {} -p {} -o {}".format(domini, paraula, pagines, nom_fitxer), shell=True)
        subprocess.call("ls")
    elif exportar == "no":
        subprocess.call("cd uDork &&  ./uDork.sh {} -t {} -p {}".format(domini, paraula, pagines), shell=True)
    else:
        print("Introdueix \"si\" o \"no\"")
while not salir:
    print ("------------------------")
    print ("Opció 1. Ajuda")
    print ("Opció 2. Buscar fitxers en extensió")
    print ("Opció 3. Buscar la paraula introduida en les pagines del domini introduit")
    print ("Opció 4. Buscar la paraula introduida en les URLs del domini introduit")
    print ("Opció 5. Buscar la paraula introduida en el titol del domini introduit")
    print ("Opció 6. Sortir")
    print ("------------------------")
    print ("Escull una opció")
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
        print ("Introduce un numero entre 1 y 6")
 
print ("Fi")
