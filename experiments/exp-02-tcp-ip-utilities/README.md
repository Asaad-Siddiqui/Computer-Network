# Experiment 2 — Implement and analyze TCP/IP utility commands

## Aim
Run the standard TCP/IP utility commands on Windows and observe what each
one shows about your own machine and its route to the internet.

## What is in this folder
- `tcp-ip-utilities.bat` — one script that runs all 8 commands in order.

## Commands in the script (in order)
1. `ipconfig` — your IP address, subnet mask and default gateway.
2. `ping google.com` — is the host reachable, and how long replies take.
3. `tracert google.com` — every hop (router) on the way to the host.
4. `nslookup google.com` — the IP address(es) behind the domain name.
5. `netstat -an` — all active connections and listening ports.
6. `arp -a` — the ARP table: IP addresses mapped to MAC addresses on your LAN.
7. `hostname` — your computer's name.
8. `pathping google.com` — route plus packet loss per hop (this one is slow,
   it can take a few minutes — that is normal, do not close it early).

## How to run
1. You need a Windows PC with an internet connection.
2. Double-click `tcp-ip-utilities.bat`, or open Command Prompt in this
   folder and run `tcp-ip-utilities.bat`.
3. The window stays open at the end (the script does not close itself) so
   you can read or screenshot the output.

## How to show the output (for the practical file)
- Run the commands one at a time as well, and screenshot each output, or
  save the whole window's output with:
  `tcp-ip-utilities.bat > exp2-output.txt` in Command Prompt.
- In your report, write one line per command: what you ran, what it
  returned on your machine, and what that value means (for example, your
  own IP from `ipconfig`, the hop count from `tracert`).

## Notes
- This is a Windows batch file (`.bat`). It will not run on Linux/macOS as
  it is — the equivalents there are `ifconfig`/`ip addr`, `ping`,
  `traceroute`, `nslookup`/`dig`, `netstat`/`ss`, `arp`, `hostname`.
- `ping`/`tracert` results change with your network, so your numbers will
  differ from anyone else's — that is expected.
