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
