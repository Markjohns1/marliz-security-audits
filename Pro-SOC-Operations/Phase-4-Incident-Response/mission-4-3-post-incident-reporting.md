# Mission 4.3: Post-Incident Reporting
**Phase:** 4 (Incident Response)
**Objective:** Documenting the incident for stakeholders and future defense.

---

## 1. The Purpose of the Report
A post-incident report serves three audiences:

1.  **Technical Team:** What happened, how was it stopped, and what needs to be fixed.
2.  **Management:** Business impact, cost, and strategic risk.
3.  **Legal/Compliance:** Evidence of due diligence and regulatory adherence.

---

## 2. Report Structure (The Marliz Standard)

### Section 1: Executive Summary
A one-paragraph overview for non-technical leadership.

**Example:**
"On February 8, 2026, an unauthorized actor gained access to a legacy workstation via a phishing email. The intrusion was detected within 10 minutes, and the system was isolated. No data exfiltration occurred. Root cause was identified as a lack of MFA on the compromised account."

### Section 2: Incident Timeline
A chronological breakdown of the attack and response.

| Time (UTC) | Event |
| :--- | :--- |
| 10:05 | Phishing email delivered to user inbox. |
| 10:12 | User clicked malicious link, credentials harvested. |
| 10:15 | Attacker logged in from external IP. |
| 10:17 | SIEM alert triggered for anomalous login. |
| 10:22 | Account disabled, session terminated. |

### Section 3: Technical Analysis
Detailed breakdown of the attack chain, including:
*   Initial Access Vector (e.g., Phishing, RDP, VPN)
*   Persistence Mechanisms (e.g., Scheduled Task, Registry Key)
*   Lateral Movement (e.g., Compromised Service Account)
*   Exfiltration Attempt (e.g., Data copied to cloud storage)

### Section 4: Impact Assessment
Quantifiable damage.
*   Data affected (number of records, sensitivity level).
*   Downtime (hours, days).
*   Financial cost (direct and indirect).

### Section 5: Remediation Actions Taken
What was done to stop the attack.
*   Account disabled.
*   Malware quarantined.
*   Firewall rules updated.

### Section 6: Recommendations
Long-term improvements to prevent recurrence.
*   Enforce MFA on all accounts.
*   Implement email filtering for phishing.
*   Conduct user awareness training.

---

## 3. Professional Narrative
"Authored comprehensive post-incident reports adhering to industry standards, providing actionable insights for technical teams and executive leadership. Reports served as foundational documents for remediation efforts and compliance audits."

**Status:** Mission 4.3 Complete.
