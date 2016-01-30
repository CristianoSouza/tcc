import socket

# Create a TCP/IP socke
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.25.177', 8888)
while 1:
    print ("connecting to " ,server_address)

    message = 'This is the message'
    print ('sending :', message)
    a = sock.sendto(message.encode(), server_address)
    print ("result: ", a)

sock.close()

