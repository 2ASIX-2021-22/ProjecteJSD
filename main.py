#!/bin/python

def DemanaNumeroEnter():
 
    correcte=False
    num=0
    while(not correcte):
        try:
            num = int(input("Introdueix un numero de l'1 al 7: "))
            correcte=True
        except ValueError:
            print('Error, Introdueix una opcio del menú:')
     
    return num
 
sortir = False
opcion = 0
 
while not sortir:
    print ("------------------------")
    print ("Opció 1. API de Shodan")
    print ("Opció 2. theHarvester")
    print ("Opció 3. Bot telegram")
    print ("Opció 4. uDork")
    print ("Opció 5. Osintgram")
    print ("Opció 6. Socket")
    print ("Opció 7. Sortir")
    print ("------------------------")
     
    print ("Escull una opció")
 
    opcion = DemanaNumeroEnter()
 
    if opcion == 1:
        print ("Opció 1")
        exec(open("APISHODAN.py").read())
    elif opcion == 2:
        print ("Opció 2")
        exec(open("apitheharvester.py").read())
    elif opcion == 3:
        print("Opció 3")
    elif opcion == 4:
        print("Opció 4")
        exec(open("uDork.py").read())
    elif opcion == 5:
        print("Opció 5")
        exec(open("apiOsintgram.py").read())
    elif opcion == 6:
        print("Opció 6")
        exec(open("apiSocket.py").read())
    elif opcion == 7:
        sortir = True
    else:
        print ("Introduce un numero entre 1 y 7")
 
print ("Fi del programa")