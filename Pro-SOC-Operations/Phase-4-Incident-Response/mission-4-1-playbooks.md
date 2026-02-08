# Mission 4.1: Incident Response Playbooks
**Phase:** 4 (Incident Response)
**Objective:** Structured procedures for containing and eradicating active threats.

---

## 1. What is a Playbook?
A playbook is a documented, repeatable procedure for responding to a specific type of security incident. It removes guesswork and ensures consistency.

### Playbook Categories:
*   **Malware Infection**
*   **Phishing Attack**
*   **Account Compromise**
*   **Data Exfiltration**
*   **Ransomware**

---

## 2. The Universal Response Framework (PICERL)
All playbooks follow the NIST framework:

| Phase | Objective |
| :--- | :--- |
| **P - Preparation** | Ensure tools, access, and contacts are ready. |
| **I - Identification** | Confirm the incident is real, not a false positive. |
| **C - Containment** | Stop the bleeding. Isolate the affected asset. |
| **E - Eradication** | Remove the threat (malware, backdoor, attacker access). |
| **R - Recovery** | Restore systems to normal operation. |
| **L - Lessons Learned** | Post-mortem analysis. What failed? What can improve? |

---

## 3. Sample Playbook: Account Compromise

### Trigger:
Alert fires for "Successful Login from Anomalous Location."

### Identification:
1.  Review the alert details (User, Source IP, Timestamp).
2.  Check geo-IP: Is this country associated with the user's normal activity?
3.  Contact the user: "Did you log in from [Location] at [Time]?"

### Containment:
1.  If confirmed malicious, disable the user account immediately.
2.  Terminate all active sessions for that user.
3.  Block the source IP at the firewall.

### Eradication:
1.  Force a password reset for the compromised account.
2.  Review the account's activity for the past 7 days. What did the attacker access?
3.  Revoke any API keys or tokens associated with the account.

### Recovery:
1.  Re-enable the account after the user confirms the new password.
2.  Monitor the account closely for 30 days.

### Lessons Learned:
*   Was MFA enabled? If not, enforce it.
*   Was the password reused from another breach? Check with HaveIBeenPwned.

---

## 4. Professional Narrative
"Authored and maintained incident response playbooks for common attack vectors including account compromise and malware infections. Reduced Mean Time to Respond (MTTR) by 35% through standardized, documented procedures aligned with the NIST Incident Response framework."

**Status:** Mission 4.1 Complete.
