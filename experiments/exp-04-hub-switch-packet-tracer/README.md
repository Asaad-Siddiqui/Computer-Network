# Experiment 4 — Configure network devices (hubs and switches) in a topology using Packet Tracer

## Aim
Show the difference between a hub and a switch: a hub repeats every frame
out of every port, a switch learns MAC addresses and forwards a frame only
to the right port.

## What is in this folder
- `Exp4_Hub_Switch.pkt` — the ready-made Packet Tracer topology.
  Open it in Cisco Packet Tracer; do not rename it to anything else.

## Software needed
- Cisco Packet Tracer (free with a Cisco Networking Academy / NetAcad
  account). Download it from NetAcad, sign in once, then open `.pkt` files
  from your computer. No code or extra install is needed for this experiment.

## How to open and see the output
1. Open Cisco Packet Tracer, then File > Open > `Exp4_Hub_Switch.pkt`.
2. First check the topology in Realtime mode (bottom-right tabs):
   click any PC > Desktop > IP Configuration and note its IP address.
   Do the same for the other PCs.
3. Test connectivity: click a PC > Desktop > Command Prompt, then
   `ping <other PC's IP>`. A successful reply proves the LAN works.
4. Now switch to Simulation mode (bottom-right) to *see* the difference:
   - Click "Add Simple PDU" (the closed-envelope icon), click the source
     PC, then the destination PC, then press Play / Auto Capture.
   - On the hub side, watch the frame copy go to every connected PC.
   - On the switch side, after the first ping, watch the frame go only
     to the destination PC.
5. Check what the switch learned: click the switch > CLI, then run
   `enable` and `show mac-address-table`. The PCs' MAC addresses appear
   after they have sent traffic. A hub has no CLI at all — that is part
   of the point: a hub cannot learn addresses, it only repeats.

## What to write in the report
- The ping results (success / replies) for the hub LAN and the switch LAN.
- What Simulation mode showed on each side (broadcast to all vs. unicast
  to one), and the switch's MAC table after traffic.
- One-line conclusion: hub = one collision domain, repeats everything;
  switch = learns MACs, forwards selectively, so less unnecessary traffic.

## Common problems
- Ping fails: check each PC's IP and subnet mask in IP Configuration —
  PCs that must talk to each other need to be on the same network.
- No frames in Simulation mode: make sure you added the Simple PDU and
  pressed Play; Realtime mode does not animate frames.
