import socket

# Create a TCP server socketS
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the IP address and port numberSS
server_socket.bind(('localhost', 12345))

# Set the server to listen for incoming connections
server_socket.listen()

print('Server started, waiting for connections...')

while True:
    # Wait for a client to connect
    client_socket, client_address = server_socket.accept()

    print(f'Client connected from {client_address}')

    while True:
        # Receive data from the client
        data = client_socket.recv(1024)

        if not data:
            # If there is no data, the client has disconnected
            print(f'Client {client_address} disconnected')
            break

        # Decode the received data and print it
        message = data.decode('utf-8')
        print(f'Received message from {client_address}: {message}')

        # Send a response back to the client
        response = f'Thank you for your message: {message}'
        client_socket.send(response.encode('utf-8'))

