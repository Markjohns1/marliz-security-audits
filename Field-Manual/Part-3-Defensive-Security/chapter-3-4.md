# Chapter 3.4: Session Hardening: Locking Down /admin

---

## The Forgotten Gatekeeper

It is common to find a secure login page (`login.php`) protecting an insecure dashboard. The developer checks the password on the login screen, sets a cookie, and redirects the user. But on `dashboard.php`, they forget to check if that cookie is valid.

## The Include Pattern

Do not write authentication logic in every file. You will forget one. Write it once.

**File: `includes/auth_check.php`**
```php
session_start();

if (!isset($_SESSION['user_id']) || $_SESSION['is_admin'] !== true) {
    header("Location: /login.php");
    exit(); // Crucial: Stop script execution immediately
}
```

**File: `admin/dashboard.php`**
```php
require_once '../includes/auth_check.php';

// The rest of the page...
```

The strict use of `require_once` ensures that if the check fails or the file is missing, the script dies instantly.

## Killing Session Fixation

Session Fixation is an attack where the hacker tricks the victim into using a session ID known to the hacker.

**The Fix:**
Whenever a user elevates privileges (e.g., logging in), you must issue a fresh ID.

```php
// Inside login.php, after password verification:
session_regenerate_id(true); // true deletes the old session file
$_SESSION['user_id'] = $user['id'];
```

## Cookie Hardening

The session ID is stored in a cookie. If that cookie is stolen (via XSS), the account is compromised. We can mitigate this by setting flags on the cookie.

1. **HttpOnly**: The cookie cannot be accessed by JavaScript. (Stops XSS theft).
2. **Secure**: The cookie is only sent over HTTPS. (Stops network sniffing).
3. **SameSite**: The cookie is not sent on cross-site requests. (Stops CSRF).

**Implementation:**
```php
session_set_cookie_params([
    'lifetime' => 0,
    'path' => '/',
    'domain' => 'marlizintel.com',
    'secure' => true,
    'httponly' => true,
    'samesite' => 'Strict'
]);
session_start();
```

## The Timeout

Sessions should not last forever. Implement an inactivity timer.

```php
if (isset($_SESSION['last_activity']) && (time() - $_SESSION['last_activity'] > 1800)) {
    // Last request was more than 30 minutes ago
    session_unset();
    session_destroy();
}
$_SESSION['last_activity'] = time();
```

---

"A session is a temporary privilege. Do not make it permanent."
Marliz Intel Field Manual
