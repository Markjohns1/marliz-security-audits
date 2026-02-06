# Chapter 2.7: Path Traversal (LFI): Reading System Files

---

## Escaping the Web Root

A web server is designed to keep visitors inside a specific directory, usually `/var/www/html`. Path Traversal (also known as Local File Inclusion or LFI) is the vulnerability that allows an attacker to step outside this sandbox and roam the entire server file system.

## The Mechanism

The vulnerability exists when an application takes a filename as input and passes it directly to a filesystem function.

**Vulnerable Code:**
```php
$page = $_GET['page']; // User input: "home"
include($page . ".php"); // Includes "home.php"
```

The developer expects the user to request "contact" or "about."
The attacker requests: `../../../../etc/passwd`

The code executes: `include("../../../../etc/passwd.php");`

Note: In modern PHP versions, the null byte injection (`%00`) required to strip the `.php` extension is patched. However, many include functions do not force an extension, or the attacker targets files that *have* the extension (like other PHP config files).

## High-Value Targets

When we have LFI, we look for system files that prove the compromise or leak information.

1. **Linux**: `/etc/passwd`
   - Returns a list of all users on the system. Useful for brute-forcing SSH later.
2. **Linux**: `/proc/self/environ`
   - In containerized environments (Docker/Kubernetes), API keys are often stored in environment variables. LFI here leaks everything.
3. **Windows**: `C:\Windows\win.ini`
   - Standard proof of existence for Windows servers.
4. **Application Logs**: `/var/log/apache2/access.log`
   - If we can read the logs, we can poison them. (See: Log Poisoning techniques).

## Defense: Whitelisting

Sanitization (removing `../`) is prone to failure. Attackers use `....//` or URL encoding to bypass filters.

The only secure method is a strict whitelist.

**Secure Code:**
```php
$allowed = ['home', 'about', 'contact'];
if (in_array($_GET['page'], $allowed)) {
    include($_GET['page'] . '.php');
} else {
    // 404 Error
}
```

---

"The filesystem is a tree. Do not let the user climb it."
Marliz Intel Field Manual
