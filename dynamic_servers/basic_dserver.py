####    Simple Server 3: HTTP Server  #####
# Follows HTTP rules, returns dynamic content
# or the contents of a file if it exists
#
# Server:
# $> python3 basic_dserver.py
# Client:
# $> nc localhost 5003
# GET /hello.html

import socket
import os

HOST = "0.0.0.0"  # Listen on all network interfaces (wildcard)
PORT = 5003  # Port to listen on
print(f"HTTP Server listening on {PORT}")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen() # wait for somebody to connect
while True:
    conn, addr = s.accept()
    with conn:
        print(f"Connection from {addr}")
        data = conn.recv(1024) # accept up to 1024 characters
        print(f"DATA: {data.decode()}")
        lines = data.decode().split('\n')
        request = lines[0].split(' ')
        if len(request)<2 or len(request[1])==0:
            conn.sendall("Invalid request".encode())
            continue
        action = request[0]
        route = request[1][1:]
        if len(route)==0:
            route="index.html"
        print(f"Action: {action}, Route: {route}")
        #### Handle dynamic responses             ####
        if route=='tasks':
            response = "My tasks: 1. Learn HTML, 2. Learn CSS, 3. Make $$$$"
        ###############################################
        elif os.path.isfile(route):
            with open(route,'r') as f:
                respone = f.read()
        else:
            conn.sendall('HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n'.encode())
            continue
        
        #### Send the response ###
        conn.sendall('HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n'.encode())
        conn.sendall(response.encode())
        