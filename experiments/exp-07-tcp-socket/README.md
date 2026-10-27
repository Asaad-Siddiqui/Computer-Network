# Experiment 7 — TCP socket program for a wired network (option a: Write Hello to Each Other)

## Aim
A TCP client and server exchange "Hello" messages over a socket, proving
a reliable, connection-based transfer. This is option (a) from the list:
*Write Hello to Each other*. Options (b) Chat and (c) Calculator/Factorial
are not in this folder.

## What is in this folder
- `server.py` — waits for a connection, receives the client's Hello,
  replies with its own Hello.
- `client.py` — connects to the server, sends its Hello, prints the reply.

Both use TCP (`SOCK_STREAM`), host `localhost`, port `12345`.

## Software needed
- Python 3 only. No extra packages. Works on Windows, Linux and macOS.

## How to run (two terminals, server first)
Terminal 1 — server:
```
python server.py
```
You should see: `Server is waiting for connection...`

Terminal 2 — client (a second terminal window, same machine):
```
python client.py
```

## Expected output
Server terminal:
```
Server is waiting for connection...
Client connected!
Client: Hello Server!
```
Client terminal:
```
Server: Hello Client!
```

## How to run it on two machines (wired network)
1. On the server machine, change `'localhost'` in both files to the
   server machine's LAN IP address (find it with `ipconfig` on Windows
   or `ip addr` on Linux).
2. Run the server on that machine, then the client on the other machine.
3. Allow Python through the firewall if Windows asks.

## Note on the files as supplied
The original files started with a `//python server.py` / `//python client.py`
line, which is not a Python comment and makes Python fail with
`SyntaxError: invalid syntax` on line 1. That line has been removed here;
the rest of the code is unchanged. The files in this folder compile and
run as shown above.
