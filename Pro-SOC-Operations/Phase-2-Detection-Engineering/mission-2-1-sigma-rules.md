# Mission 2.1: Sigma Rules - The Universal Detection Language
**Phase:** 2 (Detection Engineering)
**Objective:** Writing platform-agnostic detection logic that translates across SIEM platforms.

---

## 1. The Detection Problem
Every SIEM has its own query language. Splunk uses SPL, Elasticsearch uses KQL, Microsoft Sentinel uses its own dialect. If you write a detection rule for one platform, it is useless on another.

### Sigma: The Solution
Sigma is a YAML-based format for writing detection rules that can be converted into any SIEM's native language. Write once, deploy everywhere.

---

## 2. Anatomy of a Sigma Rule
A Sigma rule consists of four core blocks:

### A. Title & Metadata
Identifies the rule and provides context.

```yaml
title: Suspicious PowerShell Execution
status: experimental
description: Detects encoded PowerShell commands commonly used by attackers.
author: Marliz Intel Security
date: 2026/02/08
```

### B. Log Source
Specifies which log type the rule applies to.

```yaml
logsource:
    category: process_creation
    product: windows
```

### C. Detection Logic
The core of the rule. Defines what patterns to match.

```yaml
detection:
    selection:
        CommandLine|contains:
            - '-enc'
            - '-EncodedCommand'
            - 'FromBase64String'
    condition: selection
```

### D. Severity & MITRE Mapping
Links the detection to the ATT&CK framework for professional reporting.

```yaml
level: high
tags:
    - attack.execution
    - attack.t1059.001
```

---

## 3. Practical: Detecting the AMSI Bypass
Recall the bypass from the Field Manual. Here is how we detect it:

```yaml
title: AMSI Bypass via Reflection
status: stable
description: Detects attempts to manipulate the amsiInitFailed flag via .NET reflection.
author: Marliz Intel Security
logsource:
    product: windows
    service: powershell
detection:
    selection:
        ScriptBlockText|contains|all:
            - 'System.Management.Automation.AmsiUtils'
            - 'amsiInitFailed'
    condition: selection
level: critical
tags:
    - attack.defense_evasion
    - attack.t1562.001
```

---

## 4. Converting to SIEM-Specific Queries
Using open-source tools like `sigmac` or `sigma-cli`, the above YAML is converted:

### Splunk (SPL):
```spl
index=windows sourcetype=powershell ScriptBlockText="*System.Management.Automation.AmsiUtils*" AND ScriptBlockText="*amsiInitFailed*"
```

### Elastic (KQL):
```kql
event.category:process AND powershell.script_block_text:*AmsiUtils* AND powershell.script_block_text:*amsiInitFailed*
```

---

## 5. Professional Narrative
"Developed platform-agnostic detection logic using the Sigma standard, enabling rapid deployment across heterogeneous SIEM environments. Authored high-fidelity rules targeting memory-resident evasion techniques (MITRE T1562.001), significantly reducing adversary dwell time."

**Status:** Mission 2.1 Complete.
