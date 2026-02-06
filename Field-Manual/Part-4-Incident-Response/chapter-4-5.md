# Chapter 4.5: Case Study: The February 1st Attack

---

## 03:00 AM: The Alarm

The Marliz Intel SOC runs automated log monitoring. At 03:14 AM on February 1st, 2026, the Slack channel `#alerts-critical` fired.

`[CRITICAL] High frequency of 404 errors from IP 45.132.xx.xx targeting /etc/passwd`

## 03:15 AM: Assessment (Observe/Orient)

The on-call analyst woke up.
The logs showed 400 requests in 2 seconds. This was not a human. It was a script.
They were targeting `index.php?page=...`.

**Observation**: Path Traversal attack.
**Status**: Failed (logs showed PHP Warnings, not file outputs).
**Orient**: The attacker was automated. They were likely scanning thousands of servers. They had not yet succeeded, but they were mapping our file structure.

## 03:17 AM: Decision

We had two choices:
1.  **Block the IP**: Easy. Temporary. They would just rotate IPs.
2.  **Patch the Code**: Fix the vulnerability permanently.

We chose both.

## 03:20 AM: Action

1.  **Code Patch**: The analyst SSH'd into the server.
    - Edited `index.php`.
    - Implemented the Whitelist array (See Chapter 3.6).
    - Time taken: 3 minutes.
2.  **Firewall Rules**:
    - Added the IP to the permanent blocklist.
    - Analyzed the IP on AbuseIPDB (Confidence score: 100% Abuse).

## 03:30 AM: Verification

We monitored the logs. The attacker's script continued for another 2 minutes, receiving `403 Forbidden` responses, then stopped. They realized the door was closed and moved on to a softer target.

## The Post-Mortem

Why did this happen?
Root Cause Analysis revealed that a junior developer had enabled a "dynamic page loader" feature to make the URL look cleaner, but failed to validate the input.

**Corrective Action**:
- All `include()` calls are now linted in CI/CD.
- Developers underwent a 1-hour training session on LFI.

---

"The attack failed not because we were lucky, but because we were awake."
Marliz Intel Field Manual
