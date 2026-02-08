# DFIR Incident Report: Remote Keylogger Intrusion (Win10)
**Case Number:** MI-2026-002  
**Status:** [CONTAINED / REMEDIATED]  
**Severity:** HIGH  

## 1. Executive Summary
On 2026-02-08, a legacy Windows 10 workstation was identified as compromised via a remote-deployed keylogger. The adversary established persistence without physical access. This report documents the forensic artifacts discovered during the post-incident investigation and the remediation steps taken by Marliz Intel Security.

---

## 2. Incident Timeline
*   **Discovery:** [Time] - User noticed [Symptoms, e.g., slow system, mysterious files].
*   **Initial Response:** [Time] - Host disconnected from network; suspected malicious process terminated.
*   **Forensic Investigation:** [Time] - Commenced deep-dive into Registry and Event Logs.
*   **Resolution:** [Time] - Eradication of persistence and password reset completed.

---

## 3. Forensic Findings
### 3.1. Persistence Mechanism (The "Hook")
*   **Type:** [e.g., Registry Run Key / Scheduled Task]
*   **Path:** `C:\Users\%USERNAME%\AppData\Local\...`
*   **MD5/SHA-256 Hash:** `[Insert Hash Here]`

### 3.2. Exfiltration Vector (The "Phone Home")
*   **Attacker C2 IP:** `[External IP Address]`
*   **Port:** [e.g., 443, 80, 22]
*   **Country of Origin:** [Lookup via GeoIP]

### 3.3. Entry Point (The "Door")
*   **Vector:** [e.g., RDP Brute Force / Unpatched Exploit / Drive-By Download]
*   **Evidence:** Event ID 4624 found with Source Network Address: `[Attacker IP]`.

---

## 4. Remediation & Hardening
The following steps were taken to "Domain Heal" the asset:
1.  **Process Kill:** Malicious process `[ProcessName]` terminated.
2.  **Artifact Removal:** Deleted Registry key at `HKCU\...\Run`.
3.  **Credential Reset:** Force-reset all passwords for user accounts on the machine.
4.  **Service Hardening:** Disabled [RDP/SMB/Other Services] and enabled Windows Firewall.

---

## 5. Conclusion
The intrusion was successful due to [Reason, e.g., outdated OS patches or exposed RDP]. While the immediate threat has been neutralized, the credential leakage necessitates a global password reset of all services accessed from this machine during the compromise window.

**Analyst:** [Your Name / Marliz Intel]
