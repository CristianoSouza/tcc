#!/usr/bin/python

import socket

UDP_IP = "192.168.25.2"
UDP_PORT = 8000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) 
sock.bind((UDP_IP, UDP_PORT))
print ("sock:",sock)
while True:
    print ("Whille")
    
    '''server_address = ('192.168.25.177', 8888)
    message = 'This is the message'
    print ('sending :', message)
    a = sock.sendto(message.encode(), server_address)
    print ("result: ", a)
'''

    data = sock.recvfrom(100) # buffer size is 1024 bytes
    print ("Address: ", addr)
    #print ("received message:", data)
