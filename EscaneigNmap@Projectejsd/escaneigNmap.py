 #!/bin/bash/python3

import nmap
import subprocess

def host_actiu():
    nm = nmap.PortScanner()
    ip_xarxa = input("Introdueix IP de la xarxa: ")
    nm.scan(hosts = ip_xarxa, arguments='-n -sP -PE')
    up_hosts = nm.all_hosts()		# Obtenir una llista de hosts actius
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
    subprocess.call("sudo su", shell=True)
    subprocess.call("cd /usr/share/nmap/scripts/", shell=True)
    subprocess.call("git clone https://github.com/vulnersCom/nmap-vulners.git", shell=True)
    subprocess.call("git clone https://github.com/scipag/vulscan.git", shell=True)
    subprocess.call("cd vulscan/utilities/updater/", shell=True)
    subprocess.call("chmod +x updateFiles.sh", shell=True)
    subprocess.call("./updateFiles.sh", shell=True)



    ##Execució
    ip=input("[+] IP Objectiu ==> ")
    port=input("[+] Port Objectiu ==> ")
    subprocess.call("nmap --script nmap-vulners -sV -p {} {}".format(port, ip), shell=True)


host_actiu()
nmap_ports()
nmap_versio_servei()
vulnerabilitats()