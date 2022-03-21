#!/bin/python

def DemanaNumeroEnter():
 
    correcte=False
    num=0
    while(not correcte):
        try:
            num = int(input("Introdueix un numero de l'1 al 8: "))
            correcte=True
        except ValueError:
            print('Error, Introdueix una opcio del menú:')
     
    return num
 
sortir = False
opcio = 0
 
while not sortir:
    print ("------------------------")
    print ("Opció 1. API de Shodan")
    print ("Opció 2. theHarvester")
    print ("Opció 3. Bot telegram")
    print ("Opció 4. uDork")
    print ("Opció 5. Osintgram")
    print ("Opció 6. Socket")
    print ("Opció 7. Nmap")
    print ("Opció 8. Sortir")
    print ("------------------------")
     
    print ("Escull una opció")
 
    opcio = DemanaNumeroEnter()
 
    if opcio == 1:
        print ("Opció 1")
        exec(open("APISHODAN.py").read())
    elif opcio == 2:
        print ("Opció 2")
        exec(open("apitheharvester.py").read())
    elif opcio == 3:
        print("Opció 3")
    elif opcio == 4:
        print("Opció 4")
        exec(open("uDork.py").read())
    elif opcio == 5:
        print("Opció 5")
        exec(open("apiOsintgram.py").read())
    elif opcio == 6:
        print("Opció 6")
        exec(open("apiSocket.py").read())
    elif opcio == 7:
        print("Opció 7")
        exec(open("escaneigNmap.py").read())
    elif opcio == 8:
        sortir = True
    else:
        print ("Introduce un numero entre 1 y 8")
 
print ("Fi del programa")