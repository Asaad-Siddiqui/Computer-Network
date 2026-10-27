# Experiment 9 — Capture packets using Wireshark

## Aim
Capture TCP traffic while logging in to Facebook / Instagram / YouTube,
then use display filters to (a) capture the traffic, (b) count the TCP
packets with SYN, PSH and RST flags set and show each as a fraction of
all TCP packets, and (c) count how many TCP packets went to/from each
site and how many of those were also HTTP packets. Save the capture
output in a file.

## What is in this folder
- `Exp9.mp4` — video demonstration for this experiment (3 min 57 sec,
  1920x1080). It shows downloading Wireshark and then a live capture
  being filtered in Wireshark (for example a `tls or quic or http`
  display filter over a real capture). Watch it first if you have never
  used Wireshark.
- `wireshark_filters.txt` — every exact capture filter and display
  filter for parts (a), (b) and (c), plus how to count and how to work
  out the fractions. Copy and paste from there.

## Software needed
- Wireshark (free, from wireshark.org) on your own Windows/macOS/Linux PC.
  On Windows it also installs Npcap so it can capture — accept that part
  of the installer. You must run the capture on your own traffic, on
  your own network interface (usually Wi-Fi or Ethernet).

## How to do it, step by step
### 9a — Capture (capture filter, set BEFORE you start)
1. Open Wireshark > Capture Options, pick your active interface
   (the one with moving traffic), and set the Capture Filter to:
   `tcp` — or, to narrow it to web traffic, `tcp port 443`.
   Note: a capture filter cannot use a website name. If you want only
   one site's IPs, first run `nslookup facebook.com` (and the same for
   Instagram/YouTube) and use `tcp and (host <IP1> or host <IP2>)`.
2. Start the capture, THEN log in to your Facebook / Instagram /
   YouTube account in the browser, browse briefly, and stop the capture.
3. Save it: File > Save As > `exp9-capture.pcapng`. This saved file is
   the "output saved in file" the experiment asks for.

### 9b — Display filters: count SYN, PSH, RST and their fractions
A display filter is typed in the bar at the top AFTER capturing — it
does not change the saved file, it only changes what is shown.
1. Filter `tcp` and note the total TCP packet count (status bar).
2. Filter `tcp.flags.syn == 1`, note the count. Fraction = SYN count /
   total TCP count. Repeat with `tcp.flags.psh == 1` and
   `tcp.flags.rst == 1`.
3. The status bar also shows the fraction directly as
   "Displayed: X packets (Y%)" for each filter.
   Example: 120 SYN packets out of 1500 TCP packets = 120/1500 = 0.08 = 8%.
   Your numbers will differ — report your own counts and fractions.

### 9c — Per-site counts and HTTP counts
1. For one site, filter by its TLS server name, for example
   `tls.handshake.extensions_server_name contains "facebook"`
   (use "instagram" / "youtube" the same way), or by its IP:
   `ip.addr == <IP>`. Note the packet count.
2. For the HTTP part of that site's traffic, filter
   `ip.addr == <IP> && http` and note the count.
3. Repeat for each site and tabulate: site | TCP packets | HTTP packets.

## Important note for the report
Facebook / Instagram / YouTube use HTTPS (TLS on port 443), NOT plain
HTTP. So the HTTP count for those sites will be about 0. That is a
correct result, not a failed capture — write it down and explain why.
If a non-zero HTTP count is needed, capture a plain-HTTP site separately
and label it separately.

## Privacy note
Capture only your own login traffic on your own machine. Do not capture
on a shared/public network, and do not share the `.pcapng` file publicly
— it can contain session data. The video in this folder is the
demonstration; your own capture file is for your practical file only.
