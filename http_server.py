####    Simple Server 3: HTTP Server  #####
# Follows HTTP rules, returns contents of file if it exists
#
# Server:
# $> python3 http_server.py
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
        request = data.decode().split('\n')[0].split(' ')
        if len(request)<2 or len(request[1])<2:
            conn.sendall("Invalid request".encode())
            continue
        action = request[0]
        filename = request[1][1:]
        ### NEW CODE ###
        if len(filename)==0:
            filename="index.html"
        ################
        print(f"Action: {action}, File: {filename}")
        if os.path.isfile(filename):
            with open(filename,'r') as f:
                ### NEW CODE ###
                conn.sendall('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'.encode())
                ################
                conn.sendall(f.read().encode())
        else:
             ### NEW CODE ###
            conn.sendall('HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n'.encode())
            #################
