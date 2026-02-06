# Appendix D: Raw Log Examples

---

## 1. SQL Injection / Blind SQLi

**Pattern**: `UNION SELECT`, `ORDER BY`, single quotes `'`.
```
192.168.1.5 - - [01/Feb/2026:14:00:00 +0300] "GET /product.php?id=1' UNION SELECT 1,user,pass,4 FROM users-- HTTP/1.1" 200 4056
```

## 2. Directory Scanning (Dirbusters)

**Pattern**: Rapid 404s for common filenames.
```
192.168.1.5 - - [01/Feb/2026:14:02:00 +0300] "GET /admin.php HTTP/1.1" 404 203
192.168.1.5 - - [01/Feb/2026:14:02:00 +0300] "GET /administrator/ HTTP/1.1" 404 203
192.168.1.5 - - [01/Feb/2026:14:02:01 +0300] "GET /backup.zip HTTP/1.1" 404 203
```

## 3. Path Traversal (LFI)

**Pattern**: `../`, `etc/passwd`, `boot.ini`.
```
192.168.1.5 - - [01/Feb/2026:14:05:00 +0300] "GET /index.php?page=../../../../etc/passwd HTTP/1.1" 200 1500
```
Note: A 200 OK here indicates the attack SUCCEEDED.

## 4. Shell Upload / RCE

**Pattern**: `POST` to upload, followed immediately by `GET` to the same name.
```
192.168.1.5 - - [01/Feb/2026:14:10:00 +0300] "POST /upload.php HTTP/1.1" 200 45
192.168.1.5 - - [01/Feb/2026:14:10:05 +0300] "GET /uploads/shell.php?cmd=whoami HTTP/1.1" 200 12
```
