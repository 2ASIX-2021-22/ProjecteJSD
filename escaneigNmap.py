 #!/bin/bash/python3
import nmap
import subprocess
from bot_telegram import enviarMensaje, enviarDocumento


def host_actiu():
    nm = nmap.PortScanner()
    ip_xarxa = input("    Introdueix la IP de la xarxa (exemple: 192.168.1.0/24): ")
    nm.scan(hosts = ip_xarxa, arguments='-n -sP -PE')
    up_hosts = nm.all_hosts()		# Obtenir una llista de hosts actius
    enviarMensaje('IPs obertes: {}'.format(up_hosts))
    print(up_hosts)   
def nmap_ports():
    ip=input("    [+] IP Objectiu ==> ")
    nm = nmap.PortScanner()
    ports_oberts="-p "
    results = nm.scan(hosts=ip,arguments="-sT -n -Pn -T4")
    count=0
    #print (results)
    
    print("\n    Host : %s" % ip)
    print("    Estat : %s" % nm[ip].state())

    for proto in nm[ip].all_protocols():
        print("    Protocol : %s" % proto)
        print()
        lport = nm[ip][proto].keys()
        sorted(lport)
        enviarMensaje("\nHost : %(ip)s Estat: %(estat)s Protocol: %(protocol)s" %{"ip": ip, "estat": nm[ip].state(), "protocol": proto })
        for port in lport:
            print ("    Port: %s\t Estat: %s" % (port, nm[ip][proto][port]["state"]))
            if count==0:
                ports_oberts=ports_oberts+str(port)
                count=1
            else:
                ports_oberts=ports_oberts+","+str(port)
def nmap_versio_servei():
    ip=input("    [+] IP Objectiu ==> ")
    nmScan = nmap.PortScanner()
    resultprova = nmScan.scan(ip, '1-5000').keys()
    print(nmScan.csv())
    enviarMensaje(nmScan.csv())
def vulnerabilitats():
    
    ##Descarrega de scripts de vulnerabilitats(www.vulners.com)
    subprocess.call("cd /usr/share/nmap/scripts/ && sudo git clone https://github.com/vulnersCom/nmap-vulners.git && sudo git clone https://github.com/scipag/vulscan.git", shell=True)
    subprocess.call("cd /usr/share/nmap/scripts/vulscan/utilities/updater/ && sudo chmod +x updateFiles.sh &&  sudo ./updateFiles.sh", shell=True)



    ##Execució
    print("     ------------------------\n")
    ip=input("    [+] IP Objectiu ==> ")
    port=input("    [+] Port Objectiu ==> ")
    subprocess.call("nmap --script nmap-vulners -sV -oN vulnNmap.txt -p {} {}".format(port, ip), shell=True)
    enviarDocumento("./vulnNmap.txt")
def demanaNumeroEnter():
 
    correcte=False
    num=0
    while(not correcte):
        try:
            num = int(input("    Introdueix un número entre l'1 i el 5: "))
            correcte=True
        except ValueError:
            print("    Error, introdueix un número entre l'1 i el 5")
     
    return num
 
sortir = False
opcio = 0
 
while not sortir:
    print("")
    print ("    ------------NMAP-------------")
    print ("    Opció 1. Escaneig IP's de la xarxa")
    print ("    Opció 2. Ports a traves de una ip disponible")
    print ("    Opció 3. Versions serveis")
    print ("    Opció 4. Vulnerabilitats CVE")
    print ("    Opció 5. Tornar al menú principal")
 
    print ("    Tria una opció: ")
    print("")
    opcio = demanaNumeroEnter()
 
    if opcio == 1:
        host_actiu()
    elif opcio == 2:
            nmap_ports()
    elif opcio == 3:
        nmap_versio_servei()
    elif opcio == 4:
        vulnerabilitats()
    elif opcio == 5:
        sortir = True
        print("    Menú principal:")
        exec(open("main.py").read())
    else:
        print ("    Introdueix un número entre l'1 i el 5")

