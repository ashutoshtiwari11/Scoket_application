import socket

HOST = 'localhost'  # The hostname or IP address of the server
PORT = 8080  # The port to listen on

def handle_request(client_socket, client_address):
    request = client_socket.recv(1024).decode()
    print('Received request from:', client_address)
    print('Request:', request)
    
    method, Path, *_  = request.split(" ")

    # Create the HTTP response
    if method == 'GET':
       response = 'HTTP/1.1 200 OK\nContent-Type: text/html\n\nHello, World!'
   
       client_socket.sendall(response.encode())
       client_socket.close()
    elif method == 'POST':
       print("response post received")
       

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific host and port
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen()

print('Server listening on', HOST, 'port', PORT)

while True:
    # Accept a client connection
    client_socket, client_address = server_socket.accept()

    # Handle the client request in a separate function
    handle_request(client_socket, client_address)
