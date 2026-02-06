# Chapter 2.5: Database Hijacking: The MySQL Workbench Attack

---

## Direct Database Access

Once you have harvested credentials from `config.php`, the web interface becomes irrelevant. Why guess the admin password on the login page when you can just rewrite the database directly?

This phase is called Database Hijacking.

## The Tool of Choice

We do not use strange hacker scripts for this. We use **MySQL Workbench**. This is the standard administrative tool for database management. By using legitimate tools, our traffic looks like administrative maintenance, not an attack.

## The Connection Logic

1. **Host**: The IP address found durng Reconnaissance.
2. **Username**: From the leaked `config.php`.
3. **Password**: From the leaked `config.php`.
4. **Port**: 3306 (Default MySQL port).

## The "Any Host" Vulnerability

By default, MySQL only allows connections from `localhost`. However, Vibe Coders often develop from their home computers. To make this work, they log into their hosting control panel (cPanel or Hostinger) and enable "Remote MySQL."

They are asked to provide an IP address. They do not have a static IP, so they become frustrated.

They enter `%`.

In SQL, `%` allows connections from **any IP address in the world**.

## Execution: The Admin Reset

Once connected via Workbench, we have full read/write access to the database.

1. We open the `users` or `admin` table.
2. We locate the administrator account.
3. We see the password hash. We cannot reverse it easily.
4. We do not need to reverse it. We overwrite it.

We generate an MD5 hash of a known password (e.g., "Marliz123" -> `b78...`). We paste this hash into the database row and click "Apply."

We have not just bypassed the lock. We changed the lock. We can now log into the web application's dashboard with full privileges.

---

"Data does not belong to the one who creates it. It belongs to the one who holds the keys."
Marliz Intel Field Manual
