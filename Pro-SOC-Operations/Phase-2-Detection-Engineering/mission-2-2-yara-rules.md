# Mission 2.2: YARA Rules - File & Memory Pattern Matching
**Phase:** 2 (Detection Engineering)
**Objective:** Identifying malicious files and memory artifacts through byte-level pattern matching.

---

## 1. What is YARA?
YARA is the "pattern matching swiss army knife" for malware researchers. While Sigma detects behavior in logs, YARA detects patterns in files and memory.

### Use Cases:
*   Scanning a suspicious executable for known malware signatures.
*   Detecting a web shell (like our `ajax_session_handler.php`) on a compromised server.
*   Hunting for in-memory payloads that never touch disk.

---

## 2. Anatomy of a YARA Rule
A YARA rule consists of three sections:

### A. Metadata
Provides context about the rule.

```yara
rule Marliz_PHP_Webshell
{
    meta:
        author = "Marliz Intel Security"
        description = "Detects PHP web shells with common backdoor patterns"
        severity = "critical"
        date = "2026-02-08"
```

### B. Strings
Defines the patterns to search for. Can be text, hex, or regex.

```yara
    strings:
        $eval_pattern = "eval($_" ascii nocase
        $base64_decode = "base64_decode" ascii
        $system_call = /system\s*\(/ nocase
        $shell_exec = "shell_exec" ascii
        $passthru = "passthru" ascii
```

### C. Condition
The logic that determines a match.

```yara
    condition:
        filesize < 50KB and
        (2 of ($eval_pattern, $base64_decode, $system_call, $shell_exec, $passthru))
}
```

---

## 3. Practical: Detecting Our Own Backdoor
Recall `ajax_session_handler.php` from the Playkart audit. Here is a YARA rule to detect it:

```yara
rule Marliz_AjaxBackdoor_POC
{
    meta:
        author = "Marliz Intel Security"
        description = "Detects the Ajax Session Handler POC backdoor"
        reference = "Internal Pentest - Playkart Audit"
    strings:
        $magic_key = "99af53" ascii
        $action_read = "readfile" ascii
        $action_exec = "exec_cmd" ascii
    condition:
        all of them
}
```

---

## 4. Deploying YARA in a SOC
YARA is not run manually in a pro environment. It is integrated into:

*   **EDR Platforms:** CrowdStrike and SentinelOne use YARA for custom IOC detection.
*   **Malware Sandboxes:** Cuckoo and Any.Run scan submitted files with YARA.
*   **CI/CD Pipelines:** Security teams scan code repositories for malicious patterns before deployment.

---

## 5. Professional Narrative
"Authored custom YARA signatures for identifying web shell implants and fileless malware artifacts. Integrated rule sets into EDR and sandbox environments, enabling proactive threat hunting and reducing incident response time for web application compromises."

**Status:** Mission 2.2 Complete.
