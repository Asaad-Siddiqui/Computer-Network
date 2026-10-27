"""Exp 8 - UDP file transfer: sender (client).

Sends sample.txt to the receiver over UDP, then sends EOF.
Change SERVER_IP to the receiver machine's IP for two machines.
For the same machine, leave it as 127.0.0.1.
"""
import socket

SERVER_IP = "127.0.0.1"
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

with open("sample.txt", "rb") as f:
    data = f.read()
    s.sendto(data, (SERVER_IP, PORT))

s.sendto(b"EOF", (SERVER_IP, PORT))
print("File sent.")
s.close()
