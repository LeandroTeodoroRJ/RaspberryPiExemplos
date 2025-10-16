#!/usr/bin/env python3

import socket

HOST = '127.0.0.1'  # The server's hostname or IP address (or 0.0.0.0)
PORT = 1300         # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
	try:
		s.connect((HOST, PORT))
		s.sendall(b'Hello from Python client!')
		data = s.recv(1024)
	except ConnectionRefusedError:
		print("Connection ERROR")
		exit(1)

if not data:
	print("Nothing to receiver")
else:
	print('Received', repr(data))

