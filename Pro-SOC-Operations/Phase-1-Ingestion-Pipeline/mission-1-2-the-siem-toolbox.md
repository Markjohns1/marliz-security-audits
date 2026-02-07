# Mission 1.2: SIEM Selection and Architectural Integration
**Phase:** 1 (Ingestion Pipeline)
**Objective:** Evaluating SIEM platforms and optimizing collection methodologies.

---

## 1. Defining the SIEM (Correlation vs. Storage)
A SIEM (Security Information and Event Management) platform is a correlation engine. Its primary value is not in storing logs, but in identifying relationships between unrelated events to reveal an attack chain.

---

## 2. Competitive Analysis: The Major Stacks

### A. The ELK Stack (Open Source Framework)
*   **Architecture:** Elasticsearch, Logstash, Kibana.
*   **Application:** Best for high-volume logs (e.g., DNS, Web Traffic). It requires a high level of engineering skill to maintain but offers unlimited customization without license fees.

### B. Splunk (Enterprise Indexer)
*   **Application:** The industry standard for searching unindexed, schema-less data. Known for its powerful "Search Processing Language" (SPL).
*   **Limitation:** High licensing costs based on ingestion volume (GB/day).

### C. Microsoft Sentinel (Cloud-Native SIEM)
*   **Application:** Ideal for organizations with a heavy Azure/M365 footprint. It offers rapid deployment and scales automatically without the need for infrastructure management.

---

## 3. Data Collection Methodologies

### A. Agent-Based (Push)
A specialized service (Agent) resides on the endpoint and pushes logs to the SIEM.
*   **Risk Mitigation:** Agents handle network congestion and local caching, ensuring no data loss during "Sprints" (bursts of activity during an attack).

### B. Agentless (Pull)
The SIEM server connects to the target (via WMI, SSH, or API) to fetch data.
*   **Use Case:** Good for environments where installing 3rd-party software is prohibited (e.g., medical devices or legacy systems).

---

## 4. The Marliz Selection Matrix
When advising clients on SIEM selection, the following criteria are weighted:

| Factor | ELK Stack | Splunk | MS Sentinel |
| :--- | :--- | :--- | :--- |
| **Operational Cost** | High (Personnel) | High (License) | Variable (Usage) |
| **Setup Time** | Extensive | Moderate | Rapid |
| **Scalability** | Manual | Cluster-based | Auto-scale |
| **Analytics** | Custom | Native/Extensive | Native/AI-driven |

---

## 📑 Professional Narrative
"Conducted comparative analysis of SIEM architectures to determine optimal deployment strategy for diverse client environments. Developed cost-to-performance models for log ingestion, resulting in a 20% reduction in licensing overhead while maintaining 100% telemetry coverage."

**Status:** Mission 1.2 Complete.
