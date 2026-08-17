# Incident Digest — The idempotency proof that was actually a first boot: kalmia run #1 breaks apt on the daily driver, 2026-08-06

*A "prove it's idempotent" run turned out to be the first live test of a
never-validated profile — and its first defect took out package management for
the whole machine. Its second defect had been silently winning for weeks.*
Compiled 2026-08-12 from a multi-session transcript harvest, cross-checked
against GitHub ground truth. All times **America/New_York (EDT, UTC-4)**.

**Deployment-caused:** yes

---

## TL;DR

Asked to run kalmia's full `site.yml` on the ThinkPad "as an idempotency
proof," the session discovered the box had actually been provisioned by the
retired predecessor bash — making this the **first live test** of the
`ubuntu_laptop` profile, not a re-run. Run #1 (ok=42 changed=8 failed=1) left
**apt broken host-wide**: the editors role preseeds
`code/add-microsoft-repo=true` (under a comment claiming it *skips* the
prompt), so VS Code's postinst recreated the legacy `vscode.list` whose
`Signed-By` collides with kalmia's deb822 `vscode.sources` — and apt refuses
to read *any* source on a Signed-By conflict. Manual repair (remove the legacy
list), root cause filed (kalmia#73), fix merged via issue-dispatch (#74) and
verified on the same hardware: runs #2/#3 converged to `changed=0` and held
across a reboot into the new kernel.

The same session then proved a second, quieter defect: TLP battery-charge
thresholds had been **silently stranded since adoption** — the predecessor's
drop-in file wins on lexical sort order, so every ansible run reported success
while sysfs never changed. Proven empirically (config 40/50, `changed=2`,
sysfs still 75/80; remove the predecessor file and sysfs tracks immediately),
fixed with a live sysfs acceptance test in both directions (kalmia#83 → #86);
the detection gap — the role still can't *see* a future conflicting drop-in —
remains open as kalmia#85.

---

## Timeline

| Time | Event |
|---|---|
| 20:07 | Session starts; discovery that the box was provisioned by the retired bash — profile never live-tested |
| 20:13–20:18 | Run #1: ok=42 changed=8 failed=1 — "Run #1 found a real bug — and it has left `apt` broken on this laptop" |
| 20:18–20:20 | Mechanism pinned: debconf preseed → postinst recreates legacy list → Signed-By conflict → "apt refuses to read *any* sources … takes out package management on the host" |
| 20:20 | Manual repair: legacy list removed (backed up first); kalmia#73 filed |
| 20:28 | Micro-lesson: bullpen dispatch attempted off-LAN — "there is no bullpen available here - dispatch via tagging claude in the issue comments" |
| ~20:45 | Fix PR #74 (via @claude issue dispatch) reviewed, merged; run #2 ok=58 changed=9 |
| 21:00–21:16 | TLP defect proven empirically and fixed (kalmia#83 → PR #86, sysfs acceptance test); #85 filed for the detection gap |
| 21:19 | Run #3 `changed=0`; convergence holds across reboot into kernel 7.0.0-29 |

---

## What did NOT happen

- **Nothing was lost.** Apt breakage blocked installs, not the running
  system; the repair was one file removal, with a backup taken first.
- **The 149-package upgrade (incl. kernel) in the same session was
  operator-approved** and unrelated to the defect.
- **The convergence claim was not faked by the bug**: the session explicitly
  noted `changed=0` passes *with the TLP bug present* — and built the sysfs
  acceptance test precisely because convergence proves nothing about hardware.

## CTO lessons

1. **An idempotency proof on a host the code never provisioned is a first
   boot.** Treat it as one: expect run #1 to find bugs, take backups, and
   don't schedule it when a broken host would hurt. The framing ("proof")
   almost set the wrong risk posture; the discovery of the box's real
   provenance corrected it in time.
2. **Adoption leaves predecessor artifacts that beat the new system
   silently.** A lexically-earlier drop-in from the retired tooling out-ranked
   kalmia's managed file for weeks of green runs. Adoption roles must sweep
   for conflicting predecessor files — and until kalmia#85 closes, the sweep
   is manual.
3. **Convergence is not correctness.** `changed=0` measures the config file,
   not the battery. Acceptance tests must read the hardware surface (sysfs),
   in both directions — which is what #86 shipped.
4. **Comments lie; verify preseed semantics.** The role's comment claimed the
   preseed *skips* the Microsoft-repo prompt; it *answers yes* to it. The
   whole outage hangs off that one wrong word.

---

## Sources

Session `67396661` (2026-08-06, `~/repos/kalmia`); kalmia#73/#74 (branch
`claude/issue-73-20260807-0021`), #76/#77, #83/#85/#86; run recaps
ok=42/58/57, changed=8/9/0; repair `rm /etc/apt/sources.list.d/vscode.list`;
sysfs evidence 75/80 ↔ 40/50.
