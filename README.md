# Computer Networks — Practical Experiments

All the experiments from the course list that were **not cut**. Each
experiment is in its own folder, with its own files and its own short
guide. This README is the map — for the full steps, open the README
inside the experiment's folder.

## Which experiments are here, and which are not

| Exp | Topic | Folder | Type |
|-----|-------|--------|------|
| 2 | Implement and analyze TCP/IP utility commands | `experiments/exp-02-tcp-ip-utilities/` | Windows `.bat` |
| 4 | Configure hubs and switches in a topology (Packet Tracer) | `experiments/exp-04-hub-switch-packet-tracer/` | `.pkt` |
| 7 | TCP socket program — (a) Write Hello to Each Other | `experiments/exp-07-tcp-socket/` | Python |
| 8 | UDP sockets — file transfer between two machines | `experiments/exp-08-udp-file-transfer/` | Python |
| 9 | Capture packets using Wireshark | `experiments/exp-09-wireshark/` | Wireshark + video |
| 10 | Implement and analyze DHCP server and client | `experiments/exp-10-dhcp-packet-tracer/` | `.pkt` |

**Cut from the list (not in this repo):** Exp 1 (Comparative Analysis of
Network Simulators), Exp 3 (TCP and UDP Data Traffic Generation using
NS2), Exp 5 (Static routing using GNS3), Exp 6 (Dynamic routing using
GNS3). Those four were struck through on the list, so they are
deliberately left out — nothing is missing by accident.

## What you need installed (one time)

| Tool | Needed for | Where to get it |
|------|-----------|-----------------|
| Python 3 (any recent version) | Exp 7, Exp 8 | python.org — no extra packages needed |
| Cisco Packet Tracer | Exp 4, Exp 10 | Free with a Cisco Networking Academy (NetAcad) account, from NetAcad. Sign in once, then open `.pkt` files. |
| Wireshark | Exp 9 | wireshark.org (Windows installer also installs Npcap) |
| Windows PC | Exp 2 | The `.bat` file is Windows-only. On Linux/macOS use the equivalent commands listed in Exp 2's README. |

No paid software is needed for any experiment in this repo.

## How to run each experiment (short version)

Full steps, expected output and troubleshooting are in each folder's
README. This is just the quick idea:

### Exp 2 — TCP/IP utilities (Windows)
Double-click `tcp-ip-utilities.bat` in
`experiments/exp-02-tcp-ip-utilities/`. It runs `ipconfig`, `ping`,
`tracert`, `nslookup`, `netstat -an`, `arp -a`, `hostname` and
`pathping` in order. Note: `pathping` takes a few minutes — that is normal.

### Exp 4 — Hub vs. switch (Packet Tracer)
Open `Exp4_Hub_Switch.pkt` in Packet Tracer. In Realtime mode, ping one
PC from another (`ping <other PC's IP>`) to prove connectivity. Then in
Simulation mode, send a Simple PDU and watch: the hub copies the frame
to every PC, the switch sends it only to the destination after learning
MAC addresses (`show mac-address-table` on the switch CLI).

### Exp 7 — TCP Hello (Python, two terminals, server first)
```
python server.py     # terminal 1, in experiments/exp-07-tcp-socket/
python client.py     # terminal 2
```
Expected: server prints `Client: Hello Server!`, client prints
`Server: Hello Client!`. For two machines, replace `localhost` in both
files with the server machine's LAN IP.

### Exp 8 — UDP file transfer (Python, receiver first)
```
python udp_file_server.py   # terminal 1, in experiments/exp-08-udp-file-transfer/
python udp_file_client.py   # terminal 2
```
Expected: `File sent.` on the sender, and a new `received_sample.txt`
on the receiver matching `sample.txt`. For two machines, set `SERVER_IP`
in the client to the receiver's LAN IP. **Do not submit the
`supplied_*.py` files for this experiment — see the note below.**

