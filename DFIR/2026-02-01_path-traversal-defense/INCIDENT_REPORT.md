# Incident Report: Path Traversal Attack Defense
**Date:** February 1, 2026  
**Severity:** Critical (P0)  
**Status:** Resolved / Hardened  
**Lead Analyst:** John Mark Oguta (SOC Analyst - Detection & Correlation)  

---

## 1. Executive Summary
On February 1, 2026, at approximately 17:38 (Local Time), the Marliz Sec News platform was targeted by a sophisticated **Path Traversal (CWE-22)** attack. The attacker attempted to exfiltrate sensitive system configuration files including SSH keys, environment variables, and password hashes. 

The incident was identified in real-time by **John Mark Oguta** during routine log monitoring. The collaborative SOC response successfully contained the breach with an **Elite Response Time**, maintaining a **total Dwell Time of under 10 minutes**. All compromised credentials were rotated before the adversary could establish persistence.

---

## 2. Incident Classification
*   **Attack Type:** Path Traversal / Local File Inclusion (LFI)
*   **Vulnerability:** Weak input validation in the SPA catch-all route.
*   **Threat Actor IP:** `45.88.186.70`
*   **Impact:** Confirmed Read-Access to `/proc/self/environ` and system files.

---

## 3. Detailed Timeline

### **Phase 1: Detection (17:38 - 17:40)**
*   Live logs identified suspicious `GET` requests using `../../../../../../` sequences.
*   **Confirmed Leaks:** `/etc/passwd`, `/proc/self/environ`, `~/.ssh/id_rsa`, `.aws/credentials`

### **Phase 2: Analysis & Hotfix (17:41 - 17:45)**
*   **Root Cause:** The `serve_react_app` function used `os.path.join()` without validating the resolved path.
*   **Hotfix:** Implemented strict ".." detection and `os.path.abspath` normalization.

### **Phase 3: Containment (17:46 - 18:45)**
*   Docker rebuild executed: `docker compose up -d --build`
*   All API keys rotated immediately.

### **Phase 4: Recovery (18:46 - 19:00)**
*   DB audit confirmed no unauthorized records.
*   Attacker IP now receives `403 Forbidden`.

---

## 4. Technical Fix

```python
# The Ironclad Shield
if ".." in full_path or full_path.startswith("/"):
    raise HTTPException(status_code=403, detail="Forbidden")

abs_dist = os.path.abspath(FRONTEND_DIST)
requested_path = os.path.abspath(os.path.join(FRONTEND_DIST, full_path))
if not requested_path.startswith(abs_dist):
    raise HTTPException(status_code=403, detail="Forbidden")
```

---

## 5. Response Metrics

| Metric | Value | Industry Benchmark |
| :--- | :--- | :--- |
| **MTTD** | < 2 Minutes | Hours to Days |
| **MTTR** | < 8 Minutes | Hours to Weeks |
| **Dwell Time** | < 10 Minutes | 21+ Days Average |
| **Persistence** | 0% | Variable |

---

## 6. Raw Evidence Logs

```text
marliz-sec-news  | INFO:     45.88.186.70:27636 - "GET /../../../../../../etc/passwd HTTP/1.1" 200 OK
marliz-sec-news  | INFO:     45.88.186.70:56340 - "GET /../../../../../../root/.ssh/id_ed25519 HTTP/1.1" 200 OK
marliz-sec-news  | INFO:     45.88.186.70:56692 - "GET /../../../../../../proc/self/environ HTTP/1.1" 200 OK
marliz-sec-news  | WARNING:app.main:SECURITY ALERT: Blocked attempt to access ../../../../../../proc/self/cwd/.env from 45.88.186.70
marliz-sec-news  | INFO:     45.88.186.70:56752 - "GET /../../../../../../proc/self/cwd/.env HTTP/1.1" 403 Forbidden
```

---

**Report Author:** John Mark Oguta  
**Verified by:** Marliz Security Operations Center  
**Case Status:** CLOSED
