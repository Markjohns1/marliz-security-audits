# Chapter 2.8: Case Study: The Playkart Full Kill Chain

---

## 20 Minutes to Total Compromise

This case study details a Red Team engagement performed by Marliz Intel in late 2025. The target, "Playkart," was a rapidly deployed e-commerce platform built using the Vibe Coding methodology.

**Target**: Playkart (Anonymized)
**Goal**: Access Customer PII (Personally Identifiable Information)
**Time Elapsed**: 22 Minutes

## Phase 1: Reconnaissance (T+00:00)

We began with a simple ping. The domain resolved to a direct IP address hosted on a budget VPS provider. There was no Cloudflare. No WAF.

## Phase 2: Enumeration (T+00:05)

We ran `gobuster` against the target.

```bash
gobuster dir -u http://playkart.com -w common.txt -x php,bak,zip
```

**Result:**
- `/admin` (301 Redirect -> Login Page)
- `/uploads` (200 OK - Directory Listing Enabled)
- `/test` (200 OK)

## Phase 3: The Leak (T+00:10)

Inside the `/test` directory, we found a file named `db_test.php`.
The developer created this file to check if the database connection was working.

**Content of `db_test.php`:**
```php
<?php
$conn = new mysqli("localhost", "playkart_admin", "Keny@2025!", "playkart_db");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>
```

The file printed "Connected successfully" to the screen. However, because the server display errors were on, we triggered a warning by sending invalid parameters, which leaked the stack trace. More importantly, we simply guessed the file structure based on standard generic patterns. But in this specific instance, we didn't initially see the password.

**Correction**: We found `db_test.php.bak` in the same folder.
This file contained the credentials in plain text.

## Phase 4: The Takeover (T+00:15)

We opened MySQL Workbench.
We input the IP address and the credentials found in the backup file.
The connection was successful. The firewall was open.

## Phase 5: Persistence (T+00:22)

We queried the `admin_users` table.
We updated the password hash for the `super_admin` user.
We logged into the Playkart dashboard as the administrator.

## Aftermath

We had full control of the orders, customer addresses, and phone numbers. We generated a report and closed the connection.

The developer had focused on the frontend animations. They forgot that a chain is only as strong as its weakest link. In this case, the link was a forgotten backup file in a test directory.

---

"Security is not a product. It is a process. And Playkart had neither."
Marliz Intel Field Manual
