# Experiment 8 — UDP sockets: file transfer between two machines

## Aim
Transfer a file from one machine to another using UDP sockets
(`SOCK_DGRAM`, connectionless) instead of TCP.

## What is in this folder
- `udp_file_server.py` — the receiver. Run this first.
- `udp_file_client.py` — the sender. Sends `sample.txt`, then `EOF`.
- `sample.txt` — the file that gets transferred.
- `supplied_server.py` / `supplied_client.py` — the files as originally
  supplied, kept unchanged for reference. See the important note below.

## Software needed
- Python 3 only. No extra packages.

## How to run (two terminals, receiver first)
Terminal 1 — receiver:
```
python udp_file_server.py
```
You should see: `UDP receiver waiting on port 5000...`

Terminal 2 — sender (same machine for a local test):
```
python udp_file_client.py
```
You should see: `File sent.`
Receiver terminal then shows: `File received and saved as received_sample.txt`

Check it worked: open `received_sample.txt` on the receiver — it must
match `sample.txt` word for word.

Testing note: the corrected files compile cleanly, but a live UDP run
could not be tested on the machine that arranged this repo — its
sandbox blocks UDP `sendto` even on loopback (`PermissionError`), while
TCP runs fine there. Run it on your own Windows/Linux PC, where UDP
works normally, and verify `received_sample.txt` matches `sample.txt`.

## How to run it on two machines
1. On the receiver, run `udp_file_server.py` (it listens on all interfaces).
2. On the sender, edit `SERVER_IP` in `udp_file_client.py` to the
   receiver machine's LAN IP address, then run it.
3. Allow Python through the firewall if Windows asks.
4. UDP has no delivery guarantee: on a busy or lossy network a datagram
   can be lost, unlike TCP in Experiment 7. For this small sample file
   on a LAN it transfers in one datagram; large files would need to be
   split into chunks with sequence numbers — that is beyond this experiment.

## IMPORTANT NOTE — please read before submitting
The originally supplied `supplied_server.py` / `supplied_client.py` do
NOT do what this experiment asks for:
- They use `SOCK_STREAM` (TCP), not `SOCK_DGRAM` (UDP).
- They only exchange "Hello" messages — they never read or write a file.
- Their ports do not match (client connects to 12345, server listens
  on 5000), so they cannot even connect to each other.
They are kept here untouched so nothing is hidden, but do NOT submit
them as the UDP file-transfer program. Submit `udp_file_server.py` and
`udp_file_client.py` instead — those are the actual UDP file transfer.
