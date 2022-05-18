#!/bin/python
import subprocess
from sys import stdout
from bot_telegram import enviarMensaje, enviarDocumento


def demanaNumeroEnter():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("    Introdueix un número de l'1 al 4: "))
            correcto=True
        except ValueError:
            print(' Error, Introdueix una opció del menú:')
    return num

def auditoriaCompleta():
    ip_host = input("    Introdueix la IP d'un dispositiu: ")
    f = open("auditoriaCompleta.txt", "w")
    subprocess.call("./enum4linux.pl -A {}".format(ip_host), shell=True, stdout=f)
    subprocess.call("./enum4linux.pl -A {}".format(ip_host), shell=True)
    enviarDocumento("./auditoriaCompleta.txt")
def auditoriaUsuaris():
    ip_host = input("    Introdueix la IP d'un dispositiu: ")
    f = open("llistaUsuarisEnnum.txt", "w")
    subprocess.call("./enum4linux.pl -U {}".format(ip_host), shell=True, stdout=f)
    subprocess.call("./enum4linux.pl -U {}".format(ip_host), shell=True)
    enviarDocumento("./llistaUsuarisEnnum.txt")
def auditoriaSO():
    ip_host = input("    Introdueix la IP d'un dispositiu: ")
    f = open("llistaSOEnnum.txt", "w")
    subprocess.call("./enum4linux.pl -o {}".format(ip_host), shell=True, stdout=f)
    subprocess.call("./enum4linux.pl -o {}".format(ip_host), shell=True)
    enviarDocumento("./llistaSOEnnum.txt")


sortir = False
opcio = 0
 
while not sortir:
    print("")
    print ("    ------------Auditoria recursos SMB-------------")
    print ("    Opció 1. Auditoria Completa")
    print ("    Opció 2. Llistar usuaris")
    print ("    Opció 3. Auditoria S.O.")
    print ("    Opció 4. Sortir")
 
    print ("\n    Tria una opció: ")
    print("")
    opcio = demanaNumeroEnter()
 
    if opcio == 1:
        auditoriaCompleta()
    elif opcio == 2:
        auditoriaUsuaris()
    elif opcio == 3:
        auditoriaSO()
    elif opcio == 4:
        sortir = True
    else:
        print ("    Introdueix un número entre 1 i 4")

print ("    Fi de l'auditoria ssh")
exec(open("main.py").read())