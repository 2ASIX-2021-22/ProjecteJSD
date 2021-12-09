#!/bin/python
import subprocess
def pedirNumeroEntero():
 
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("Introdueix un numero de l'1 al 4: "))
            correcto=True
        except ValueError:
            print('Error, Introdueix una opcio del menú:')
     
    return num
 
salir = False
opcion = 0

def menu_ajuda():
    print("Opció 1")
    print("------------OPCIONS---------------")
    print("     -e <extension> / <all> : cerca fitxers per extensió. Utilitzeu-ho tot per trobar l'extensió de la llista.")
    print("     -s <text> / <all>: cerca text al contingut del lloc web.")
    print("     -u <cadena> / <tot>: localitza cadenes de text a l'URL.")
    print("     -u <string> / <all> : llista la cadena de text al títol del lloc.")
    print("     -t <string> / <all> : ataca un lloc amb una llista predefinida de dorks. Revisa la llista \"./uDork -l\".")
    print("     -l : Mostra la llista de dorks predefinits (Exploit-DB).")
    print("     -f <custom_list> : Utilitzeu la vostra pròpia llista personalitzada de idiotes.")
    print("     -p <number> : nombre de pàgines per cercar a Google. (Per defecte 1 pàgina).")
    print("     -o <name_file> : exporta els resultats a un fitxer.")

def menu_execucio():
    print ("Opció 2")
    domini=input("introdueix un nom de un domini: ")
    extensio=input("introdueix la extensio dels fitxers que vols buscar (all, pdf, ...) : ")
    subprocess.call("cd uDork &&  ./uDork.sh {} -e {}".format(domini, extensio), shell=True)
def menu_avançat():
    print ("Opció 3")
    domini=input("introdueix un nom de un domini: ")
    pentesting=input("introdueix on vols fer la auditories/pentesting (admin, directories, usernames, passwords, webservers, vulnerable_files, vulnerable_servers, error_messages, portal_logins, vulnerable_networks, devices : ")
    subprocess.call("cd uDork/ && ./uDork.sh {} -g {}".format(domini, pentesting), shell=True)

while not salir:
    print ("------------------------")
    print ("Opció 1. Ajuda")
    print ("Opció 2. Execució")
    print ("Opció 3. Auditoria")
    print ("Opció 4. Sortir")
    print ("------------------------")
    print ("Escull una opció")
    opcion = pedirNumeroEntero()
    
    if opcion == 1:
        menu_ajuda()
    elif opcion == 2:
        menu_execucio()
    elif opcion == 3:
        menu_avançat()
    elif opcion == 4:
        salir = True
    else:
        print ("Introduce un numero entre 1 y 4")
 
print ("Fi")
