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
