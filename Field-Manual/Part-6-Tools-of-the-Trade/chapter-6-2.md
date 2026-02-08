# Chapter 6.2: SIEM - The Art of Correlation

---

## The Brain of the SOC

A SIEM (Security Information and Event Management) system is often treated as a compliance dump—a place where logs go to die. This is a waste of a million-dollar tool.

The SIEM is the brain of your security operation. It remembers everything. But like any brain, it is useless if you don't teach it *how to think*.

This chapter assumes you have the logs. Now we will teach you **Detection Engineering**: the art of turning raw data into actionable intelligence.

## The Problem: "Log Fatigue"

A single domain controller generates 50,000 logs an hour. A firewall generates millions.

If your strategy is "Alert me on every failed login," you will fail. You will receive 5,000 emails a day, ignore them all, and miss the real breach. This is **Alert Fatigue**.

**The Solution:** We do not alert on *events*. We alert on *patterns*.

## The Formula for Correlation

Correlation is the logic of combining multiple weak signals to create one high-fidelity alert.

**Logic:**
`Condition A` + `Condition B` + `Time constraints` = **Incident**

### Tier 1: The "Noise" (Do Not Alert)
*   **Event:** `EventID 4625` (Failed Login).
*   **Context:** User creates a typo.
*   **Action:** Log it. Do not page the analyst.

### Tier 2: The Brute Force (Simple Correlation)
*   **Logic:**
    *   `EventID 4625` (Failed Login)
    *   `Count` > 10
    *   `Source_IP` = Same
    *   `Timeframe` = 1 minute
*   **Verdict:** This is a script.
*   **Action:** Low severity ticket.

### Tier 3: The "Impossible Travel" (High Fidelity)
This is where you start nodding your head. This rule catches compromised credentials even when the password is correct.

*   **Logic:**
    *   `Event A`: Successful Login (`User: jdoe`) from `IP: 1.2.3.4 (New York)` at `10:00 AM`.
    *   `Event B`: Successful Login (`User: jdoe`) from `IP: 5.6.7.8 (London)` at `11:00 AM`.
    *   `Constraint`: Time difference < 6 hours (Flight time).
*   **Verdict:** Physics violation. `jdoe` did not fly supersonic. His credentials are stolen and being used by two people.
*   **Action:** **Critical Alert.** Isolate account immediately.

### Tier 4: The "Low & Slow" Exfiltration (The Marliz Standard)
Advanced attackers don't smash windows; they sneak. They use "Low and Slow" techniques to stay under the radar. Here is how we catch them.

*   **The Scenario:** An attacker is stealing your database, but in small chunks to avoid spiking the bandwidth graph.
*   **The Query Logic:**
    1.  **Select**: Firewall Allow Logs.
    2.  **Filter**: `Direction = Outbound` AND `Destination_Port != 80/443`.
    3.  **Aggregation**: Sum(`Bytes_Sent`) per `Source_IP` > 500MB over `24 hours`.
    4.  **Enrichment**: `Destination_IP` is NOT in `Known_Business_Partners`.
    5.  **Context**: Occurs between `02:00` and `05:00` (User's local time).
*   **Verdict:** Why is a laptop sending 500MB of data to an unknown IP in Russia at 3 AM on a non-web port?
*   **Action:** Wake up the CISO.

## The "Trap" Integration

Recall **Chapter 3.6**. We discussed setting a trap for Path Traversal.

Real detection engineering connects the **App** to the **Firewall** via the **SIEM**.

1.  **Trigger:** Web Server logs `GET /../../etc/passwd`.
2.  **SIEM Rule:** `IF URI contains "../" THEN Trigger "Web Attack"`.
3.  **SOAR Response:** `Update Firewall Group -> Block Source_IP for 24h`.

The analyst doesn't even need to wake up. The system defended itself.

---

"A single log is data. Two logs connected by logic is intelligence."
Marliz Intel Field Manual
