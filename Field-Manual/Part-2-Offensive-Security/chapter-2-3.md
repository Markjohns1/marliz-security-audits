# Chapter 2.3: Remote Code Execution: The eval() Disaster

---

## The Apex Predator of Vulnerabilities

Remote Code Execution (RCE) is the highest severity vulnerability that can exist on a web server. It allows an attacker to bypass the application logic entirely and execute commands directly on the operating system.

It turns a website visitor into a server administrator.

## Understanding eval()

In PHP (and JavaScript/Python equivalents), `eval()` is a function that takes a string of text and executes it as code.

```php
$code = "echo 'Hello World';";
eval($code);
```

This seems harmless until user input is introduced.

## The Diagnostic Backdoor

Vibe Coders often ask AI for a way to "remotely debug" their application or "run commands from the browser." The AI frequently suggests the following pattern:

```php
// debug.php
if (isset($_GET['cmd'])) {
    eval($_GET['cmd']);
}
```

This three-line script is a nuclear weapon.

## The Kill Chain

Once an attacker discovers this file (often via Directory Enumeration), the exploitation is trivial.

### Step 1: Verification
The attacker sends a simple mathematical operation or print command to confirm code execution.

URL: `target.com/debug.php?cmd=echo 10+10;`
Output: `20`

### Step 2: System Reconnaissance
The attacker switches from PHP code to System commands using `system()` or `shell_exec()`.

URL: `target.com/debug.php?cmd=system('whoami');`
Output: `www-data`

This confirms they are running as the web server user.

### Step 3: Total Takeover
The attacker keeps the "webshell" purely in memory or writes a more permanent backdoor.

URL: `target.com/debug.php?cmd=system('ls -la /');`

They can now read `/etc/passwd`. They can traverse directories. They can delete the entire database.

## Why It Happens

Developers resort to `eval()` when they need "dynamic behavior" but lack the architectural skill to implement it safely. They want to calculate prices dynamically or run custom logic for a specific client.

Instead of building a rule engine, they just let the client (and the hacker) write the rules.

---

"If you invite the user to write code, do not be surprised when they write an exploit."
Marliz Intel Field Manual
