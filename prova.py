import subprocess

f = open("output.txt", "w") # this creates the file
ip_host = input("Introdueix IP d'un dispositiu: ")
#cmd=['python3 /home/alumne/Code/ProjecteJSD/ssh-audit/ssh-audit.py {}'.format(ip_host)]
subprocess.run("python3 /home/alumne/Code/ProjecteJSD/ssh-audit/ssh-audit.py {}".format(ip_host), stdout=f) # this sends it to f

with open("output.txt", "r") as f:
     print(f.read())



# ip_host = input("Introdueix IP d'un dispositiu: ")
# subprocess.call("python3 ./ssh-audit/ssh-audit.py {}".format(ip_host), shell=True)