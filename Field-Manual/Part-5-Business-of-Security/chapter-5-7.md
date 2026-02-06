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
