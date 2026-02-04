# Marliz Intel Security Audits

**Official Case Studies and Incident Response Reports**

This repository contains **real-world security audits**, **DFIR (Digital Forensics and Incident Response) reports**, and **penetration testing case studies** conducted by the **Marliz Intel Security** team.

These are not theoretical exercises. Every report documents a **live engagement** against real adversaries or live production systems.

---

## Repository Structure

```
marliz-security-audits/
├── README.md
├── DFIR/
│   └── 2026-02-01_path-traversal-defense/
│       └── INCIDENT_REPORT.md
└── Penetration-Tests/
    └── 2026-02-04_playkart-ecommerce-audit/
        └── VULNERABILITY_ASSESSMENT.md
```

---

## Featured Case Studies

### 1. Path Traversal Attack Defense (DFIR)
*   **Target:** marlizintel.com (Internal Asset)
*   **Date:** February 1, 2026
*   **Severity:** Critical (P0)
*   **Outcome:** Attacker exfiltrated sensitive files before detection. Full containment achieved within 10 minutes. Zero persistence established.
*   **Key Metrics:**
    *   MTTD (Mean Time to Detect): < 2 Minutes
    *   MTTR (Mean Time to Respond): < 8 Minutes
    *   Adversary Dwell Time: < 10 Minutes
*   [Read Full Report](./DFIR/2026-02-01_path-traversal-defense/INCIDENT_REPORT.md)

### 2. Playkart E-Commerce Security Audit (Penetration Test)
*   **Target:** playkartstores.com (External Client)
*   **Date:** February 4, 2026
*   **Severity:** Critical
*   **Outcome:** Identified RCE backdoors, plain-text credential leakage, and broken access controls.
*   [Read Full Report](./Penetration-Tests/2026-02-04_playkart-ecommerce-audit/VULNERABILITY_ASSESSMENT.md)

---

## About Marliz Intel Security

Marliz Intel Security is an independent cybersecurity intelligence firm specializing in:
*   **Penetration Testing & Vulnerability Research**
*   **Incident Response & Digital Forensics**
*   **Infrastructure Hardening & Secure Architecture**
*   **Threat Intelligence & Adversary Tracking**

We don't just find bugs; we engineer resilience.

---

## Contact

*   **Website:** [marlizintel.com](https://marlizintel.com)
*   **Lead Analyst:** Mark J.
