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