### Exp 9 — Wireshark (your own PC, your own traffic)
1. Watch `Exp9.mp4` in `experiments/exp-09-wireshark/` first (3 min 57 sec).
2. Set the capture filter to `tcp` (or `tcp port 443`), start capturing,
   log in to Facebook / Instagram / YouTube, stop, and save as
   `exp9-capture.pcapng`.
3. Use the display filters in `wireshark_filters.txt`: `tcp.flags.syn == 1`,
   `tcp.flags.psh == 1`, `tcp.flags.rst == 1` — each count divided by the
   total TCP count is its fraction. For per-site counts use
   `tls.handshake.extensions_server_name contains "facebook"` (and the
   same for Instagram/YouTube) and `ip.addr == <IP> && http` for HTTP.
   Note: those sites use HTTPS, so their plain-HTTP count will be about
   0 — that is a correct result, explained in Exp 9's README.

### Exp 10 — DHCP (Packet Tracer)
Open `Exp10_DHCP.pkt` in Packet Tracer. Set each PC to DHCP (Desktop >
IP Configuration > DHCP), then on a PC run `ipconfig /all` to see its
leased address, gateway and DHCP server. On the server side check the
lease table (`show ip dhcp binding` on a router, or Services > DHCP on
a Server device). Ping one client from another to prove it works.

## How to see the output in a `.pkt` file (Exp 4 and Exp 10)
A `.pkt` file is not code and has no output of its own — you open it
and run the network inside Packet Tracer:
- **Realtime mode** (bottom-right tab): the network runs live. Click a
  device, use Desktop > Command Prompt (`ping`, `ipconfig`) or Desktop >
  IP Configuration, and read the results there.
- **Simulation mode** (bottom-right tab): the network runs step by step.
  Add a Simple PDU between two devices, press Play, and watch each
  packet/frame move device by device. Click any packet in the event list
  to open its details (OSI layers, headers, in/out).
- **Device CLI**: click a router or switch > CLI, type `enable`, then
  commands like `show ip dhcp binding`, `show mac-address-table` or
  `show ip interface brief` to see what the device itself knows.
- **Purpose in one line:** Exp 4 proves hub vs. switch forwarding;
  Exp 10 proves automatic addressing (DHCP). Your report should quote
  the ping results, the CLI tables and what Simulation mode showed —
  those are the experiment's outputs.

## File map
```
experiments/
  exp-02-tcp-ip-utilities/
    tcp-ip-utilities.bat, README.md
  exp-04-hub-switch-packet-tracer/
    Exp4_Hub_Switch.pkt, README.md
  exp-07-tcp-socket/
    server.py, client.py, README.md
  exp-08-udp-file-transfer/
    udp_file_server.py, udp_file_client.py, sample.txt,
    supplied_server.py, supplied_client.py, README.md
  exp-09-wireshark/
    Exp9.mp4, wireshark_filters.txt, README.md
  exp-10-dhcp-packet-tracer/
    Exp10_DHCP.pkt, router_dhcp_config.txt, README.md
```

## Two problems found in the files as supplied (fixed, not hidden)
1. **Exp 7 (and the supplied Exp 8 files):** the original `.py` files
   started with a `//python ...` line, which is not a Python comment —
   Python fails on line 1 with `SyntaxError`. That line was removed
   from Exp 7's files; the rest of the code is unchanged and now runs.
2. **Exp 8:** the originally supplied files were not a UDP file transfer
   at all — they used TCP (`SOCK_STREAM`), only exchanged "Hello", and
   their ports did not match (client 12345, server 5000), so they could
   not connect. They are kept untouched as `supplied_server.py` /
   `supplied_client.py` for reference, and a real UDP file transfer
   (`udp_file_server.py` / `udp_file_client.py`) is provided alongside.
   Submit the UDP files, not the supplied ones.

## Notes
- Your results (IPs, hop counts, packet counts, leased addresses) will
  differ from anyone else's because they depend on your own network and
  your own capture. Report your own numbers.
- Wireshark captures: capture only your own traffic on your own machine.
  Do not share a `.pcapng` file publicly — it can contain session data.

---
Asaad Siddiqui -- AI Agent
