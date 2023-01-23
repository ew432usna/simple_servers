####    Simple Server 1: Echo  #####
# Returns text unchanged to client 
#
# Server:
# $> python3 echo_server.py
# Client:
# $> nc localhost 5000

import socket
from random import randint

HOST = "0.0.0.0"  # Listen on all network interfaces (wildcard)
PORT = randint(5000,10000)  # Port to listen on
print(f"Echo Server listening on {PORT}")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen() # wait for somebody to connect
while True:
    conn, addr = s.accept()
    with conn:
        print(f"Connection from {addr}")
        data = conn.recv(1024) # accept up to 1024 characters
        print(f"DATA: {data}")
        conn.sendall(data)     # send it right back, echo
