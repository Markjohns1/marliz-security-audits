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
