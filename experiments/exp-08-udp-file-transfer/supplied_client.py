//python client.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(('localhost', 12345))

s.send("Hello Server!".encode())

msg = s.recv(1024).decode()
print("Server:", msg)

s.close()
