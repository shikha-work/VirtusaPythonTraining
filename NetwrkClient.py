import socket

# create a socket object
clnt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9898

# connection to hostname on the port.
clnt.connect((host, port))

# Receive no more than 1024 bytes
msg = clnt.recv(1024)

clnt.close()
print (msg.decode('ascii'))