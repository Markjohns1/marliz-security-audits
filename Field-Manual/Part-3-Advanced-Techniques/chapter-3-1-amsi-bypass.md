# Chapter 3.1: AMSI Bypass - Blinding the Security Guard
**Category:** Advanced Persistence / Evasion Techniques  
**Analyst:** Marliz Intel Security Team

---

## 1. Executive Theory: What is AMSI?
The **Antimalware Scan Interface (AMSI)** is a versatile interface standard that allows applications and services to integrate with any antimalware product on a computer. It is most famous for its role in **PowerShell**, where it scans scripts in memory before they are executed.

### Why "Gatekeepers" Hate This:
In the past, hackers could simply "Obfuscate" (mess up) their code so a static scanner couldn't read it. AMSI fixed this by waiting until the code is **de-obfuscated in memory** right before execution. This makes fileless attacks much harder—unless you blind the scanner first.

---

## 2. Practical Lab: The "Reflection" Patch
This is a classic (and often censored) technique. Instead of avoiding the scanner, we use a feature of .NET called **Reflection** to reach into the Windows memory and tell AMSI that it has failed to initialize.

### The Logic (Step-by-Step):
1.  **Locate**: We find the `AmsiUtils` class in the System Management namespace.
2.  **Access**: We use reflection to find a specific private field called `amsiInitFailed`.
3.  **Patch**: We set this field to `True`.
4.  **Result**: Every subsequent command you run will be ignored by AMSI because it "thinks" it is broken.

### The "Amsi-Blind" POC:
*Note: This is for educational research and signature development.*

```powershell
# This is a common obfuscated bypass string
[Ref].Assembly.GetType('System.Management.Automation.AmsiUtils').GetField('amsiInitFailed','NonPublic,Static').SetValue($null,$true)
```

---

## 3. The "Marliz Intel" Forensic Harvest
If an attacker uses the above bypass, standard Antivirus will see nothing. As a professional, you must know how to catch this.

### A. Script Block Logging (The Black Box)
Enable **PowerShell Script Block Logging** (GPO: Administrative Templates -> Windows Components -> Windows PowerShell).
*   **Event ID 4104**: This records the *entire* content of every script block executed.
*   **The Catch**: Even if the bypass is successful, the command to *do the bypass* is logged in plain text.

### B. Hunting for reflection
Search your SIEM or Event Logs for the following strings:
*   `[Ref].Assembly.GetType`
*   `amsiInitFailed`
*   `GetField`

---

## 4. Portfolio Conclusion (The "Job Hunter" Angle)
This module demonstrates your ability to operate at the **Memory & Kernel level**. 

**Key Takeaway for CV:**
"Engineered detection signatures for memory-resident bypass techniques, specifically targeting the AMSI (Antimalware Scan Interface) reflection vulnerability. Leveraged PowerShell Event ID 4104 (Script Block Logging) to perform forensic reconstruction of fileless attacks."

**Disclaimer:** This material is for authorized security testing and defensive research only.
