# Mission 3.1: Hypothesis-Driven Threat Hunting
**Phase:** 3 (Tactical Hunting)
**Objective:** Find the attacker before the alert fires.

---

## 1. Why Hunting Matters

Here is the uncomfortable truth: Your SIEM will miss things. Not because it is broken, but because:
- The attacker used a technique you did not have a rule for.
- The attacker moved slowly enough to stay below your thresholds.
- The attacker used your own tools against you (Living off the Land).

Hunting is how you find what the rules missed. You do not wait for an alert. You assume the attacker is already inside and you go looking for them.

---

## 2. The Hunting Cycle (Step by Step)

### Step 1: Form a Hypothesis
Start with a question based on real-world attacker behavior.

**Example Hypothesis:** "An attacker who stole credentials via phishing is now using them to access internal systems during off-hours when nobody is watching."

Why this hypothesis? Because attackers know your security team works 9-5. They move at 2 AM.

### Step 2: Identify Your Data
What logs would show this behavior?
- Windows Security Event 4624 (Successful Logon)
- LogonType 10 (Remote Desktop) or LogonType 3 (Network)
- Timestamp outside business hours

### Step 3: Write the Query

**Splunk SPL:**
```spl
index=windows sourcetype=WinEventLog:Security EventCode=4624 LogonType IN (3,10)
| eval hour=strftime(_time, "%H")
| where hour < 6 OR hour > 22
| stats count by src_ip, user, hour
| where count > 1
```

**Elastic KQL:**
```kql
event.code:4624 AND (winlog.event_data.LogonType:3 OR winlog.event_data.LogonType:10)
| where hour_of_day < 6 OR hour_of_day > 22
```

### Step 4: Analyze the Results
You get a list of users who logged in between 10 PM and 6 AM. Now ask:
- Is this a known night-shift worker?
- Is this the CEO traveling internationally (time zone difference)?
- Is this a service account that runs scheduled jobs?
- Or is this an attacker who stole credentials?

### Step 5: Document Everything
Whether you find something or not, document:
- The hypothesis
- The query
- The results
- The conclusion

This becomes institutional knowledge. Next time, someone else can run the same hunt.

---

## 3. Real Hunt Scenarios (Execute These)

### Hunt A: Credential Dumping (Mimikatz Detection)
**Hypothesis:** An attacker is using Mimikatz to extract passwords from memory.

**Indicator:** Mimikatz accesses lsass.exe (the process that stores credentials).

**Query (Sysmon Event 10: Process Access):**
```spl
index=sysmon EventCode=10 TargetImage="*lsass.exe"
| where SourceImage!="*\\MsMpEng.exe" AND SourceImage!="*\\csrss.exe"
| table _time, Computer, SourceImage, SourceUser
```

**What to look for:** Any non-system process touching lsass.exe is highly suspicious.

---

### Hunt B: Data Staging Before Exfiltration
**Hypothesis:** An attacker is collecting files into a staging folder before exfiltrating them.

**Indicator:** Large number of files copied to a single directory in a short time.

**Query (Windows Event 4663: File Access):**
```spl
index=windows EventCode=4663 ObjectType="File"
| stats count by ObjectName, SubjectUserName
| where count > 100
| sort -count
```

**What to look for:** A user copying 500 files to `C:\Users\Public\` or similar is worth investigating.

---

### Hunt C: Persistence via Scheduled Tasks
**Hypothesis:** An attacker created a scheduled task to maintain access.

**Indicator:** New scheduled task created by a non-admin user.

**Query (Windows Event 4698: Scheduled Task Created):**
```spl
index=windows EventCode=4698
| where SubjectUserName!="SYSTEM" AND SubjectUserName!="*admin*"
| table _time, Computer, SubjectUserName, TaskName, TaskContent
```

**What to look for:** Tasks with encoded PowerShell commands or tasks that point to files in Temp directories.

---

## 4. The Hunt Report Template

After every hunt, fill this out:

```
Hunt ID: HUNT-2026-02-001
Date: 2026-02-08
Analyst: [Your Name]

Hypothesis: [What you were looking for]
Data Sources: [Windows Security, Sysmon, Firewall, etc.]
Query: [The actual query you ran]
Time Range: [Last 7 days, Last 30 days, etc.]

Findings:
- [List what you found]

Conclusion:
- [True Positive / False Positive / Inconclusive]

Recommendations:
- [Create a detection rule? Notify the user? Escalate to IR?]
```

---

## Professional Narrative
"Executed hypothesis-driven threat hunts targeting credential harvesting, data staging, and persistence mechanisms. Developed and documented repeatable hunting queries for common ATT&CK techniques (T1003 Credential Dumping, T1053 Scheduled Tasks, T1074 Data Staging). Identified dormant adversary activity that evaded automated detection."

**Status:** Mission 3.1 Complete.
