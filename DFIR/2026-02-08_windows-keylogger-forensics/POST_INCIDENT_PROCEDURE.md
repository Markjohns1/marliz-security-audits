# Practical Lab: Forensic Investigation of a Remote Keylogger
**Case ID:** MARLIZ-2026-02-08-WK  
**Category:** Digital Forensics & Incident Response (DFIR)  
**Host System:** Windows 10 (Legacy)

---

## 🔬 Scenario
An external adversary successfully deployed a keylogger onto a workstation without physical access. The threat has been "kicked out," but the entry vector and persistence mechanisms remain unknown. Your goal is to conduct a **Post-Mortem Analysis** to ensure total eradication and document the incident for the Marliz Intel archive.

---

## 🛠️ Phase 1: Persistence Hunting (Where are they hiding?)
Attackers don't want to re-infect you every time you reboot. They hide in "Auto-Run" locations.

### Task 1.1: Check the Registry Run Keys
Open PowerShell as Administrator and run:
```powershell
Get-ItemProperty HKLM:\Software\Microsoft\Windows\CurrentVersion\Run
Get-ItemProperty HKCU:\Software\Microsoft\Windows\CurrentVersion\Run
```
**What to look for:** Any entry pointing to a file in `AppData`, `Temp`, or a file with a random name like `svchost_update.exe`.

### Task 1.2: Check Scheduled Tasks
Malware often creates a scheduled task to run at "Logon" or every 60 minutes.
```powershell
Get-ScheduledTask | Get-ScheduledTaskInfo | Select-Object TaskName, LastRunTime | Sort-Object LastRunTime -Descending | Select-Object -First 10
```

---

## 📡 Phase 2: Network Forensics (Who were they talking to?)
Keyloggers must exfiltrate (send) the data to the attacker's server (C2 - Command & Control).

### Task 2.1: Check Established Connections
```powershell
netstat -ano | findstr "ESTABLISHED"
```
**What to look for:** Look for IPs you don't recognize. Use a tool like `whois` or `shodan.io` to check if the destination IP belongs to a VPS provider (DigitalOcean, Linode) or a suspicious country.

---

## Phase 3: Log Auditing (How did they get in?)
We need to see if they remote-logged into your machine.

### Task 3.1: Audit Successful Network Logons (Event ID 4624)
```powershell
Get-WinEvent -FilterHashtable @{LogName='Security';ID=4624} | Select-Object -First 20 | Out-GridView
```
**Filter for:** Logon Type 3 (Network) or Logon Type 10 (Remote Interactive). If you see a logon from an IP that isn't yours—that's your entry vector.

---

## 📝 Phase 4: Deliverables for Portfolio
To prove you did this "Practical," you must create the following:

1.  **The Artifact Log**: A list of any suspicious files found.
2.  **The Evidence Screenshot**: (Simulate or capture) the Command Line output showing a suspicious connection or startup item.
3.  **The Hardening Script**: A small `.ps1` script that deletes the malicious task/registry key.

---

## ⚠️ Safety Warning
*   **Do not** execute any files you find during this investigation unless you are in a Sandbox/VM.
*   **Hash everything**: If you find a suspicious file, record its SHA-256 hash before deleting it.
