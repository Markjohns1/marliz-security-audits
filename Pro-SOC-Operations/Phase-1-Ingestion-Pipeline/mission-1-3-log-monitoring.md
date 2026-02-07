# Mission 1.3: Strategic Monitoring & Baseline Analysis
**Phase:** 1 (Ingestion Pipeline)
**Objective:** Establishing high-fidelity monitoring and situational awareness.

---

## 1. Tactical Monitoring Principles
Monitoring is the active observation of system behavior to identify deviations from an established baseline.

### Monitoring vs. Alerting
*   **Monitoring:** The constant visibility into the "Health" and "Heat" of the network.
*   **Alerting:** The specific notification triggered when a condition is met (e.g., a "Bang" event).

---

## 2. High-Value Telemetry Sources
A professional SOC focuses on specific logs that reveal adversary movement:

### A. Identity & Authentication (Who?)
*   **Windows Event ID 4624/4625:** Successful and failed logons.
*   **Pattern:** Multiple failed logons followed by a success (Brute Force).

### B. Process Execution (How?)
*   **Sysmon Event ID 1 / Windows 4688:** Process creation logs.
*   **Pattern:** Non-standard binaries (like PowerShell or CMD) spawned by web server processes (RCE).

### C. Network Connectivity (Where?)
*   **Sysmon Event ID 3:** Network connection events.
*   **Pattern:** Direct IP connections to known malicious C2 (Command & Control) infrastructure.

---

## 3. Dashboard Architecture
To maintain visibility, a SOC requires three distinct tiers of dashboards:

1.  **Level 1: Operational Monitoring (Health)**
    *   Metrics: EPS (Events Per Second), pipeline latency, heartbeat of shippers.
2.  **Level 2: Security Monitoring (The "Heat Map")**
    *   Metrics: Top 10 blocked IPs, failed logon spikes, active threat map.
3.  **Level 3: Forensics & Hunting (The "Deep Dive")**
    *   Metrics: Detailed search interfaces for investigating specific Indicator of Compromise (IoCs).

---

## 4. Practical: Detecting Unauthorized Configuration Changes
One of the most effective monitors is **FIM (File Integrity Monitoring)**.

### Case: Preventing Web Defacement or Backdoors
*   **Mechanism:** Monitor the filesystem for changes to sensitive files (e.g., `.htaccess`, `config.php`, `init.php`).
*   **Logic:** If a change occurs outside of a "Change Window" or is performed by a non-admin account, trigger a Critical Alert.

---

## 📑 Professional Narrative
"Designed and deployed enterprise-grade SOC dashboards providing real-time visibility into high-value telemetry. Established behavior-based baselines to identify anomalous activity, significantly reducing the Mean Time to Detect (MTTD) for sophisticated endpoint intrusions."

**Status:** Mission 1.3 Complete.
