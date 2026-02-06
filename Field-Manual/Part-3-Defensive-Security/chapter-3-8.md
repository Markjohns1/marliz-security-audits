# Chapter 3.8: Log Monitoring: Seeing the Attack in Real-Time

---

## The Flight Recorder

When a plane crashes, identifying the cause relies on the Black Box. When a server crashes, we rely on the logs.

Logs are the only immutable record of what actually happened. Vibe Coders ignore them. Security Analysts live in them.

## The Matrix View

To see traffic as it hits your server, use the `tail` command.

```bash
tail -f /var/log/apache2/access.log
```

You will see a stream of requests.
`192.168.1.5 - GET /index.php 200`
`192.168.1.5 - GET /style.css 200`

## Identifying Hostility

You do not need AI to spot an attack. You just need to recognize the patterns.

### 1. The Scanner
Normal users click one link every few seconds. Scanners request 50 links per second.
If the log is scrolling faster than you can read, you are being scanned.

### 2. The Probe
If you see requests for software you do not use, it is a bot.
`GET /wp-admin/login.php` (On a custom PHP site)
`GET /phpmyadmin/` (When you don't have it installed)

### 3. The Payload
If the URL contains strange characters, it is an injection attempt.
`GET /id=1' UNION SELECT 1,2,3--`

## The Error Log: The Early Warning System

`access.log` shows traffic. `/var/log/apache2/error.log` shows pain.

If you see:
`PHP Warning: include(../../etc/passwd): failed`

This means someone *tried* LFI and failed. This is not a "system error." This is a "targeted attack."
Most admins ignore warnings. We do not. A warning is often the only notification you get before the breach becomes successful.

## Retention

Attackers wipe logs.
Solution: Ship your logs off-server.
Use `rsyslog` to send logs to a separate, locked-down server. If the web server is compromised, the evidence remains safe in the vault.

---

"Logs are truth. Everything else is hearsay."
Marliz Intel Field Manual
