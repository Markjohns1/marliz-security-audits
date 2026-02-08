# Chapter 6.6: MySQL Workbench for Reconnaissance

---

## Not Just for DBAs

We have discussed using MySQL Workbench for exploitation (Chapter 2.5), but it is also a powerful **Reconnaissance** tool.

## The Connection Test

When you are scanning a range of IPs (e.g., a subnet belonging to a company), you can use Workbench to test for open doors without needing complex command-line scanners.

1.  **New Connection**.
2.  **Hostname**: Target IP.
3.  **Port**: 3306.
4.  **Username**: `root` (or `admin`, `backup`).
5.  **Test Connection**.

If the server responds:
> "Access Denied for user 'root' used password NO"

You know three critical facts:
1.  **The port is open** (you bypassed the firewall).
2.  **MySQL is running** on that server.
3.  **The root user exists** (username enumeration).

This is valuable information leakage.

## Visualizing the Loot

If you manage to steal credentials (e.g., from a `config.php` file), using the command line `mysql -u root -p` is tedious and hard to read.

Workbench allows you to:
1.  **Reverse Engineer**: Click "Database" -> "Reverse Engineer" to generate a full **Entity Relationship Diagram (ERD)**. You can see how the tables link, helping you find the "Crown Jewels" (User tables, Transaction tables) instantly.
2.  **Export Data**: Right-click a table -> "Export Table Data" -> CSV. This is how you generate Proof of Concept (PoC) artifacts for your report efficiently.

## The Tunnel (Bypassing Firewalls)

Workbench has built-in SSH Tunneling, which is a common hacker technique made easy.

**Scenario:** The database port (3306) is blocked by a firewall, but SSH (22) is open. You have compromised a user (e.g., `git` or `www-data` via SSH key theft).

**The Setup:**
1.  **Connection Method**: Standard TCP/IP over SSH.
2.  **SSH Host**: Target IP (The web server).
3.  **SSH User**: `www-data` (The compromised user).
4.  **MYSQL Host**: `127.0.0.1` (Internal to the server).

**Result:** You are now managing the "internal-only" database from your remote laptop, tunneling your traffic through the SSH connection. The firewall sees only encrypted SSH traffic.

---

"A GUI is not a sign of weakness. It is a tool for speed."
Marliz Intel Field Manual
