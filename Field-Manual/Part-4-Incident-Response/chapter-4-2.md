# Chapter 4.2: Evidence Preservation: Capturing Raw Logs

---

## Do Not Clean Up (Yet)

The biggest mistake a junior sysadmin makes is "fixing" the hack immediately. They delete the malicious file. They restart the server.

By doing this, they destroy the evidence.

Digital Forensics and Incident Response (DFIR) requires a crime scene. If you mop up the blood, you cannot catch the killer.

## The Order of Volatility

Capture evidence in the order that it disappears.

1. **Memory (RAM)**: If you reboot, this is gone forever. This contains running processes, encryption keys, and active network connections.
   - Command: `lime` or `memdump` (Advanced).
   - Basic: `netstat -antp > /tmp/connections.txt`
   - Basic: `ps auxf > /tmp/processes.txt`

2. **Network State**: Who is connected right now?
   - Command: `ss -tunapl`

3. **Disk (Temporary)**: Files in `/tmp` or `/dev/shm`. Attackers love these folders because they are often world-writable.

4. **Disk (Persistent)**: The logs and the web root.

## The Snapshot Strategy

If you are on a cloud provider (AWS, DigitalOcean, Hostinger VPS), do not just copy files. **Take a Snapshot.**

A snapshot freezes the entire hard drive state at that exact second.
1. Take the snapshot.
2. Spin up a *new* droplet from that snapshot in an isolated sandybox network.
3. Perform your forensics on the copy.
4. Wipe the original server and rebuild.

## Secure Copy (SCP)

If you cannot snapshot, exfiltrate the logs immediately to your local machine.

```bash
scp -r root@target.com:/var/log/apache2/ ./evidence/logs/
scp -r root@target.com:/var/www/html/ ./evidence/html_dump/
```

## Hash Everything

Once you have the files, fingerprint them.

```bash
sha256sum access.log > access.log.hash
```

This proves that the evidence has not been tampered with. If you are ever in a legal situation (suing a developer or prosecuting an attacker), this chain of custody is required.

---

"Treat the server like a crime scene. Do not touch what you do not have to."
Marliz Intel Field Manual
