import socket

host = '0.0.0.0'
port = 9999
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.connect((host, port))
serv.listen(1)
print(f"Server listening on {host} : {port}") 
cli_socket, cli_address = serv.accept()
print(f"connection from {cli_address}")
while True:
    command = input("Enter command: ")
    if command.lower() == 'exit' :
        break
    cli_socket.send(command.encode())
    response = cli_socket.recv(1024).decode()
    print(f"Client response: {response}")
    cli_socket.close()
serv.close()
