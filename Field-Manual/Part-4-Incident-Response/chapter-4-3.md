# Chapter 4.3: Credential Rotation: Assuming Total Compromise

---

## The Poisoned Well

When an attacker gains read access to your file system (via LFI or Shell), you must assume they have read *everything*. Including the `.env` file you thought was safe.

Changing the database password is not enough.

## The Kill List

You must rotate every secret that was resident on the server.

1.  **Database User Passwords**: The `DB_PASS` in your config.
2.  **API Keys**: AWS Access Keys, Stripe Secrets, Twilio Tokens. Even if you think the attacker didn't see them, revoke them.
3.  **SSH Keys**: If the attacker read `~/.ssh/id_rsa`, they can impersonate the server to *other* servers. Remove the public key from all `authorized_keys` files on your network.
4.  **Application Secrets**: The `APP_KEY` used to sign session cookies (Laravel/Django/Rails). If you don't change this, the attacker can forge session cookies and log in as admin forever.
5.  **SMTP Passwords**: Your email sending credentials.

## Kick The Users

Changing the passwords prevents *future* logins. It does not stop *current* ones.

You must trigger a global logout.
1. Truncate the `sessions` table in the database.
2. Delete the contents of `/var/lib/php/sessions` (for PHP file-based sessions).
3. If using JWTs (JSON Web Tokens), you must rotate the signing key (see point #4 above). This invalidates all existing tokens immediately.

## The Admin Reset

Force every administrator to change their password.
An attacker might have hashed a known password into the database (see Chapter 2.5). Validating the old password is useless. Force a reset via email.

---

"Regret is cheaper than a second breach."
Marliz Intel Field Manual
