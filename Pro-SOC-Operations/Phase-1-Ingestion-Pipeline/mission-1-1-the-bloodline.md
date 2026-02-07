# Mission 1.1: The Bloodline - Data Ingestion & Normalization
**Phase:** 1 (Ingestion Pipeline)
**Objective:** Capture and structure raw telemetry for cross-platform correlation.

---

## 1. The Core Challenge: Event Heterogeneity
Modern environments consist of hundreds of unique device types. A Cisco Firewall, a Windows Domain Controller, and a Linux Web Server all output data in different formats. Direct ingestion of these formats results in a non-searchable data set.

### Normalization Standards
At Marliz Intel, we enforce schema normalization. Every log source must be mapped to a common field set (e.g., Elastic Common Schema or Splunk CIM).
*   **Target Field:** `src_ip` must represent "Source IP" across all platforms.

---

## 2. Infrastructure Tiers: The Log Flow
For professional environments, the ingestion pipeline follows a four-tier architecture:

### Tier 1: The Source
The endpoint or service generating the event (e.g., Windows Event Log, Linux Syslog).

### Tier 2: The Shipper
Lightweight agents installed on the source to forward events (e.g., Winlogbeat, Filebeat, Splunk Universal Forwarder). Agents are preferred over agentless methods as they offer local caching during network outages.

### Tier 3: The Aggregator & Buffer
A centralized server that receives logs from all shippers. It performs initial parsing and acts as a buffer (using tools like Logstash, Graylog, or Apache Kafka). This prevents data loss if the SIEM is unreachable.

### Tier 4: The SIEM (Indexer)
The final destination where transformed data is indexed, stored, and made available for searching and alerting.

---

## 3. Tactical Priority: Temporal Integrity
In a SOC environment, time is the primary pivot point. Clock drift across servers makes incident reconstruction impossible. All infrastructure must be synchronized via a centralized Network Time Protocol (NTP) hierarchy.

---

## 4. Practical: Data Extraction (Grok/Regex)
To normalize data, you must extract key-value pairs from raw strings.

**Example Case: Web Server Access Log**
*   **Raw Log:** `192.168.1.10 - - [08/Feb/2026:01:00:00 +0000] "GET /admin HTTP/1.1" 403 500`
*   **Extracted Fields:**
    *   `src_ip`: 192.168.1.10
    *   `timestamp`: 08/Feb/2026:01:00:00
    *   `request_path`: /admin
    *   `http_status`: 403

---

## 📑 Professional Narrative
"Engineered high-availability ingestion pipelines utilizing a tiered architecture to ensure telemetry persistence. Implemented comprehensive log normalization strategies to facilitate multi-vector correlation and reduce mean-time-to-detection (MTTD)."

**Status:** Mission 1.1 Complete.
