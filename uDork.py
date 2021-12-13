#!/bin/python
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

def menu_ajuda():
    print("Opció 1")
    print("------------OPCIONS---------------")
    print("-e <extension> / <all> : cerca fitxers per extensió. Utilitzeu-ho \"all\" per buscar fitxers en les extensions de la llista.")
    print("-s <text> / <all>: cerca text al contingut del lloc web.")
    print("-u <string> / <all> : llista la cadena de text al títol del lloc.")
    print("-t <string> / <all> : ataca un lloc amb una llista predefinida de dorks. Revisa la llista \"./uDork -l\".")
    print("-l : Mostra la llista de dorks predefinits (Exploit-DB).")
    print("-f <custom_list> : Utilitzeu la vostra pròpia llista personalitzada de idiotes.")
    print("-p <number> : nombre de pàgines per cercar a Google. (Per defecte 1 pàgina).")
    print("-o <name_file> : exporta els resultats a un fitxer.")
    print("================================ EXEMPLE ===================================")
    print("Exemple Ús: ./uDork.sh domini.com -e extensió")

def menu_execucio():
    print ("Opció 2")
    domini=input("introdueix un nom de un domini: ")
    extensio=input("introdueix la extensio dels fitxers que vols buscar (all, pdf, xml, xls, xlsx, doc, docx): ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -e {}".format(domini, extensio), shell=True)
def menu_text():
    print ("Opció 3")
    domini=input("introdueix un nom de un domini: ")
    paraula=input("introdueix la paraula que vols buscar: ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -s {}".format(domini, paraula), shell=True)
def menu_cadena():
    print ("Opció 4")
    domini=input("introdueix un nom de un domini: ")
    paraula=input("introdueix la paraula que vols buscar: ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -u {}".format(domini, paraula), shell=True)

while not salir:
    print ("------------------------")
    print ("Opció 1. Ajuda")
    print ("Opció 2. Buscar fitxers en extensió")
    print ("Opció 3. Buscar la paraula ")
    print ("Opció 4. Buscar ")
    print ("Opció 5. Tornar al menú")
    print ("------------------------")
    print ("Escull una opció")
    opcion = pedirNumeroEntero()
    
    if opcion == 1:
        menu_ajuda()
    elif opcion == 2:
        menu_execucio()
    elif opcion == 3:
        menu_text()
    elif opcion == 4:
        menu_cadena()
    elif opcion == 5:
        exec(open("main.py").read())
    else:
        print ("Introduce un numero entre 1 y 5")
 
print ("Fi")
