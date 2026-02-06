# Chapter 3.3: Environment Isolation: The .env Architecture

---

## Secrets Are Not Code

Hardcoding credentials into source files is the single most common cause of data breaches in Vibe Coded projects. It leads to:
1. Credentials leaking to GitHub.
2. Credentials leaking in stack traces.
3. Inability to rotate passwords without editing code.

To fix this, we implement Environment Isolation.

## The .env File

This is a simple text file that stores configuration variables.

```ini
DB_HOST=127.0.0.1
DB_NAME=production_db
DB_USER=admin
DB_PASS=SuperSecretPassword!
DEBUG_MODE=false
```

This file is **never** committed to version control. It stays on the server.

## The .gitignore

You must immediately create a `.gitignore` file in your repository root and add the following line:

```
.env
```

This ensures that when you push your code to GitHub, the secrets stay behind. You provide a `.env.example` file instead, with placeholders.

## Loading Secrets in PHP

To access these values, we use the `$_ENV` superglobal or `getenv()`.

**Modern Approach (using vlucas/phpdotenv):**
```php
$dotenv = Dotenv\Dotenv::createImmutable(__DIR__);
$dotenv->load();

$host = $_ENV['DB_HOST'];
```

**Legacy Approach (if you cannot use Composer):**
You can parse the file manually, but ensure the parser ignores comments and handles lines correctly.

## Defense in Depth: Placement

Where you put the `.env` file matters.

**Bad:** `/var/www/html/.env`
If the web server is misconfigured, `target.com/.env` will download the secrets.

**Good:** `/var/www/.env`
Place the file **outside** the public document root. The PHP script can read files anywhere on the disk, but the user via the browser is trapped in `/html`.

```php
// config.php
$dotenv = Dotenv\Dotenv::createImmutable('/var/www/'); // Load from one level up
```

This makes the `config.php` file useless to an attacker even if they read it via LFI/Display Source. It contains no secrets, only references to variables they cannot access.

---

"Your code should be public. Your configuration should be private."
Marliz Intel Field Manual
