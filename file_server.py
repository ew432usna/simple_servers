####    Simple Server 2: File Server  #####
# Returns contents of file if it exists
#
# Server:
# $> python3 file_server.py
# Client:
# $> nc localhost 5000
# GET /hello.html

import socket
import os
from random import randint

HOST = "0.0.0.0"  # Listen on all network interfaces (wildcard)
PORT = randint(5000,10000)  # Port to listen on
print(f"File Server listening on {PORT}")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen() # wait for somebody to connect
while True:
    conn, addr = s.accept()
    with conn:
        print(f"Connection from {addr}")
        data = conn.recv(1024) # accept up to 1024 characters
        print(f"DATA: {data.decode()}")
        ##### NEW CODE ######
        # 1. First line of the request should be GET <filename>
        request = data.decode().split('\n')[0].split(' ')
        if len(request)<2 or len(request[1])<2:
            conn.sendall("Invalid request".encode())
            continue
        # 2. Put each part in a variable
        action = request[0]
        filename = request[1][1:]
        print(f"Action: {action}, File: {filename}")
        # 3. If the file exists, send it
        if os.path.isfile(filename):
            with open(filename,'r') as f:
                conn.sendall(f.read().encode())
        else:
            #    ...otherwise send an error message
            conn.sendall("That file does not exist".encode())
