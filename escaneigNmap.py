 #!/bin/bash/python3
import nmap
import subprocess
from bot_telegram import enviarMensaje, enviarDocumento


def host_actiu():
    nm = nmap.PortScanner()
    ip_xarxa = input("Introdueix IP de la xarxa: ")
    nm.scan(hosts = ip_xarxa, arguments='-n -sP -PE')
    up_hosts = nm.all_hosts()		# Obtenir una llista de hosts actius
    enviarMensaje('IPs obertes: {}'.format(up_hosts))
    print(up_hosts)   
def nmap_ports():
    ip=input("[+] IP Objectiu ==> ")
    nm = nmap.PortScanner()
    ports_oberts="-p "
    results = nm.scan(hosts=ip,arguments="-sT -n -Pn -T4")
    count=0
    #print (results)
    
    print("\nHost : %s" % ip)
    print("Estat : %s" % nm[ip].state())

    for proto in nm[ip].all_protocols():
        print("Protocol : %s" % proto)
        print()
        lport = nm[ip][proto].keys()
        sorted(lport)
        enviarMensaje("\nHost : %(ip)s Estat: %(estat)s Protocol: %(protocol)s" %{"ip": ip, "estat": nm[ip].state(), "protocol": proto })
        for port in lport:
            print ("Port: %s\t Estat: %s" % (port, nm[ip][proto][port]["state"]))
            if count==0:
                ports_oberts=ports_oberts+str(port)
                count=1
            else:
                ports_oberts=ports_oberts+","+str(port)
def nmap_versio_servei():
    ip=input("[+] IP Objectiu ==> ")
    nmScan = nmap.PortScanner()
    resultprova = nmScan.scan(ip, '1-5000').keys()
    print(nmScan.csv())
def vulnerabilitats():
    
    ##Descarrega de scripts de vulnerabilitats(www.vulners.com)
    subprocess.call("cd /usr/share/nmap/scripts/ && sudo git clone https://github.com/vulnersCom/nmap-vulners.git && sudo git clone https://github.com/scipag/vulscan.git", shell=True)
    subprocess.call("cd /usr/share/nmap/scripts/vulscan/utilities/updater/ && sudo chmod +x updateFiles.sh &&  sudo ./updateFiles.sh", shell=True)



    ##Execució
    print("------------------------\n")
    ip=input("[+] IP Objectiu ==> ")
    port=input("[+] Port Objectiu ==> ")
    subprocess.call("nmap --script nmap-vulners -sV -p {} {}".format(port, ip), shell=True)
def demanaNumeroEnter():
 
    correcte=False
    num=0
    while(not correcte):
        try:
            num = int(input("Introdueix un numero enter: "))
            correcte=True
        except ValueError:
            print('Error, introdueix un numero enter')
     
    return num
 
sortir = False
opcio = 0
 
while not sortir:
    print("")
    print ("------------NMAP-------------")
    print ("1. Escaneig IP's de la xarxa")
    print ("2. Ports a traves de una ip disponible")
    print ("3. Versions serveis")
    print ("4. Vulnerabilitats CVE")
    print ("5. Sortir")
 
    print ("Tria una opció: ")
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
    else:
        print ("Introdueix un número entre 1 i 5")

print ("Fi")


