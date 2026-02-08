# Mission 2.3: Alert Tuning - Making Alerts Actually Useful
**Phase:** 2 (Detection Engineering)
**Objective:** Stop the noise. Catch the real threats.

---

## 1. The Problem: Alert Fatigue

Here is a real scenario: Your SIEM fires 500 alerts per day. You have 2 analysts. Each analyst can investigate maybe 30 alerts properly per shift. That means 440 alerts get ignored or auto-closed.

If one of those 440 alerts was a real attacker, you missed them.

This is why tuning matters. You need to make every alert count.

---

## 2. The Three Tuning Techniques

### Technique A: Whitelisting (Known-Good Exclusions)

Your rule fires for "PowerShell with encoded command." But your IT team runs an automation script every hour that uses encoded PowerShell. That is 24 false positives per day.

**Before Tuning:**
```spl
index=windows EventCode=4688 CommandLine="*-enc*"
```
This fires for everyone.

**After Tuning:**
```spl
index=windows EventCode=4688 CommandLine="*-enc*"
| where User!="SVC_Automation"
| where NOT match(CommandLine, "Known-Script-Hash-123")
```
Now the automation account is excluded.

**Warning:** Never whitelist blindly. If an attacker compromises that automation account, you will miss them. Review whitelists quarterly.

---

### Technique B: Threshold Adjustment

A single failed login is normal. Someone mistyped their password. But 50 failed logins in 5 minutes? That is a brute force attack.

**Before Tuning:**
```spl
index=windows EventCode=4625
```
This fires for every failed login. Useless.

**After Tuning:**
```spl
index=windows EventCode=4625
| stats count by src_ip, user
| where count > 20
```
Now you only see accounts being actively attacked.

---

### Technique C: Enrichment (Add Context)

An alert fires: "User logged in from new country." Is this the CEO traveling for a conference, or is it an attacker in Russia?

**Enriched Alert:**
```spl
index=windows EventCode=4624 LogonType=10
| iplocation src_ip
| lookup user_travel_schedule.csv user AS user OUTPUT travel_country
| where Country!=travel_country
| table _time, user, src_ip, Country, travel_country
```

Now the alert shows: "User logged in from Russia. Their scheduled travel is Kenya." That is clearly an attacker.

---

## 3. The Tuning Lifecycle

Tuning is not a one-time task. It is a cycle.

**Week 1: Deploy**
- Push the new rule to production.
- Set it to "Alert" mode (not auto-block).

**Week 2-4: Monitor**
- Track how many alerts fire.
- Sample 10-20 alerts manually. Are they true positives or false positives?

**Week 5: Analyze**
- Calculate your True Positive Rate: `(Real Attacks) / (Total Alerts)`
- If TPR is below 20%, the rule needs work.

**Week 6: Refine**
- Add whitelists for known-good.
- Adjust thresholds based on baseline.
- Add enrichment for faster triage.

**Repeat every quarter.**

---

## 4. Metrics: How to Know If Your Tuning Is Working

Track these numbers monthly:

| Metric | Target | Why |
| :--- | :--- | :--- |
| **Alerts per Day** | Decreasing (with stable coverage) | Less noise |
| **True Positive Rate** | Above 20% | 1 in 5 alerts should be real |
| **Mean Time to Acknowledge** | Under 15 minutes | Analysts trust the alerts |
| **Alert-to-Incident Ratio** | 5:1 or better | Not every alert is an incident, but many should escalate |

If your TPR is below 10%, your analysts are ignoring alerts. That is dangerous.

---

## 5. Practical: Tuning a Noisy Rule

You have this rule that fires 200 times per day:
```spl
index=sysmon EventCode=1 Image="*powershell.exe*"
```

**Step 1: Sample the Alerts**
Look at 20 random alerts. What are they?
- 15 are scheduled tasks running maintenance scripts
- 3 are IT admins doing their job
- 2 are actually suspicious

**Step 2: Build Exclusions**
```spl
index=sysmon EventCode=1 Image="*powershell.exe*"
| where NOT match(ParentImage, "(?i)taskeng|svchost|mmc")
| where User!="IT_Admins"
```

**Step 3: Measure**
After tuning, you get 20 alerts per day instead of 200. Of those 20, 5 are real. That is a 25% TPR. Good.

---

## 6. The Golden Rule of Tuning

**Never tune away the signal.**

It is tempting to exclude everything that causes noise. But if you whitelist too aggressively, an attacker who learns your exclusions can slip right through.

Always ask: "If an attacker knew about this exclusion, how would they exploit it?"

---

## Professional Narrative
"Implemented continuous alert tuning program, reducing false positive volume by 60% while maintaining detection coverage. Developed threshold-based and enrichment-based rules that improved True Positive Rate from 8% to 32%. Quarterly whitelist reviews ensured exclusions did not create detection blind spots."

**Status:** Mission 2.3 Complete.
