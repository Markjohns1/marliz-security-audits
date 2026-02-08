# Mission 4.3: Post-Incident Reporting
**Phase:** 4 (Incident Response)
**Objective:** Document the incident so everyone learns from it.

---

## 1. Why the Report Matters

The incident is over. The attacker is out. Why spend hours writing a report?

**Three Reasons:**
1. **Legal Protection:** If you get sued or audited, this document proves you did your job.
2. **Process Improvement:** You will find what failed and fix it.
3. **Knowledge Transfer:** The next analyst who faces a similar attack will know what to do.

---

## 2. The Report Structure

Every incident report should have these sections:

### Section 1: Executive Summary
One paragraph. No jargon. Your CEO should understand this.

### Section 2: Incident Timeline
Minute-by-minute breakdown of what happened.

### Section 3: Technical Analysis
Deep dive for the security team. Attack chain, IOCs, forensic artifacts.

### Section 4: Impact Assessment
What was damaged? What was stolen? What did it cost?

### Section 5: Remediation Actions
What you did to stop the attack and prevent it from happening again.

### Section 6: Recommendations
Long-term improvements for the organization.

---

## 3. Filled Example: Real Incident Report

```
=============================================================
INCIDENT REPORT
=============================================================
Report ID: INC-2026-02-001
Classification: CONFIDENTIAL
Date: February 8, 2026
Author: Mark J., SOC Analyst, Marliz Intel Security

=============================================================
SECTION 1: EXECUTIVE SUMMARY
=============================================================

On February 8, 2026, at approximately 02:15 EAT, an unauthorized 
actor gained access to an employee workstation using stolen 
credentials. The attacker was detected within 7 minutes by our 
SIEM alerting system. The compromised account was disabled at 
02:22 EAT. No evidence of data exfiltration was found. The root 
cause was identified as a successful phishing attack combined 
with lack of multi-factor authentication on the affected account.

=============================================================
SECTION 2: INCIDENT TIMELINE
=============================================================

| Time (EAT) | Event |
|------------|-------|
| 02:10 | Phishing email delivered to user jsmith@company.com |
| 02:12 | User clicked link, entered credentials on fake login page |
| 02:15 | Attacker logged in from IP 185.220.101.45 (Tor exit node) |
| 02:17 | SIEM alert fired: "Login from anomalous location" |
| 02:18 | SOC analyst acknowledged alert, began investigation |
| 02:20 | Analyst confirmed malicious activity, initiated containment |
| 02:22 | Account jsmith disabled in Active Directory |
| 02:22 | All active sessions for jsmith terminated |
| 02:25 | Firewall rule added to block 185.220.101.45 |
| 02:30 | Incident declared contained |

=============================================================
SECTION 3: TECHNICAL ANALYSIS
=============================================================

Attack Chain (MITRE ATT&CK Mapping):

1. Initial Access (T1566.002 - Spearphishing Link)
   - Phishing email impersonating IT department
   - Link: hxxps://company-login-secure[.]com/auth
   - Credential harvesting page hosted on compromised WordPress site

2. Valid Accounts (T1078)
   - Attacker used stolen credentials to access OWA (Outlook Web App)
   - Source IP: 185.220.101.45 (Tor exit node, Germany)

3. Discovery (T1087 - Account Discovery)
   - Attacker ran "whoami" and "net user" commands
   - Evidence found in PowerShell command history

4. No Lateral Movement Detected
   - Attacker was contained before moving to other systems

Indicators of Compromise:
- IP: 185.220.101.45
- Domain: company-login-secure[.]com
- Phishing Email From: it-support@company-secure[.]net

=============================================================
SECTION 4: IMPACT ASSESSMENT
=============================================================

| Category | Impact |
|----------|--------|
| Data Exfiltration | None confirmed |
| Systems Compromised | 1 (jsmith workstation) |
| Accounts Compromised | 1 (jsmith@company.com) |
| Downtime | 0 hours (user account reset within 30 minutes) |
| Financial Cost | ~$500 (analyst time, password reset overhead) |
| Regulatory Impact | None (no PII accessed) |

=============================================================
SECTION 5: REMEDIATION ACTIONS TAKEN
=============================================================

Immediate Actions (During Incident):
[X] Disabled compromised account
[X] Terminated all active sessions
[X] Blocked attacker IP at firewall
[X] Reset user password
[X] Scanned workstation for malware (none found)

Post-Incident Actions (Within 24 Hours):
[X] Added phishing domain to email block list
[X] Added IOCs to SIEM watchlist
[X] Sent phishing awareness reminder to all staff
[X] Enabled MFA on affected account

=============================================================
SECTION 6: RECOMMENDATIONS
=============================================================

Short-Term (Within 1 Week):
1. Enforce MFA on all user accounts, not just VPN
2. Implement email banner for external senders
3. Add Tor exit node blocklist to firewall

Long-Term (Within 1 Month):
1. Deploy anti-phishing training with simulated attacks
2. Implement FIDO2 hardware keys for high-risk users
3. Review email filtering rules for credential harvesting patterns

=============================================================
APPROVAL
=============================================================

Prepared by: Mark J., SOC Analyst
Reviewed by: [Security Manager Name]
Approved by: [CISO Name]

=============================================================
END OF REPORT
=============================================================
```

---

## 4. How to Write the Executive Summary

The executive summary is the hardest part. Here is the formula:

**Sentence 1:** When did it happen?
**Sentence 2:** What did the attacker do?
**Sentence 3:** How fast did we respond?
**Sentence 4:** What was the impact?
**Sentence 5:** What was the root cause?

That is it. Five sentences. No technical jargon.

---

## Professional Narrative
"Authored comprehensive incident reports following industry-standard frameworks. Documented attack chains with MITRE ATT&CK mapping, enabling pattern recognition across multiple incidents. Provided actionable recommendations that reduced organizational attack surface and improved mean time to respond."

**Status:** Mission 4.3 Complete.
