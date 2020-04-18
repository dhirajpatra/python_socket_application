import socket

# create a socket object
s = socket.socket()
print("socket sucessfully created")

# reserv e a port
port = 12345

# bind the port
s.bind(('', port))
print("socket bind on port %s" % (port))

# put the socket in listning mode
s.listen(5)
print("socket is listning")

# a forever loop of listning until inturrupt
while True:

    # establish connection with client
    c, addr = s.accept()
    print("got connection from ", addr)

    # send a response back to client
    output = "thank you for connecting"
    c.sendall(output.encode('utf-8'))

    # close the connection
    c.close()
