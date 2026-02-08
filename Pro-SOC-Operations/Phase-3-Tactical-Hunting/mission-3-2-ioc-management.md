# Mission 3.2: Indicator of Compromise (IOC) Management
**Phase:** 3 (Tactical Hunting)
**Objective:** Turn threat intelligence into active defense.

---

## 1. What is an IOC and Why Does It Matter

An IOC is a fingerprint of an attacker. When a security researcher discovers a new attack, they publish IOCs so everyone else can check if they were hit too.

**Types of IOCs:**

| Type | What It Is | Example |
| :--- | :--- | :--- |
| **File Hash** | Unique ID of a malicious file | `d41d8cd98f00b204e9800998ecf8427e` |
| **IP Address** | Attacker's command server | `185.220.101.45` |
| **Domain** | Phishing or malware delivery site | `secure-login-update.com` |
| **URL** | Specific malicious resource | `http://evil.com/malware.exe` |
| **Email Address** | Phishing sender | `hr-update@company-secure.net` |
| **Registry Key** | Persistence mechanism | `HKCU\Software\...\Run\backdoor` |
| **User-Agent** | Malware identification string | `Mozilla/5.0 (compatible; malware/1.0)` |

---

## 2. Where to Get IOCs

### Free Sources (Use These Today):
- **AlienVault OTX:** https://otx.alienvault.com - Community-driven, excellent quality
- **Abuse.ch:** https://abuse.ch - Malware, botnets, and command servers
- **VirusTotal:** https://virustotal.com - Hash lookups and relationship graphs
- **MISP Feeds:** Open-source threat intel sharing

### Paid Sources (Enterprise):
- **Recorded Future** - Premium intel with context
- **Mandiant Advantage** - APT tracking
- **CrowdStrike Falcon Intel** - Real-time attacker updates

---

## 3. Hands-On: Creating a SIEM Watchlist

### Step 1: Build Your IOC List
Create a CSV file with your IOCs:
```csv
ioc_type,ioc_value,description,source,date_added
ip,185.220.101.45,Tor Exit Node - Known Malicious,abuse.ch,2026-02-08
ip,45.33.32.156,C2 Server for Emotet,AlienVault,2026-02-08
domain,secure-login-update.com,Phishing Domain,Internal Report,2026-02-08
hash,d41d8cd98f00b204e9800998ecf8427e,Empty File Hash (Test),Manual,2026-02-08
```

### Step 2: Upload to Splunk as a Lookup
```spl
| inputlookup ioc_watchlist.csv
```

### Step 3: Create an Alert That Matches Against the Watchlist
```spl
index=firewall OR index=proxy
| eval ioc_check=coalesce(src_ip, dest_ip, url_domain)
| lookup ioc_watchlist.csv ioc_value AS ioc_check OUTPUT description, source
| where isnotnull(description)
| table _time, src_ip, dest_ip, url_domain, description, source
```

This alert will fire any time your network traffic matches a known bad IOC.

---

## 4. IOC Lifecycle: They Expire

IOCs are not permanent. Attackers change their infrastructure constantly.

**Typical Lifespan:**
- IP Address: 30-90 days (attackers rotate servers)
- Domain: 30-180 days (depends on takedown speed)
- File Hash: Permanent (the file does not change)
- URL: 7-30 days (paths change frequently)

**Your Process:**
1. Add IOC with a date
2. Set expiration (e.g., 90 days for IPs)
3. Review and remove expired IOCs monthly
4. Keep hashes indefinitely

---

## 5. Practical: Checking a Suspicious Hash

You found a suspicious file on a user's machine. How do you check if it is known malware?

### Step 1: Get the Hash
```powershell
Get-FileHash -Algorithm SHA256 "C:\Users\suspicious\file.exe"
```

### Step 2: Check VirusTotal
Go to https://virustotal.com and paste the hash. If it shows detections, you have malware.

### Step 3: Check Your Internal Watchlist
```spl
| inputlookup ioc_watchlist.csv
| where ioc_value="<paste-hash-here>"
```

### Step 4: If It Is New Malware, Add It
```csv
hash,<the-hash>,New malware from incident INC-2026-001,Internal,2026-02-08
```

Now your entire organization is protected from this file.

---

## 6. Automation: MISP to SIEM Pipeline

In a professional environment, you do not manually copy-paste IOCs. You automate.

**MISP (Malware Information Sharing Platform):**
- Aggregates IOCs from multiple feeds
- Deduplicates and enriches them
- Pushes them to your SIEM via API

**Example Flow:**
```
[MISP] --> [Python Script] --> [Splunk API] --> [Watchlist Updated]
```

This means your SIEM is always up-to-date with the latest threat intel.

---

## Professional Narrative
"Managed the IOC lifecycle from acquisition through expiration, integrating threat intelligence feeds from AlienVault OTX and internal incident reports. Developed automated SIEM watchlists that correlate network telemetry against known malicious indicators, enabling real-time detection of compromised infrastructure."

**Status:** Mission 3.2 Complete.
