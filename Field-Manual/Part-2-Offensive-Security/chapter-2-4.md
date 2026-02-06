# Chapter 2.4: Credential Harvesting: Reading config.php

---

## The Keys to the Kingdom

In 99% of PHP applications, the database connection details are stored in a file named `config.php`, `db.php`, or `.env`.
This file contains the **Crown Jewels**: `DB_HOST`, `DB_NAME`, `DB_USER`, and `DB_PASS`.

If an attacker reads this file, the firewall does not matter. The encryption does not matter. The attacker *is* the admin.

## The Mechanic: How Web Servers Handle Files

To understand how to steal this file, you must understand how Apache and Nginx work.

When you request `https://target.com/index.php`, the server looks at the extension `.php`.
1.  It sees `.php` in its MIME mapping.
2.  It sends the file to the **PHP Preprocessor (PHP-FPM)**.
3.  PHP executes the code (`<?php $pass="secret"; ?>`).
4.  PHP returns the *output* (which is usually nothing for a config file).
5.  The browser sees a blank page.

**The Goal:** We must trick the server into skipping Step 2. We want the server to treat the file as **Plain Text**, not **Code**.

---

## Method 1: The Backup Mistake (The Vibe Coder Special)

Vibe Coders are terrified of breaking things. So before they edit the config to change a password, they make a copy.
They rename `config.php` to `config.php.bak`, `config.php.old`, or `config.php_copy`.

### The Vulnerability
Apache knows that `.php` is code.
Apache *does not* know what `.bak` is.

When you request `target.com/config.php.bak`:
1.  Server checks extension `.bak`.
2.  No handler exists for `.bak`.
3.  Server falls back to default behavior: **Serve as Download** (`application/octet-stream`).
4.  The browser downloads the raw source code.

**War Story: The "Hidden" Dotfile**
A Kenyan SACCO had a secure site. But the developer used `nano` to edit files on the server.
When `nano` crashes or is closed improperly, it leaves a recovery file named `.config.php.swp` (Swap file).
We scanned for `.swp` files. We downloaded it. It contained the database credentials.
**Lesson**: Tools leave artifacts. Artifacts leak data.

---

## Method 2: PHP Wrapper LFI (Bypassing Execution)

If the site has a Local File Inclusion vulnerability (e.g., `index.php?page=about`), everyday attackers try to read `/etc/passwd`.
Pros try to read `config.php`.

**The Failure:**
Request: `index.php?page=config.php`
Result: The server `include()`s the file. It executes it. You see a blank screen because `$password = "123"` produces no HTML output.

**The Fix: `php://filter`**
PHP has a built-in stream wrapper system. We can tell PHP to "filter" the stream before using it.

**Payload:**
`index.php?page=php://filter/convert.base64-encode/resource=config.php`

**What happens:**
1.  PHP opens `config.php`.
2.  PHP passes the content through the `base64-encode` filter.
3.  The opening tag `<?php` becomes `PD9waHA=`.
4.  Since it no longer looks like code, the `include()` statement treats it as a string and prints it to the screen.

**The Result:**
You see a massive block of random text:
`PD9waHANCiRkYl91c2VyID0gJ2FkbWluJzsNCiRkYl9wYXNzID0gJ3N1cGVyc2VjcmV0Jzs...`

**The Loot:**
Copy that string. Run `base64 -d` on your terminal.
You now have the source code.

---

## Method 3: The Text Editor Artifacts

Developers use VS Code, JetBrains, or Sublime Text. These editors create hidden folders like `.vscode/` or `.idea/`.
Often, the `sftp-config.json` file inside these folders contains the FTP credentials for the server, stored in plain text.

**Attack Vector:**
`GET /.vscode/sftp.json`
`GET /.idea/webServers.xml`

If the `.gitignore` didn't catch these, and they were uploaded, you just compromised the FTP account.

---

## Drill: The Manual Check

Don't rely on tools. Use `curl` to verify exactly what the server is telling you.

```bash
# Check for backup file
curl -I -X GET https://target.com/config.php.bak

# Analyze Headers
HTTP/1.1 200 OK
Content-Type: text/plain  <-- THIS IS THE WIN
Content-Length: 456
```

If `Content-Type` is `text/html`, it executed (Bad for us).
If `Content-Type` is `text/plain` or `application/octet-stream`, it downloaded (Good for us).

---

"A secret that is written down is only as safe as the paper it is written on."
Marliz Intel Field Manual
