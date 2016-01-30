#!/usr/bin/env python
 
import socket
import sys
 
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('192.168.1.100', 5015)
sock.bind(server_address)
# Listen for incoming connections
sock.listen(5)
 
try: 
    while True:
        # Wait for a connection
        print('waiting for a connection...')
        connection, client_address = sock.accept()
        print('connection from: ',client_address)
        try:
            while True:
                data = connection.recv(1024)

                print ("DADO rECEBIDO:> ", data.decode())

                msg = "A"
                connection.sendall(msg.encode())
                break

        finally:
            # Clean up the connection
            connection.close()
except KeyboardInterrupt:
    print('exiting.')
finally:
    sock.shutdown(socket.SHUT_RDWR)
    sock.close()
