import socket

domain = input("Introdueix un domini per obtindre la ip pública: ")

ip2 = socket.getaddrinfo(domain, 80)


print("La teva IP pública és: {}".format(ip2[0][4]))
 


#print ("La teva IP pública és: {}".format(ip2[0][4]))