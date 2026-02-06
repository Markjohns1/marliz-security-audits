# Chapter 2.4: Credential Harvesting: Reading config.php

---

## The Keys to the Kingdom

In 99% of PHP applications, the database connection details are stored in a file named `config.php`, `db.php`, or `.env`.

This file contains four critical pieces of information:
1. **DB_HOST**: Where the database lives.
2. **DB_NAME**: The name of the data store.
3. **DB_USER**: The username authorized to access it.
4. **DB_PASS**: The password that protects it.

If an attacker reads this file, they own the data.

## The Visibility Paradox

If you navigate to `target.com/config.php` in your browser, you will see a blank page.

This is because the server identifies the `.php` extension, executes the code within (which sets variables but outputs no text), and sends the empty result to the browser. The secrets remain hidden in the server's memory.

To steal the credentials, we must trick the server into treating the file as **text** instead of **code**.

## Method 1: The Backup Mistake (The Vibe Coder Special)

When a developer edits the configuration, they often save a backup. They rename the file to `config.php.bak` or `config.php.old`.

This is a critical error.

Most web servers (Apache/Nginx) are configured to execute `.php` files. They are *not* configured to execute `.bak` files. When you request `target.com/config.php.bak`, the server treats it as a plain text file and invites you to download it.

You open the text file. You see the password.

## Method 2: The View Source Vulnerability

Sometimes, developers leave "source code viewers" in production to help them debug.

`target.com/view.php?file=index.php`

If we change the parameter to `config.php`, the script reads the file content and displays it on the screen.

## Method 3: LFI with Wrappers

If the site has a Local File Inclusion vulnerability (e.g., `?page=home`), simply requesting `?page=config.php` will not work. The server will include and *execute* the config file. You still see nothing.

We must use PHP Filters to encode the payload.

Payload: `?page=php://filter/convert.base64-encode/resource=config.php`

This forces the server to base64 encode the file content *before* displaying it. The browser displays a long string of random characters. We copy this string, decode it locally, and reveal the plaintext code.

---

"A secret that is written down is only as safe as the paper it is written on."
Marliz Intel Field Manual
