import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(('localhost', 12345))
s.listen(1)

print("Server is waiting for connection...")
conn, addr = s.accept()
print("Client connected!")

msg = conn.recv(1024).decode()
print("Client:", msg)

conn.send("Hello Client!".encode())

conn.close()
s.close()
