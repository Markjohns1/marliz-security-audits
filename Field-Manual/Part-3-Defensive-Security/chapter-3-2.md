# Chapter 3.2: Input Validation: Killing ../ Before It Kills You

---

## Trust No One

The cardinal sin of Vibe Coding is trusting the `$_GET` and `$_POST` superglobals. The developer assumes that because the frontend form only allows numbers, the backend receives only numbers.

This is false. We play with `curl`. We send whatever we want.

## White-List vs Black-List

There are two ways to filter input.

1.  **Black-Listing**: "Block everything that looks like a hack."
    - We try to block `../`, `<script>`, `UNION`.
    - This fails because attackers are creative. `....//` gets past `../`.
2.  **White-Listing**: "Allow only what is known to be good."
    - We allow only `[a-z0-9]`.
    - If the input contains anything else, we reject it.

White-listing is the only secure method.

## Practical Defenses

### 1. Defeating Path Traversal
To stop LFI, we must ensure filenames do not contain directory separators.

**The Fix: `basename()`**
This PHP function strips all directory information from a path.

```php
$file = $_GET['file']; // "../../../etc/passwd"
$clean = basename($file); // "passwd"
include($clean); // Fails safely
```

### 2. Defeating Integer Injection
If a parameter is supposed to be an ID, force it to be an integer.

**The Fix: Type Casting**

```php
$id = (int)$_GET['id'];
// If input is "1 UNION SELECT...", $id becomes 1.
// If input is "hello", $id becomes 0.
```

The injection is neutralized before it even reaches the database.

### 3. Defeating XSS output
When we print user data back to the screen, we must neutralize HTML tags.

**The Fix: `htmlspecialchars()`**

```php
echo htmlspecialchars($user_comment, ENT_QUOTES, 'UTF-8');
```

This turns `<script>` into `&lt;script&gt;`. The browser displays the text, but does not execute the code.

## The Validation Gate

Perform all validation at the very top of your file. If the input is invalid, `die()` immediately. Do not execute a single line of business logic until the data is proven clean.

---

"Sanitize your inputs, or your database will be sanitized for you."
Marliz Intel Field Manual
