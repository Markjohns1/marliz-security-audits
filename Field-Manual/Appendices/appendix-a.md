# Appendix A: DFIR Report Template

---

**Marliz Intel Security**
**Incident Response Report**

**Date:** [DATE]
**Client:** [CLIENT NAME]
**Case ID:** [CASE ID]

## 1. Executive Summary
On [DATE], Marliz Intel detectors observed suspicious activity targeting [DOMAIN]. An immediate investigation confirmed that an unauthorized actor had gained access to the system via [VECTOR].

The threat was contained at [TIME], and all access was revoked. No sensitive financial data was exfiltrated. The system has been patched and returned to full operational status.

## 2. Incident Timeline

| Time (EAT) | Activity | Source |
| :--- | :--- | :--- |
| 14:00 | Attacker scans port 80 | 192.168.1.5 |
| 14:05 | SQL Injection payload sent | 192.168.1.5 |
| 14:06 | Database dumps user table | System Logs |
| 14:10 | Marliz Firewall blocks IP | Automated |

## 3. Technical Findings

**Vulnerability:** SQL Injection (SQLi)
**Location:** `/search.php` (Line 42)
**Impact:** Full Database Read Access.

**Evidence:**
[INSERT SCREENSHOT OF LOGS]

## 4. Remediation Actions Taken

1.  **Patched Code:** Implemented PDO Prepared Statements.
2.  **Credental Rotation:** Reset all admin passwords.
3.  **Firewalling:** Blocked attacker subnet.

## 5. Recommendations

1.  Keep PHP updated to version 8.2+.
2.  Enable automated database backups.
3.  Schedule a clean-code audit in Q3.

**Signed:**
John Mark Oguta
Lead Analyst, Marliz Intel
