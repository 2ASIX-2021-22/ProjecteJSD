# #!/bin/bash/python3
from ensurepip import version
from itertools import product
from operator import length_hint
from typing import Protocol
import nmap 
import subprocess

def host_actiu():
    nm = nmap.PortScanner()
    ip_xarxa = input("Introdueix IP de la xarxa: ")
    nm.scan(hosts = ip_xarxa, arguments='-n -sP -PE')
    up_hosts = nm.all_hosts()		# Obtenir una llista de hosts actius
    print(up_hosts)

# def host_list():
#     nm = nmap.PortScanner()
#     ip_xarxa = input("Introdueix IP de la xarxa: ")
#     nm.scan(hosts=ip_xarxa, arguments='-n -sP -PE -PA21,23,80,3389')
#     hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
#     for host, status in hosts_list:
#         print('{0}:{1}'.host)

    # nm.scan(hosts='192.168.1.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
    # hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
    # for host, status in hosts_list:
    #     print('{0}:{1}'.format(host, status))

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


# def nmap_versio_servei():
#     ip=input("[+] IP Objectiu ==> ")
#     nm = nmap.PortScanner()
#     results = nm.scan(hosts=ip,arguments="-sV")
#     results1 = nm[ip].all_tcp()
#     #prova = nm[ip]['tcp'][results1[0:]]
#     # print(results1["name"])
#     # print(results1["product"])
#     # print(results1["version"])
#     # print(results1["extrainfo"])
#     print(results1)

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


# def port_host():
#     nm = nmap.PortScanner()
#     host=input("[+] IP Objectiu ==> ")
#     for host in nm.all_hosts():
#      print('----------------------------------------------------')
#      print('Host : %s (%s)' % (host, nm[host].hostname()))
#      print('State : %s' % nm[host].state())
    
#     for proto in nm[host].all_protocols():
#         print('----------')
#         print('Protocol : %s' % proto)
#         lport = nm[host][proto].keys()
#         lport.sort()

#     for port in lport:
#         print ('port : %s\tstate : %s' % (port, nm[host][proto][port]['state']))



     
#port_host()
#host_list()
host_actiu()
nmap_ports()
nmap_versio_servei()
vulnerabilitats()



