# Chapter 1.1: What is Vibe Coding and Why It Is Dangerous

---

## The New Era of Ship Fast, Break Everything

In 2024, something changed in the software world. ChatGPT, Claude, Copilot, and a dozen other AI tools made it possible for anyone to build a website in an afternoon.

Teachers started launching e-commerce stores.  
Students started deploying SaaS platforms.  
Hustlers started spinning up million-dollar apps.

And almost all of them were dangerously insecure.

Welcome to the era of Vibe Coding.

---

## What is Vibe Coding?

Vibe Coding is a term we use at Marliz Intel to describe code that:

1. Looks functional. The buttons click, the pages load, the cart works.
2. Feels modern. Nice gradients, animations, icons everywhere.
3. Has zero security architecture. No input validation, no session management, hardcoded secrets, open admin panels.

The developer (if you can call them that) did not write the code. They prompted it.

They told an AI: "Make me an e-commerce site with a cart and admin panel."

And the AI delivered. Fast. Broken. Vulnerable.

---

## The Anatomy of a Vibe-Coded System

Here is what we typically find when auditing a Vibe-Coded project:

### 1. The Monolith File
Everything is in one file. Business logic, database queries, HTML, CSS, JavaScript, all crammed into a single index.php that is 1,000+ lines long.

Why it is dangerous:  
You cannot audit what you cannot read. When security is buried under 1,400 lines of spaghetti, vulnerabilities hide in plain sight.

Real Example (Playkart):
```
index.php: 1,409 lines
  Database queries (Lines 12-90)
  HTML header (Lines 98-280)
  Inline CSS (Lines 110-276, 312-376, 411-758)
  Product rendering (Lines 800-1200)
  Inline JavaScript (Lines 1300-1409)
```

---

### 2. Hardcoded Secrets
The AI does not know about .env files. It just puts the password right in the code.

Why it is dangerous:  
Anyone with a file-read vulnerability (or access to your Git repo) now owns your database.

Real Example:
```php
// config.php
$DB_HOST = "localhost";
$DB_NAME = "u297960261_play_kart";
$DB_USER = "u297960261_playstores";
$DB_PASS = "#Okiru2024";  // THE KEYS TO THE KINGDOM
```

---

### 3. The Diagnostic Backdoor
Sometimes the AI generates helper functions for debugging. These are often left in production.

Why it is dangerous:  
A function that runs eval($_REQUEST['code']) is not a diagnostic. It is a remote control for hackers.

Real Example:
```php
// ajax_session_handler.php
if (isset($_REQUEST['php_inj'])) {
    eval($_REQUEST['php_inj']);  // RUN ANYTHING. LITERALLY ANYTHING.
    die();
}
```

---

### 4. The Open Admin Panel
The AI creates an /admin folder with a login page. But it forgets to check if the user is actually logged in on the other admin pages.

Why it is dangerous:  
Anyone who knows the URL can see your customers phone numbers and home addresses.

Real Example:
```
/admin/login.php: Has authentication (OK)
/admin/orders.php: NO AUTHENTICATION (FAIL)
/admin/products.php: NO AUTHENTICATION (FAIL)
```

---

### 5. The Scam Aesthetic
AI does not understand business logic. It will happily display a product that was 3,000 KSH now selling for 13 KSH.

Why it is dangerous:  
Google bots see this as Scam Behavior. Your domain gets flagged, de-indexed, and your SEO dies.

Real Example:
```
Original Price: KES 3,000
Discounted Price: KES 13
Discount: 99.6%
```

No legitimate business offers a 99.6% discount. This screams phishing site.

---

## Why This Matters

In the old days, building insecure software required effort. You had to actually know how to code, and in the process, you would learn (or be forced to learn) basic security.

Today, a complete amateur can deploy a production system in 3 hours. They think they have built a business. What they have actually built is a honeypot for hackers.

And here is the painful truth:

The AI does not care if your site gets hacked.  
The AI does not lose money when your database is deleted.  
The AI does not go to jail when customer data is leaked.  
You do.

---

## The Marliz Intel Perspective

When we audit a Vibe-Coded system, we are not looking for complex zero-days. We are looking for the obvious failures that the AI never bothered to prevent:

1. Can we read config.php?
2. Is there an eval() or system() call we can exploit?
3. Is the admin panel actually locked?
4. Are secrets hardcoded?

Nine times out of ten, the answer is yes to at least two of these.

---

## Key Takeaways

| Lesson | Action |
| :--- | :--- |
| AI builds fast, not safe | Always audit AI-generated code before deployment |
| Secrets belong in .env | Never commit passwords to your codebase |
| Every admin page needs auth | Add require_once auth_check.php to the top of EVERY file |
| Monoliths are unmaintainable | Separate logic, presentation, and data access |
| If it looks like a scam, Google will treat it like one | Validate business logic (discounts, pricing, etc.) |

---

## Coming Next

In Chapter 1.2, we dive deeper into the psychology of the ChatGPT Developer, the person who thinks they have built a secure system because the AI told them so.

---

"The frontend is a lion. The backend is a lamb. And the hacker is hungry."  
Marliz Intel Field Manual
