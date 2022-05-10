#!/bin/python

def DemanaNumeroEnter():
 
    correcte=False
    num=0
    while(not correcte):
        try:
            num = int(input("    Introdueix un número de l'1 al 8: "))
            correcte=True
        except ValueError:
            print('      Error, introdueix una opció del menú:')
     
    return num
 
sortir = False
opcio = 0

while not sortir:
    print ("    ._____. ._____. ._________________. ._____. ._____.")
    print ("    | ._. | | ._. | | ._____________. | | ._. | | ._. |")
    print ("    | !_| |_|_|_! | | !_____________! | | !_| |_|_|_! |")
    print ("    !___| |_______! !_________________! !___| |_______!")
    print ("    .___|_|_| |_____________________________|_|_| |___.")
    print ("    | ._____| |_________________________________| |_. |")
    print ("    | !_! | | |                             | | ! !_! |")
    print ("    !_____! | |                             | | !_____!")
    print ("    ._____. | |       ##  ######  ########  | | ._____.")
    print ("    | ._. | | |       ## ##    ## ##     ## | | | ._. |")
    print ("    | | | | | |       ## ##       ##     ## | | | | | |")
    print ("    | | | | | |       ##  ######  ##     ## | | | | | |")
    print ("    | !_! | | | ##    ##       ## ##     ## | | ! !_! |")
    print ("    !_____! | | ##    ## ##    ## ##     ## | | !_____!")
    print ("    ._____. | |  ######   ######  ########  | | ._____.")
    print ("    | ._. | | |                             | | | ._. |")
    print ("    | !_| |_|_|_____________________________| |_|_|_! |")
    print ("    !___| |_________________________________| |_______!")      
    print ("    | ._____| |_________________________________| |_. |")
    print ("    | !_! | | |                             | | ! !_! |")
    print ("    !_____! | |   Opció 1. API de Shodan    | | !_____!")
    print ("    ._____. | |   Opció 2. TheHarvester     | | ._____.")
    print ("    | ._. | | |   Opció 3. Auditoria SSH    | | | ._. |")
    print ("    | | | | | |   Opció 4. uDork            | | | | | |")
    print ("    | | | | | |   Opció 5. Osintgram        | | | | | |")
    print ("    | !_! | | |   Opció 6. Python.Socket    | | ! !_! |")
    print ("    !_____! | |   Opció 7. Nmap             | | !_____!")
    print ("    ._____. | |   Opció 8. Sortir           | | ._____.")
    print ("    | ._. | | |                             | | | ._. |")
    print ("    | !_| |_|_|_____________________________| |_|_|_! |")
    print ("    !___| |_________________________________| |_______!")
    print ("    .___|_|_| |___. ._________________. .___|_|_| |___.")
    print ("    | ._____| |_. | | ._____________. | | ._____| |_. |")
    print ("    | !_! | | !_! | | !_____________! | | !_! | | !_! |")
    print ("    !_____! !_____! !_________________! !_____! !_____!")
    print ("    ._____. ._____. ._________________. ._____. ._____.")

     
    print ("\n    Escull una opció")
 
    opcio = DemanaNumeroEnter()
 
    if opcio == 1:
        print ("Opció 1")
        exec(open("APISHODAN.py").read())
    elif opcio == 2:
        print ("Opció 2")
        exec(open("apitheharvester.py").read())
    elif opcio == 3:
        print("Opció 3")
        exec(open("ssh-audit.py").read())
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
        print ("    Introdueix un número entre l'1 i 8")
 
print ("    Fi del programa")
