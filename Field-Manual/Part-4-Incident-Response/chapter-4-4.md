# Chapter 4.4: Writing DFIR Reports

---

## The Paperwork of War

After the battle is won, you must account for it. A DFIR (Digital Forensics and Incident Response) report is not a blog post. It is a legal document. It may be read by CEOs, lawyers, or insurance adjusters.

## The Structure

A professional report has three sections.

### 1. Executive Summary
**Audience**: The CEO / Non-Technical Client.
**Length**: 1 Page.
**Content**:
- **What happened?** (High-level: "We were hacked.")
- **How bad was it?** (Impact: "Customer data was accessed.")
- **Is it over?** (Status: "The vulnerability is patched and attackers are ejected.")
- **What next?** (Recommendation: "We need a full code audit.")

**Do NOT** include IP addresses or code snippets here. Use plain English. "The attacker used a stolen password" is better than "Credential stuffing attack via compromised hash."

### 2. Technical Timeline
**Audience**: The CTO / Developers / Other Analysts.
**Length**: As long as necessary.
**Content**: A second-by-second reconstruction of the attack.

| Time (UTC) | Event | Evidence |
| :--- | :--- | :--- |
| 14:02:01 | IP 192.168.1.5 scans port 80 | access.log |
| 14:02:15 | File `shell.php` uploaded | file system timestamp |
| 14:03:00 | Database `users` table dumped | mysql.log |

### 3. Root Cause Analysis (RCA)
**Audience**: The Developer who has to fix it.
**Content**: The specific vulnerability that allowed the breach.

- **Vulnerability**: Unrestricted File Upload.
- **Location**: `upload.php` line 42.
- **Paylod Used**: `evil.php.jpg`.
- **Remediation**: Implement strict file type checking using MIME types.

## The Tone

Be objective.
**Bad**: "The lazy developer forgot to check the password."
**Good**: "The authentication mechanism lacked improper input validation."

Do not speculate. Only state what the logs prove. If you don't know how they got in, say "Entry vector: Unknown." Do not guess.

---

"If it is not written down, it did not happen."
Marliz Intel Field Manual
