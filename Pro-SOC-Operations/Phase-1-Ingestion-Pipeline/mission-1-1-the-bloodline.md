# Mission 1.1: The Bloodline - Data Ingestion & Normalization
**Phase:** 1 (Ingestion Pipeline)
**Objective:** Capture and structure raw telemetry for cross-platform correlation.

---

## 1. The Core Problem You Need to Solve

Imagine this scenario: Your organization has 500 Windows servers, 100 Linux servers, 50 firewalls, and 20 web servers. An attacker compromises one Linux server, moves to a Windows server, and exfiltrates data through the firewall.

To detect this, you need to correlate events across all three platforms. But here is the problem:
- The Linux server logs: `Feb 8 02:00:00 webserver sshd[12345]: Failed password for root from 192.168.1.100`
- The Windows server logs: `EventID=4625, TargetUserName=Administrator, IpAddress=192.168.1.100`
- The firewall logs: `src=192.168.1.100 dst=203.0.113.50 action=allow bytes=50000000`

Three different formats. Three different field names. If you search for "192.168.1.100" you might find it, but if you search for "failed login from this IP AND large outbound transfer" you need normalization.

---

## 2. The Solution: Normalization

Normalization means mapping every log source to a common schema. The two major standards are:

**Elastic Common Schema (ECS):**
- `source.ip` = The IP that initiated the connection
- `user.name` = The username involved
- `event.outcome` = success or failure

**Splunk Common Information Model (CIM):**
- `src_ip` = Source IP
- `user` = Username
- `action` = What happened

After normalization, all three logs above would have:
- `source.ip: 192.168.1.100`
- `event.category: authentication` (for the login attempts)
- `event.category: network` (for the firewall)

Now you can write ONE query that searches across all sources.

---

## 3. The Infrastructure: How Logs Actually Flow

### Real-World Architecture:

```
[Endpoints] --> [Shipper/Agent] --> [Aggregator] --> [SIEM]
     |               |                    |              |
  Windows        Winlogbeat           Logstash      Elasticsearch
  Linux          Filebeat             Kafka         Splunk Indexer
  Firewall       Syslog-ng            Graylog       Sentinel
```

### Why the Aggregator Matters:
If your SIEM goes down for maintenance, what happens to your logs? Without an aggregator, they are lost forever. With Kafka or Logstash as a buffer, logs are queued and delivered when the SIEM comes back online.

---

## 4. Hands-On: Installing a Log Shipper (Winlogbeat)

This is how you actually get Windows event logs into a SIEM.

### Step 1: Download Winlogbeat
```powershell
Invoke-WebRequest -Uri "https://artifacts.elastic.co/downloads/beats/winlogbeat/winlogbeat-8.x.x-windows-x86_64.zip" -OutFile winlogbeat.zip
Expand-Archive winlogbeat.zip -DestinationPath C:\Program Files\Winlogbeat
```

### Step 2: Configure the Output (winlogbeat.yml)
```yaml
winlogbeat.event_logs:
  - name: Security
    event_id: 4624, 4625, 4688, 4697
  - name: Microsoft-Windows-Sysmon/Operational

output.elasticsearch:
  hosts: ["your-siem.example.com:9200"]
  username: "winlogbeat"
  password: "your-password"
```

### Step 3: Install and Start the Service
```powershell
.\install-service-winlogbeat.ps1
Start-Service winlogbeat
```

Now your Windows security events are flowing to the SIEM in real-time.

---

## 5. The Critical Rule: Time Synchronization

Every forensic investigation depends on accurate timestamps. If Server A says the attack happened at 10:00:00 and Server B says it happened at 10:00:45, your timeline is ruined.

### The Fix: NTP Configuration (Windows)
```powershell
w32tm /config /manualpeerlist:"time.google.com" /syncfromflags:manual /reliable:YES /update
Restart-Service w32time
w32tm /resync
```

### The Fix: NTP Configuration (Linux)
```bash
sudo timedatectl set-ntp true
sudo systemctl restart systemd-timesyncd
```

---

## 6. Practical Lab: Parsing a Raw Log

Take this raw Apache access log:
```
192.168.1.50 - - [08/Feb/2026:14:30:00 +0000] "GET /admin/config.php HTTP/1.1" 200 1234
```

### Grok Pattern (for Logstash):
```
%{IP:source.ip} - - \[%{HTTPDATE:timestamp}\] "%{WORD:http.method} %{URIPATH:url.path} HTTP/%{NUMBER}" %{NUMBER:http.status} %{NUMBER:http.bytes}
```

### Result (Normalized JSON):
```json
{
  "source.ip": "192.168.1.50",
  "timestamp": "08/Feb/2026:14:30:00 +0000",
  "http.method": "GET",
  "url.path": "/admin/config.php",
  "http.status": 200,
  "http.bytes": 1234
}
```

Now this log can be correlated with any other source that uses `source.ip`.

---

## Professional Narrative
"Engineered enterprise log ingestion pipelines with normalization to Elastic Common Schema. Deployed Winlogbeat agents across Windows infrastructure for real-time Security Event forwarding. Implemented Grok parsing patterns to transform unstructured web logs into searchable, correlated data streams."

**Status:** Mission 1.1 Complete.
