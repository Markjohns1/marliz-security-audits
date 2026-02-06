# Chapter 1.3: Case Study: The 1,400-line Monolith

---

## The One-File Framework

In the world of Vibe Coding, file structure is an annoyance. The developer wants to deploy, and managing `includes/` or `classes/` takes time. So they ask the AI for "one file that does everything."

The result is the Monolith.

We routinely encounter single `index.php` files exceeding 1,500 lines. These files contain the database connection, the CCS styling, the Javascript logic, the HTML layout, and the server-side processing, all mixed together in a chaotic soup.

## Analysis of a Monolith

During a recent audit of a logistics platform, we found a file named `dashboard.php`. It was 1,440 lines long.

**Lines 1-50**: CSS Styles (Hardcoded)
**Lines 51-120**: Database Connection and Login Check (Authentication)
**Lines 121-400**: HTML Header and Navigation
**Lines 401-450**: PHP Logic for updating tracking numbers (Business Logic)
**Lines 451-900**: Huge table rendering logic
**Lines 901-950**: **HIDDEN VULNERABILITY** (Unprotected file upload handler)
**Lines 951-1440**: Javascript and Footer

### The "Fold" Problem

The vulnerability on line 901 was invisible. It was buried between a massive HTML table closure and a block of jQuery scripts.

When a developer opens this file, their IDE renders the top 100 lines. They see the CSS. They see the login check. They think the file is safe. They do not scroll down to line 900 where the AI inserted a "temporary" file upload handler that accepts `.php` extensions.

## Why AI Creates Monoliths

AI models operate well within a "context window." When you ask for a complete page, the AI tries to provide a standalone solution. It is easier for the AI to output one continuous block of code than to instruct the user to create four separate files and link them.

The AI is optimizing for "Copy-Paste Convenience," not "Maintainable Architecture."

## Auditing the Monolith

When the Marliz SOC encounters a Monolith, we do not read it top-to-bottom. That leads to fatigue and missed bugs. We use `grep` (or Ctrl+F) to hunt for entry points.

**The Filter List:**
1. `$_POST`: Where is data coming in?
2. `$_GET`: Where are URL parameters handled?
3. `$_FILES`: Are there uploads?
4. `query(`: Where is the database touched?

In the logistics platform case, searching for `$_FILES` took us straight to line 901.

## Remediation Strategy

You cannot secure a Monolith. You must break it.

**Step 1**: Extract the CSS to `style.css`.
**Step 2**: Extract the JS to `script.js`.
**Step 3**: Move the Database connection to `db_connect.php`. (And put it in `.gitignore`)
**Step 4**: Move the header/footer to `includes/`.

Only then can you see the actual logic. Once the noise is removed, the vulnerabilities usually become obvious.

---

"Complexity is the enemy of security."
Marliz Intel Field Manual
