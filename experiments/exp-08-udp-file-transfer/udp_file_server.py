"""Exp 8 - UDP file transfer: receiver (server).

Run this FIRST, then run udp_file_client.py.
Listens on UDP port 5000 and writes the received file as
received_sample.txt in this folder.
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("0.0.0.0", 5000))
print("UDP receiver waiting on port 5000...")

with open("received_sample.txt", "wb") as f:
    while True:
        data, addr = s.recvfrom(65535)
        if data == b"EOF":
            break
        f.write(data)

print("File received and saved as received_sample.txt")
s.close()
