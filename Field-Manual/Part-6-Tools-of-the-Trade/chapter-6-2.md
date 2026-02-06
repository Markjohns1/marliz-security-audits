# Chapter 6.2: MySQL Workbench for Reconnaissance

---

## Not Just for DBAs

We have discussed using MySQL Workbench for exploitation (Chapter 2.5), but it is also a powerful Recon tool.

## The Connection Test

When you are scanning a range of IPs (e.g., a subnet belonging to a company), you can use Workbench to test for open doors.

1. **New Connection**.
2. **Hostname**: Target IP.
3. **Port**: 3306.
4. **Username**: `root` (or `admin`, `backup`).
5. **Test Connection**.

If the server responds "Access Denied for user 'root' used password NO," you know:
1. The port is open (bypass firewall).
2. MySQL is running.
3. The root user exists.

This is information leakage.

## Visualizing the Loot

If you steal credentials (`config.php`), using the command line `mysql -u root -p` is tedious.
Workbench allows you to:
1. **Reverse Engineer**: Click "Database" -> "Reverse Engineer" to generate a full Entity Relationship Diagram (ERD). You can see how the tables link, helping you find the "Crown Jewels" (User tables, Transaction tables).
2. **Export Data**: Right-click a table -> "Export Table Data" -> CSV. This is how you generate Proof of Concept (PoC) artifacts for your report.

## The Tunnel

Workbench has built-in SSH Tunneling.
If the database port (3306) is blocked, but SSH (22) is open, and you have compromised a user (e.g., `git` user or `www-data` via SSH key theft):
1. **Connection Method**: Standard TCP/IP over SSH.
2. **SSH Host**: Target IP.
3. **SSH User**: `www-data`.
4. **MYSQL Host**: `127.0.0.1` (Internal).

You can now manage the local database from your remote laptop, tunneling through the SSH protection.

---

"A GUI is not a sign of weakness. It is a tool for speed."
Marliz Intel Field Manual
