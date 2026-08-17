# Incident Digest — WireGuard handshake black-hole on ChromeOS, 2026-06-25

*A three-hour layered diagnosis that exonerated the server with a packet
capture: 446 handshake initiations in, 249 responses out, zero data packets —
and the culprit was the client's app container all along.*
Compiled 2026-07-13 by Home Claude from local session transcripts in
`~/.claude/projects/` (harvested by the `/incident-digest` full-history scan).
All times **America/New_York (EDT, UTC-4)**; raw transcript timestamps are UTC.

**Deployment-caused:** no

---

## TL;DR

The operator's Chromebook "connected" to the Firewalla's WireGuard VPN but lost
all network access — the classic full-tunnel black-hole: the client routes
`0.0.0.0/0` into a tunnel whose data path never actually came up. Over one
evening session (19:01–22:20) the diagnosis moved through four layers — peer
config, hardened client profile, kernel handshake logs, raw packet capture —
each ruling out a candidate until only one remained: **the WireGuard Android
app, running inside ChromeOS's ARC++ container, silently drops the inbound
handshake responses**. The server was healthy the entire time. Recreating the
tunnel in ChromeOS's *native* built-in WireGuard client fixed it in seconds.

The diagnostic ladder, each rung evidence-backed:

1. **The lie in the UI** — client says "connected"; server says
   `last_handshake_epoch = 0`: the handshake *never once completed*.
2. **Hardened profile, identical failure** — fresh keypair, IPv4-literal
   endpoint, `PersistentKeepalive 25`, matched MTU: still `handshake NEVER`,
   which comprehensively ruled out the client *config*.
3. **The kernel's word** — the box was receiving initiations and sending
   responses ~25×/second, plus periodic "Invalid handshake" complaints from
   stale retries.
4. **The 35-second capture** — 446 INIT packets in, 249 RESP packets out (each
   correctly addressed, physically leaving the WAN interface), **0 transport
   packets** in either direction. The response leaves the server and never
   reaches the app.

Nothing was broken on the Firewalla and nothing was lost; the cost was one
evening of methodical elimination. The lesson is that **"connected" is a
client-UI claim, not a cryptographic one** — and that ChromeOS's ARC++
container is not a trustworthy network path for a VPN client.

---

## Timeline (EDT)

| Time | Event | Evidence |
|---|---|---|
| 19:01 | Session starts: *"hop into my firewall and report on the wireguard vpn. I can connect from my Chromebook but I lose all network access"* | transcript first prompt |
| 19:02–19:03 | Server side read-only sweep: interface up, forwarding on, NAT sane, inbound `udp/51820 ACCEPT` | `wg` dump, iptables |
| 19:04 | **Smoking gun**: peer shows `last_handshake_epoch 0` — *never* handshaked — while rx keeps climbing across probes. The initiations arrive and are cryptographically valid (the server learns/updates the peer endpoint, which only happens for a valid peer), so keys are fine; the *loop* never closes | `wg` peer dump |
| 19:07 | Report delivered: server healthy; full-tunnel `0.0.0.0/0` into a dead data path black-holes all client traffic; break is in the handshake **return path** | transcript |
| 19:26–19:28 | Config-model established: client private keys live only in the phone app (never on the box). A second peer appears live mid-session — flagged to the operator before touching anything, to avoid colliding with his parallel app-side attempts | `wg0.conf` + redis reads |
| 20:26 | `wg0.conf` backed up (`wg0.conf.bak.20260625-202609`) | on-box backup |
| 20:27 | **Hardened peer deployed** (additive, reversible): fresh keypair, `PersistentKeepalive 25`, IPv4-literal endpoint (the box's DDNS name resolves IPv6-first — a dual-stack black-hole risk found en route), MTU 1412 | transcript |
| 21:57 | Hardened peer: **`handshake NEVER`** after ~260 KiB of pure init/response ping-pong. Client config now comprehensively ruled out | `wg` dump |
| 21:58 | Routing re-verified clean: single WAN egress, correct fwmark, no SNAT on the control plane | ip rule / iptables |
| 22:00 | Kernel logs during a live connect: `Receiving handshake initiation` → `Sending handshake response`, repeating ~25×/second, with periodic `Invalid handshake` from stale retries | dmesg |
| 22:08 | **The decisive capture (35 s):** 446 × INIT (148 B) in, 249 × RESP (92 B) out — every response to the exact source of the inits, leaving eth0 — and **zero transport/keepalive/data packets** | tcpdump tally |
| 22:11 | Diagnosis locked. Client is the WireGuard **Android app via QR** on a personal Chromebook → app runs in the **ARC++ container**, which is not delivering inbound handshake responses to it. Fix: ChromeOS **native built-in** WireGuard | transcript |
| 22:20 | **Working.** Native-client tunnel: `handshake: 37 sec ago` (was NEVER all night), full-size data packets both directions, zero new INITs on the wire | `wg` dump + live capture |

---

## The failure class — a VPN that fails *after* authenticating

What made this hard is that every cheap signal said "fine": the client UI said
connected, the server's rx/tx counters climbed, the keys authenticated (the
server demonstrably accepted the peer). The failure lived in one specific hop —
UDP responses crossing back into an app container — which no config option on
either end could touch. Two design choices turned that one lost hop into a
total outage:

