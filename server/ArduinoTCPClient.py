import socket

# Create a TCP/IP socke
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('192.168.25.178', 23)

print ("connecting to " ,server_address)
sock.connect(server_address)
print ("Conexctou1")

message = "abba"
print ('sending :', message)
a = sock.send(message.encode())
print ("result: ", a)

data = sock.recv(1024)
data.decode()
print ("DADO: ", data.decode())

sock.close()
