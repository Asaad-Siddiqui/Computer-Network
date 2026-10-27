# Experiment 10 — Implement and analyze DHCP server and client

## Aim
A DHCP server hands out IP addresses automatically, so client PCs get
their IP, subnet mask, gateway and DNS without manual configuration.

## What is in this folder
- `Exp10_DHCP.pkt` — the ready-made Packet Tracer topology.
  Open it in Cisco Packet Tracer.
- `router_dhcp_config.txt` — reference router-as-DHCP-server commands
  (pool, excluded addresses, gateway, DNS). Use it if your topology's
  router is the DHCP server, or to check what the file's server is doing.

## Software needed
- Cisco Packet Tracer (free with a Cisco Networking Academy / NetAcad
  account). No code or extra install is needed for this experiment.

## How to open and see the output
1. Open Cisco Packet Tracer, then File > Open > `Exp10_DHCP.pkt`.
2. On each client PC, check that it is set to DHCP, not a static IP:
   click the PC > Desktop > IP Configuration > select DHCP.
   The PC should receive an address automatically (for example in the
   192.168.1.11 onwards range if the pool starts after the excluded
   addresses — your file's exact range depends on its own setup, so
   read what the PC actually shows).
3. Confirm on the PC: Desktop > Command Prompt, then run
   `ipconfig /all` and look for the leased IP address, subnet mask,
   default gateway and the DHCP server's address. To force a fresh lease:
   `ipconfig /release` then `ipconfig /renew`.
4. Confirm on the server side:
   - If the router is the DHCP server: click the router > CLI, then
     `enable`, `show ip dhcp binding` (which PC got which address) and
     `show ip dhcp pool` (pool size and how many addresses are leased).
   - If a Server device is the DHCP server: click it > Services > DHCP
     and check the pool and the leases shown there.
5. Prove it works end to end: from one DHCP client, `ping` another
   client's leased IP. A reply proves the auto-configured clients can
   reach each other.

## What to write in the report
- The four DHCP steps in order: Discover, Offer, Request, Acknowledge
  (DORA) — in Simulation mode you can watch these packets if you filter
  for DHCP/BOOTP.
- Each client's leased IP, gateway and DNS from `ipconfig /all`.
- The server's binding/lease table (who got what).
- One-line conclusion: DHCP removes manual IP setup and prevents two
  PCs accidentally getting the same address.

## Common problems
- PC shows 169.254.x.x: it got no DHCP reply. Check the PC is on DHCP,
  the cable/link to the server is connected, and the DHCP service/pool
  is enabled on the server.
- PC gets an address but ping fails: check the gateway and that both
  PCs are in the same pool/network.
