# Mission 3.2: Indicator of Compromise (IOC) Management
**Phase:** 3 (Tactical Hunting)
**Objective:** Operationalizing threat intelligence for active defense.

---

## 1. What is an IOC?
An Indicator of Compromise (IOC) is a forensic artifact that indicates a potential intrusion. IOCs are the "fingerprints" of an attacker.

### Types of IOCs:

| Type | Description | Example |
| :--- | :--- | :--- |
| **Hash** | Unique identifier of a malicious file | `e99a18c428cb38d5f260853678922e03` |
| **IP Address** | Known C2 (Command & Control) server | `185.220.101.45` |
| **Domain** | Malicious domain used for phishing | `secure-login-update.com` |
| **URL** | Specific malicious resource | `http://evil.com/payload.exe` |
| **Registry Key** | Persistence mechanism | `HKCU\Software\Microsoft\...\Run` |

---

## 2. The IOC Lifecycle
IOCs have a lifespan. A domain used today may be burned tomorrow.

### Stages:
1.  **Acquisition:** Received from threat intel feeds (MISP, AlienVault OTX, etc.).
2.  **Validation:** Confirmed as malicious (not a false positive).
3.  **Deployment:** Pushed to SIEM, EDR, and Firewall for blocking/alerting.
4.  **Expiration:** Removed after a defined period (e.g., 90 days) unless refreshed.

---

## 3. Deploying IOCs in Practice

### A. SIEM Watchlists
Create a lookup table of malicious IPs/Domains. Alert when any log matches.

**Splunk Example:**
```spl
| inputlookup malicious_ips.csv
| join type=inner src_ip [search index=firewall]
```

### B. EDR Blocklists
Push file hashes to the EDR to prevent execution.

### C. DNS Sinkholing
Redirect traffic to known malicious domains to an internal server. This prevents the malware from "phoning home" and allows you to identify infected hosts.

---

## 4. Threat Intel Platforms
A professional SOC uses a Threat Intelligence Platform (TIP) to manage IOCs:

*   **MISP:** Open-source, widely used for sharing IOCs.
*   **OpenCTI:** Modern platform with STIX/TAXII support.
*   **Recorded Future / Mandiant:** Commercial, premium intel.

---

## 5. Professional Narrative
"Managed the IOC lifecycle from acquisition to expiration, integrating threat intelligence feeds into SIEM and EDR platforms. Automated IOC deployment using MISP-to-Splunk pipelines, reducing manual effort and ensuring real-time protection against emerging threats."

**Status:** Mission 3.2 Complete.
