#!/bin/python
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

def auditoriaCompleta():
    ip_host = input("Introdueix IP d'un dispositiu: ")
    subprocess.call("python3 ./ssh-audit/ssh-audit.py {}".format(ip_host), shell=True)
def auditoriaFails():
    ip_host = input("Introdueix IP d'un dispositiu: ")
    subprocess.call("python3 ./ssh-audit/ssh-audit.py --level fail {}".format(ip_host), shell=True)
def auditoriaWarn():
    ip_host = input("Introdueix IP d'un dispositiu: ")
    subprocess.call("python3 ./ssh-audit/ssh-audit.py --level warn {}".format(ip_host), shell=True)
def auditoriaInfo():
    ip_host = input("Introdueix IP d'un dispositiu: ")
    subprocess.call("python3 ./ssh-audit/ssh-audit.py --level info {}".format(ip_host), shell=True)




sortir = False
opcio = 0
 
while not sortir:
    print("")
    print ("------------Auditoria SSH-------------")
    print ("1. Auditoria completa")
    print ("2. Auditoria 'FAILS'")
    print ("3. Auditoria 'WARNS'")
    print ("4. Auditoria 'INFO'")
    print ("5. Sortir")
 
    print ("Tria una opció: ")
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
        print ("Introdueix un número entre 1 i 5")

print ("Fi de l'auditoria ssh")
exec(open("main.py").read())