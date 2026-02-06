# Chapter 2.6: The Inside Man Attack: Bypassing Firewalls

---

## When the Front Door is Locked

Sophisticated hosting environments or prudent sysadmins will block external access to Port 3306. If you try to connect via MySQL Workbench from your laptop, the connection will time out.

The firewall rules state: "Only allow connections from Localhost."

This stops external attackers. But it does not stop us, because we can become "Localhost."

## The Pivot Concept

The web application itself (WordPress, Laravel, custom PHP) is hosted on the same server network as the database. It connects via `localhost`. If we can execute code on the server, we inherit its privileges.

We need a database client that runs *on* the server.

## The Tool: Adminer

**Adminer** is a single-file PHP script that functions like phpMyAdmin. It creates a full database management GUI. It consists of one file, usually named `adminer.php`.

## The Execution

1. **Locate an Upload Vector**: We find an image upload form, a document submission portal, or we use a previously established Web Shell.
2. **Deploy the Agent**: We upload `adminer.php` to the server.
3. **Access**: We navigate to `https://target.com/uploads/adminer.php`.
4. **Connect**:
   - Server: `localhost` (This is the key. From the perspective of the script, it is local.)
   - Username/Password: From `config.php`.

## Bypassing the Firewall

The firewall sees an inbound HTTP request to port 443 (HTTPS). This is allowed traffic.
The web server executes the PHP script, which opens a connection to port 3306 *internally*. This is allowed traffic.

The firewall is effectively bypassed because the request originates from inside the castle.

## Cleanup

This method leaves a high-risk artifact on the server. If you leave `adminer.php` in a public directory, anyone can find it and brute force the database password. A responsible audit requires the immediate deletion of this tool after the proof-of-concept is documented.

---

"A wall is only as strong as the people you let inside the gate."
Marliz Intel Field Manual
