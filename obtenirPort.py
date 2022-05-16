import sys
import socket

from bot_telegram import enviarMensaje

objectiu = socket.gethostbyname(input("    Introdueix la direcció IP: "))

print("    Escanejant objectiu: " + objectiu)

try:
    for port in range (1, 65000):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        resultat = s.connect_ex((objectiu, port))
        if resultat == 0:
            print("    El port {} està obert".format(port))
            enviarMensaje("El port {} està obert".format(port))
        s.close()
except:
    print("\n    Sortint...")
    sys.exit