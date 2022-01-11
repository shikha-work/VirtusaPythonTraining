#!/usr/bin/python3           # This is server.py file
import socket

# create a socket object
srvr = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 9898

# bind to the port
srvr.bind((host, port))

# queue up to 5 requests
srvr.listen(5)

while True:
    # establish a connection
    clnt, addr = srvr.accept()

    print("Got a connection from %s" % str(addr))

    msg = 'Thank you for connecting' + "\r\n"
    clnt.send(msg.encode('ascii'))
    clnt.close()