#!/bin/python
import subprocess
from sys import stdout
from bot_telegram import enviarMensaje, enviarDocumento


def demanaNumeroEnter():
    correcto=False
    num=0
    while(not correcto):
        try:
            num = int(input("    Introdueix un número de l'1 al 5: "))
            correcto=True
        except ValueError:
            print ('    Error, Introdueix una opció del menú:')
    return num

def auditoriaCompleta():
    ip_host = input("    Introdueix la IP d'un dispositiu: ")
    f = open("complet.txt", "w")
    subprocess.call("python3 ./ssh-audit/ssh-audit.py {}".format(ip_host), shell=True, stdout=f)
    subprocess.call("    python3 ./ssh-audit/ssh-audit.py {}".format(ip_host), shell=True)
    enviarDocumento("./complet.txt")
def auditoriaFails():
    ip_host = input("    Introdueix la IP d'un dispositiu: ")
    f = open("fails.txt", "w")
    subprocess.call("python3 ./ssh-audit/ssh-audit.py --level fail {}".format(ip_host), shell=True, stdout=f)
    subprocess.call("    python3 ./ssh-audit/ssh-audit.py --level fail {}".format(ip_host), shell=True)
    enviarDocumento("./fails.txt")

def auditoriaWarn():
    ip_host = input("    Introdueix la IP d'un dispositiu: ")
    f = open("warn.txt", "w")
    subprocess.call("python3 ./ssh-audit/ssh-audit.py --level warn {}".format(ip_host), shell=True, stdout=f)
    subprocess.call("    python3 ./ssh-audit/ssh-audit.py --level warn {}".format(ip_host), shell=True)
    enviarDocumento("./warn.txt")

def auditoriaInfo():
    ip_host = input("    Introdueix la IP d'un dispositiu: ")
    f = open("info.txt", "w")
    subprocess.call("python3 ./ssh-audit/ssh-audit.py --level info {}".format(ip_host), shell=True, stdout=f)
    subprocess.call("    python3 ./ssh-audit/ssh-audit.py --level info {}".format(ip_host), shell=True)
    enviarDocumento("./info.txt")


sortir = False
opcio = 0
 
while not sortir:
    print("")
    print ("    ------------Auditoria SSH-------------")
    print ("    1. Auditoria completa")
    print ("    2. Auditoria 'FAILS'")
    print ("    3. Auditoria 'WARNS'")
    print ("    4. Auditoria 'INFO'")
    print ("    5. Tornar al menú principal")
 
    print ("    Tria una opció")
    print("")
    opcio = demanaNumeroEnter()
 
    if opcio == 1:
        auditoriaCompleta()
    elif opcio == 2:
        auditoriaFails()
    elif opcio == 3:
        auditoriaWarn()
    elif opcio == 4:
        auditoriaInfo()
    elif opcio == 5:
        sortir = True
    else:
        print ("    Introdueix un número entre l'1 i el 5")

print ("    Menú principal")
exec(open("main.py").read())