# Chapter 1.2: The ChatGPT Developer: Fast but Fatal

---

## The Rise of the Prompter

The traditional software engineer spends years learning syntax, memory management, and system architecture. The ChatGPT Developer spends an afternoon learning how to ask for a "modern e-commerce site using Bootstrap."

They are not builders. They are assemblers.

This distinction is critical for the security analyst. The builder understands the foundation. The assembler only cares about the facade. When we audit systems built by assemblers, we find a distinct lack of structural integrity.

## The Loop: Prompt, Paste, Pray

The workflow of the ChatGPT Developer is a closed loop of ignorance.

1. **Prompt**: "Write a PHP script to handle user login."
2. **Paste**: The code is dumped into `login.php`.
3. **Run**: It generates an error.
4. **Reprompt**: The error is pasted back into the AI. "Fix this."
5. **Paste**: The "fixed" code replaces the old one.
6. **Success**: The error is gone.

At no point in this cycle does the developer understand *why* the error occurred or *how* it was fixed. This is dangerous. The "fix" often involves suppressing errors, bypassing checks, or removing the security constraint that caused the friction.

## The Blind Spot

We observed this behavior in the Playkart audit. The developer likely encountered a "Foreign Key Constraint" error when trying to delete a user.

A real developer checks the database schema.
The ChatGPT Developer asks the AI to "force delete user."
The AI obliges: `SET FOREIGN_KEY_CHECKS=0; DELETE FROM users...`

Just like that, data integrity is compromised because the developer prioritized the removal of the error message over the health of the system.

## The Illusion of Competence

These developers move fast. They show progress updates daily. The UI looks polished. To a client or employer (the "Mwalimu"), they appear highly competent.

**The Reality Check:**
They are borrowing technical debt at an interest rate they cannot afford.
They are deploying code they cannot read.
They are unable to patch vulnerabilities because they do not know where the code handles input.

## Profile of a Target

When doing reconnaissance, how do we identify a ChatGPT Developer?

1. **Inconsistent Comment Styles**: One file has JSDoc comments, the next has Python-style docstrings in PHP. The AI fluctuates based on training data.
2. **Over-commenting**: "Starts the session" above `session_start()`. Detailed explanations of obvious standard library functions.
3. **Variable Naming Chaos**: A mix of `camelCase` and `snake_case` in the same function.
4. **Zombie Code**: Large commented-out blocks that look like alternative solutions the AI suggested but were abandoned.

## Conclusion

The ChatGPT Developer is not malicious. They are negligent. They are operating heavy machinery without a license. In the Marliz SOC, we treat their code as hostile territory not because of intent, but because of chaos.

They build the attack surface for us.

---

"Speed is irrelevant if you are running in the wrong direction."
Marliz Intel Field Manual
