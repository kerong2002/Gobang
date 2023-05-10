import socket

# Create a UDP server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the IP address and port number
server_socket.bind(('localhost', 12345))

print('Server started, waiting for messages...')

while True:
    # Receive data and client address from client socket
    data, client_address = server_socket.recvfrom(1024)

    # Decode the received data and print it
    message = data.decode('utf-8')
    print(f'Received message from {client_address}: {message}')

    # Send a response back to the client
    response = f'Thank you for your message: {message}'
    server_socket.sendto(response.encode('utf-8'), client_address)
