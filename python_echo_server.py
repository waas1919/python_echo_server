#!/usr/bin/env python3
import socket

def start_echo_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Bind the socket to a specific address and port
    server_address = ('localhost', 9091)
    server_socket.bind(server_address)
    
    # Listen for incoming connections
    server_socket.listen(1)
    print('Echo server started on {}:{}'.format(*server_address))
    
    while True:
        # Wait for a client to connect
        print('Waiting for a connection...')
        client_socket, client_address = server_socket.accept()
        print('Connected to', client_address)
        
        # Receive and send back the data
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            
            # Send back the received data
            client_socket.sendall(data)
        
        # Close the connection
        client_socket.close()
        print('Connection closed')

# Start the echo server
start_echo_server()

