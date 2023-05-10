import socket

# Create a UDP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Send a message to the server
message = 'Hello, server!'
client_socket.sendto(message.encode('utf-8'), ('localhost', 12345))

# Receive a response from the server
response, server_address = client_socket.recvfrom(1024)

# Decode the received data and print it
message = response.decode('utf-8')
print(f'Received message from server {server_address}: {message}')

# Close the client socket
client_socket.close()
