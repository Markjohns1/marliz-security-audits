# Chapter 3.6: Case Study: Path Traversal Defense (marlizintel.com)

---

## The February 1st Incident

This case study analyzes an attempted breach of the Marliz Intel public portal.

**Date**: February 1, 2026
**Vector**: Path Traversal (LFI)
**Status**: Mitigated

## The Attack Signature

At 03:14 AM EAT, our logs recorded the following request:

`GET /index.php?page=../../../../../../../../../../etc/passwd`

The attacker was attempting to break out of the web root to read the server's user list. This is a standard automated script from a botnet.

## The Configuration Failure

At the time, our error reporting was set to `E_ALL` (Development Mode).

**Server Response:**
`Warning: include(../../../../../../../../../../etc/passwd.php): failed to open stream: No such file or directory in /var/www/html/index.php on line 42`

While the LFI failed (because the attacker didn't null-terminate or handle the `.php` extension appended by our code), the error message revealed:
1. The full path of our script (`/var/www/html/`).
2. The fact that we were using `include()`.
3. The fact that we did not sanitize input.

We gave the attacker a map.

## The Remediation

We applied a three-layer defense within 15 minutes.

### Layer 1: The Whitelist (Code Level)
We replaced the dynamic include logic with a strict array check.

```php
$allowed_pages = ['home', 'services', 'about', 'contact'];
if (!in_array($_GET['page'], $allowed_pages)) {
    http_response_code(404);
    include('404.php');
    exit();
}
```

### Layer 2: Error Suppression (Config Level)
We edited `php.ini` to disable error display in production.

`display_errors = Off`

Now, if a hack fails, the screen remains blank. The attacker gets no feedback.

### Layer 3: The Trap (Network Level)
We configured Fail2Ban to monitor the Nginx logs. Any IP address requesting `etc/passwd` or `../` is immediately banned for 48 hours at the firewall level.

## Conclusion

The attack was unsophisticated, but it exposed a lack of "Defense in Depth." We relied on the file extension (`.php`) to save us. That is luck, not security. We now rely on explicit white-listing.

---

"Luck is not a strategy."
Marliz Intel Field Manual
