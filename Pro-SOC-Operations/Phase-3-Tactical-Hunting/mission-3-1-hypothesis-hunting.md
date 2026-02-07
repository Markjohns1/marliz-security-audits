# Mission 3.1: Hypothesis-Driven Threat Hunting
**Phase:** 3 (Tactical Hunting)
**Objective:** Proactively searching for adversaries before alerts fire.

---

## 1. Hunting vs. Alerting
Alerting is reactive. You wait for a rule to trigger. Hunting is proactive. You search for evidence of compromise based on a hypothesis.

### The Hunting Premise:
"Assume the attacker is already inside. Find them."

---

## 2. The Hunting Cycle
A professional hunt follows a structured methodology:

### Step 1: Form a Hypothesis
Based on threat intelligence or known attacker techniques.

**Example Hypothesis:** "An adversary may have stolen credentials via phishing and is using them for lateral movement during off-hours."

### Step 2: Identify Data Sources
Which logs contain evidence of this behavior?

*   Windows Security Logs (Logon Events - 4624, 4625)
*   Network Flows (Sysmon Event ID 3)
*   Firewall Logs

### Step 3: Execute the Hunt
Query the SIEM for the specific patterns.

**Query (Splunk SPL):**
```spl
index=windows EventCode=4624 LogonType=10
| stats count by src_ip, user, _time
| where _time > relative_time(now(), "-1d@d")
| search (date_hour < 6 OR date_hour > 22)
```

### Step 4: Analyze Results
Review the output. Is there a legitimate business reason for this activity?

### Step 5: Document Findings
Whether positive or negative, the hunt must be recorded.

---

## 3. Hunt Scenarios (The Marliz Playbook)

### Scenario A: Credential Harvesting
**Hypothesis:** An attacker is using Mimikatz to dump credentials.
**Indicator:** Unexpected access to `lsass.exe` by non-system processes.

### Scenario B: Data Exfiltration
**Hypothesis:** An insider is copying sensitive data to a cloud storage provider.
**Indicator:** High-volume outbound traffic to domains like `dropbox.com` or `mega.nz`.

### Scenario C: Persistence via Scheduled Tasks
**Hypothesis:** An attacker has created a hidden scheduled task for persistence.
**Indicator:** New scheduled task created by a non-admin user.

---

## 4. Professional Narrative
"Executed hypothesis-driven threat hunts targeting lateral movement and credential harvesting techniques (MITRE T1078, T1003). Identified dormant adversary activity that had evaded automated detection, resulting in successful containment before data exfiltration."

**Status:** Mission 3.1 Complete.
