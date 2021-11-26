import sys
import socket

objectiu = socket.gethostbyname(input("Introdueïx la direcció IP: "))

print("Escanejant objectiu: " + objectiu)

try:
    for port in range (1, 150):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultat = s.connect_ex((objectiu, port))
        if resultat == 0:
            print("El port {} està obert".format(port))
        s.close()
except:
    print("\n Sortint...")
    sys.exit