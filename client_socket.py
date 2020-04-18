import socket

# create a object
s = socket.socket()

# define the port on which server is running
port = 12345

# connect to the server
s.connect(('127.0.0.1', port))

# receive data from server
print(s.recv(1024))

# close the connection
s.close()
