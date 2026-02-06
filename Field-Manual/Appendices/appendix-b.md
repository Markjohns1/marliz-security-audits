# Appendix B: Pentest Report Template

---

**Marliz Intel Security**
**Penetration Test Report**

**Target:** [DOMAIN]
**Scope:** Black Box (No credentials provided)
**Date:** [DATE]

## 1. Summary of Findings

Our assessment identified **3 Critical** and **2 High** vulnerabilities. The system is currently highly susceptible to compromise.

## 2. Risk Matrix

| ID | Vulnerability | Severity | Status |
| :--- | :--- | :--- | :--- |
| VULN-01 | Remote Code Execution | Critical | Open |
| VULN-02 | Exposed .env File | Critical | Open |
| VULN-03 | Default Admin Credentials | High | Open |

## 3. Detailed Findings

**VULN-01: Remote Code Execution via File Upload**

**Description:**
The file upload function at `/upload.php` does not validate file extensions. Multiple PHP shells were successfully uploaded and executed.

**Proof of Concept:**
1.  Created file `shell.php`.
2.  Uploaded via standard form.
3.  Navigated to `/uploads/shell.php`.
4.  Executed command `whoami`.
5.  Result: `www-data`.

**Recommendation:**
Implement a strict whitelist of allowed MIME types (e.g., `image/jpeg`, `image/png`) and rename all uploaded files to a random hash.

## 4. Conclusion

The application requires immediate attention. It is recommended to take the site offline until VULN-01 is patched.
