//python server.py

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 5000))
s.listen(1)

c, a = s.accept()
print(c.recv(1024).decode())
c.send(b"Hello Client")

c.close()
s.close()