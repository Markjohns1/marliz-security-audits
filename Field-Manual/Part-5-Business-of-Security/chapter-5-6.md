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
