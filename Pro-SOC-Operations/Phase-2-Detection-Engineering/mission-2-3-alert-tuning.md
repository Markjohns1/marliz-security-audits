# Mission 2.3: Alert Tuning - Reducing Noise Without Losing Signal
**Phase:** 2 (Detection Engineering)
**Objective:** Engineering high-fidelity alerts that analysts trust.

---

## 1. The "Alert Fatigue" Problem
An untuned SIEM generates thousands of alerts per day. Analysts become desensitized. True positives (real attacks) are lost in a sea of false positives (noise). This is how breaches happen.

### The Marliz Standard:
An alert should only fire when an analyst needs to act. If the alert is informational, it belongs on a dashboard, not in a queue.

---

## 2. Tuning Methodologies

### A. Whitelisting (Exclusion)
Remove known-good activity from triggering alerts.

**Example:** PowerShell is flagged as suspicious, but the IT admin uses it daily.
**Solution:** Whitelist the admin's username or workstation in the rule.

```yaml
detection:
    selection:
        CommandLine|contains: '-enc'
    filter:
        User: 'SVC_AdminAutomation'
    condition: selection and not filter
```

### B. Threshold Adjustment
Require multiple events before alerting.

**Example:** A single failed login is normal. 50 failed logins in 5 minutes is a brute force.
**Solution:** Set a threshold.

```yaml
condition: selection | count() by src_ip > 50 within 5m
```

### C. Enrichment
Add context to the alert to help the analyst decide faster.

**Example:** An alert fires for a login from an unusual country.
**Enhancement:** Enrich the alert with geo-IP data and the user's normal login locations.

---

## 3. The Tuning Lifecycle
Alert tuning is not a one-time task. It is a continuous process:

1.  **Deploy:** Push the new rule to production.
2.  **Monitor:** Track the alert volume for 7 days.
3.  **Analyze:** Review false positives. Identify patterns.
4.  **Refine:** Add filters or adjust thresholds.
5.  **Document:** Record the change in the rule's changelog.

---

## 4. Metrics for Success
A healthy detection environment is measured by:

| Metric | Target |
| :--- | :--- |
| **False Positive Rate** | Less than 10% |
| **Mean Time to Acknowledge (MTTA)** | Less than 15 minutes |
| **Alert-to-Incident Ratio** | Greater than 1:5 (1 in 5 alerts is a real incident) |

---

## 5. Professional Narrative
"Implemented a continuous alert tuning program, reducing false positive rates by 40% and improving analyst efficiency. Developed whitelisting and threshold-based logic to ensure high-fidelity alerting aligned with the MITRE ATT&CK framework."

**Status:** Mission 2.3 Complete.
