# Mission 4.2: Forensic Evidence Collection
**Phase:** 4 (Incident Response)
**Objective:** Preserving digital evidence for analysis and legal proceedings.

---

## 1. The Chain of Custody
Digital evidence is fragile. If improperly handled, it can be corrupted or deemed inadmissible in court. The Chain of Custody is a documented record of who handled the evidence and when.

### Requirements:
*   Evidence must be hashed (SHA-256) immediately upon collection.
*   Every access to the evidence must be logged.
*   Original evidence is never modified; work is done on a forensic copy.

---

## 2. Evidence Types

### A. Volatile Evidence (Memory)
Data that is lost when the system is powered off.
*   Running processes
*   Network connections
*   Logged-in users

**Collection:** Use tools like `winpmem`, `FTK Imager`, or `volatility`.

### B. Non-Volatile Evidence (Disk)
Data that persists after power off.
*   File system
*   Registry
*   Event logs

**Collection:** Create a bit-for-bit disk image using `dd`, `FTK Imager`, or `Guymager`.

---

## 3. The Order of Volatility
Collect evidence in order of how quickly it disappears:

1.  CPU Registers / Cache (Seconds)
2.  RAM (Minutes)
3.  Network Connections (Minutes)
4.  Running Processes (Minutes)
5.  Disk (Persistent)
6.  Remote Logs / Cloud (Persistent)

---

## 4. Practical: Capturing a Memory Dump (Windows)
This is the first step in any forensic investigation of a live Windows machine.

### Using WinPMem:
```powershell
winpmem_mini_x64.exe memory_dump.raw
```

### Verifying the Hash:
```powershell
Get-FileHash -Algorithm SHA256 memory_dump.raw
```

---

## 5. Artifact Locations (Windows)
Key forensic artifacts on a Windows system:

| Artifact | Location |
| :--- | :--- |
| **Event Logs** | `C:\Windows\System32\winevt\Logs\` |
| **Prefetch** | `C:\Windows\Prefetch\` |
| **NTUSER.DAT** | `C:\Users\<User>\NTUSER.DAT` |
| **Browser History** | `C:\Users\<User>\AppData\Local\...` |
| **Scheduled Tasks** | `C:\Windows\System32\Tasks\` |

---

## 6. Professional Narrative
"Executed forensic evidence collection procedures adhering to chain-of-custody best practices. Proficient in volatile memory acquisition and disk imaging, ensuring evidence integrity for internal investigations and external legal proceedings."

**Status:** Mission 4.2 Complete.