- **Full-tunnel routing** (`AllowedIPs 0.0.0.0/0`): the client committed all
  traffic to the tunnel before the tunnel proved itself. A split-tunnel client
  would have degraded instead of black-holing.
- **No keepalive in the stock app profile**: nothing forced the half-open
  handshake to resolve or fail visibly; the app just retried forever while the
  user experienced "no internet."

The hardened-profile step (20:27) deserves a note even though it "failed": it
was the step that converted the diagnosis from plausible to certain. With
keypair, endpoint addressing, keepalive, and MTU all controlled and the failure
byte-for-byte identical, the remaining suspect list had exactly one entry.

## What did NOT happen (the reassuring part)

- **The Firewalla was never at fault and never at risk.** All changes were
  additive (one extra peer) with a timestamped config backup taken first;
  rollback was a one-liner. The original peers were untouched.
- **No key material was exposed.** Client private keys never existed on the
  box (app-side only); the new peer's keypair was generated fresh and handed
  over out-of-band. Nothing key-shaped appears in the repo or logs.
- **The household network was unaffected** — this was a remote-access path
  problem only; LAN, DNS, DHCP and the other VPN peers ran normally throughout.
- **What the cost actually WAS:** one evening (~3h20m) of operator+Claude
  diagnosis time, spent down a ladder that ruled out the server, the keys, the
  addressing, and the config before landing on the platform.

## CTO lessons — where governance was missing

1. **"Connected" needs a server-side definition.** The client UI's claim was
   false for the entire incident. The check that matters is the server's
   `latest handshake` age — cheap to poll, and worth a monitoring probe if VPN
   access ever becomes load-bearing (today it's convenience-tier; accepted as a
   manual check).
2. **Prefer the platform-native client on ChromeOS.** The Android app's ARC++
   network path silently drops inbound WireGuard handshake responses on this
   device class. This is now recorded in the homelab reference memory so no
   future session re-walks the ladder.
3. **Ship keepalive + IPv4-literal endpoints in client profiles by default.**
   Two latent risks found en route (no keepalive; DDNS resolving IPv6-first on
   dual-stack clients) are free to eliminate in every future exported profile
   even though neither was the root cause here.
4. **Announce before touching a surface the operator is also touching.** The
   mid-session appearance of a second peer (the operator experimenting in the
   app) was caught and flagged before any box-side change — the right reflex,
   post-06-19: state the collision risk, then act.

---

## Appendix — sources

```
Transcript:  ~/.claude/projects/-home-cpitzi/82e75bcc-*.jsonl
             (session 2026-06-25 19:01 → 22:20 EDT)
Ground truth: live wg peer dumps, dmesg handshake log, 35-second tcpdump tally,
             wg0.conf backup wg0.conf.bak.20260625-202609 (on-box)
No repo artifacts — appliance + client incident; lesson preserved in the
reference memory (WireGuard topology) and this report.
```
