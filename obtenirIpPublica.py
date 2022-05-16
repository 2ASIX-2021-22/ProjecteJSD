import socket

from bot_telegram import enviarMensaje

domain = input("    Introdueix un domini per obtindre la IP pública: ")

ip2 = socket.getaddrinfo(domain, 80)


print("    La teva IP pública és: {}".format(ip2[0][4]))
enviarMensaje("La teva IP pública és: {}".format(ip2[0][4]))
