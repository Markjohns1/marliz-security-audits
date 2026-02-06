# Chapter 3.7: Building Honeypots: Trapping Script Kiddies

---

## Active Deception

Most security is passive. Firewalls, permissions, input validation. These are walls. A honeypot is a trap. It entices the attacker to reveal themselves by interacting with a resource that a legitimate user would never touch.

## 1. The Robots.txt Trap

Attackers always read `robots.txt` to see what you are hiding.

**The Setup:**
1. Create a file `robots.txt`.
2. Add: `Disallow: /super-secret-admin`
3. Create a PHP script at `/super-secret-admin`.

**The Trigger:**
Legitimate Google bots will respect the rule and stay away. Real users will never see the URL.
Only a hacker manually enumerating the site will visit it.

**The Payload:**
The script does not contain an admin panel. It contains a logger that blacklists the visitor's IP address immediately.

## 2. The Backup File Trap

We know attackers hunt for `.bak` files. Give them one.

**The Setup:**
Create `db_connect.php.bak` in the root directory.

**The Content:**
```php
<?php
$host = "192.168.1.50"; // Fake Internal IP
$user = "root";
$pass = "SuperSecretAdminPass123";
?>
```

**The Monitoring:**
Monitor your logs. Anyone who downloads this file is an attacker. Anyone who tries to log in with "SuperSecretAdminPass123" is confirmed hostile.

## 3. The Hidden Form Field

 Bots love to fill out every field in a form.

**The Setup:**
```html
<input type="text" name="website" style="display:none;">
```

**The Trigger:**
A human user does not see this field (CSS hidden). A bot reads the HTML, sees an input, and fills it.

**The Logic:**
```php
if (!empty($_POST['website'])) {
    die("Bot detected.");
}
```

## Why This Matters

Honeypots reduce noise. Instead of analyzing gigabytes of logs to find the attack, the attack isolates itself. If the alarm rings, you know with 100% certainty that you are being targeted.

---

"Do not just build a wall. Dig a moat. And fill it with crocodiles."
Marliz Intel Field Manual
