import socket

# Create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect(('localhost', 12345))

# Send a message to the server
message = 'Hello, server!'
client_socket.send(message.encode('utf-8'))

# Receive a response from the server
response = client_socket.recv(1024)

# Decode the received data and print it
message = response.decode('utf-8')
print(f'Received message from server: {message}')

# Close the client socket
client_socket.close()
