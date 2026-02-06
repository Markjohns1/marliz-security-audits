# Chapter 4.1: The OODA Loop: Observe, Orient, Decide, Act

---

## Combat Theory in Cybersecurity

When a server is under attack, panic is the enemy. You see CPU usage spike to 100%. You see strange files appearing in `/tmp`. The instinct is to just pull the power plug.

That is often a mistake.

At Marliz Intel, we use the OODA Loop. Developed by military strategist John Boyd, it is the cycle of decision-making in chaotic environments.

## 1. Observe

Stop. Look. Do not touch anything yet.
Gather the raw data.
- **System Load**: `htop`
- **Network Connections**: `netstat -antp`
- **Active Processes**: `ps auxf`
- **Logs**: `tail -f /var/log/syslog`

**Goal**: Identify the anomaly. "Why is the `www-data` user running a process called `miner`?"

## 2. Orient

Contextualize the observation. Use your knowledge to understand the threat.
- Is this a script kiddie scanning for open ports? (Low Threat)
- Is this a crypto-miner stealing CPU cycles? (Medium Threat)
- Is this a data exfiltration script sending database dumps to Russia? (High Threat)

**Goal**: Determine the severity and the vector. "They got in through an insecure file upload on the contact page."

## 3. Decide

Choose a course of action. You have options:
- **Containment**: Block the IP. Kill the process.
- **Isolation**: Disconnect the server from the network to preserve evidence.
- **Eradication**: Wipe the server and rebuild from a clean image.
- **Monitoring**: Watch them for 10 more minutes to learn their techniques (Risky, but valuable).

**Goal**: Select the tactic that minimizes damage and maximizes recovery.

## 4. Act

Execute the decision.
- `kill -9 [PID]`
- `iptables -A INPUT -s [ATTACKER_IP] -j DROP`
- `docker-compose down`

## The Cycle

Once you Act, the situation changes. The attacker might change IPs. The malware might respawn. You must immediately loop back to **Observe**. Did the `kill` command work? Is the CPU load down?

Start the loop again. Faster.

---

"He who processes information faster than his opponent wins the battle."
Marliz Intel Field Manual
