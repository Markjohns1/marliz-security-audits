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
