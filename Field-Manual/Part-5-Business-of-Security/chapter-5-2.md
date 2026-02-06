# Chapter 5.2: Finding Targets: The Background Radiation of the Internet

---

## Targeted vs Opportunistic

There are two ways to find work.

1.  **Targeted**: You pick a specific company (e.g., "Safaricom") and try to hack them.
    - **Risk**: High. They have blue teams watching.
    - **Difficulty**: Hard.
2.  **Opportunistic**: You look for *any* vulnerable server in Kenya and then find out who owns it.
    - **Risk**: Low. You are helping people who don't even know they are bleeding.
    - **Difficulty**: Easy.

Marliz Intel focuses on Opportunistic Discovery.

## Shodan: The Search Engine for Hackers

Google crawls text. Shodan crawls ports.

We use Shodan to find servers that are misconfigured by default.

**The Query:**
`country:"KE" port:"3306" product:"MySQL"`

This asks Shodan: "Show me every computer in Kenya that has its database port open to the public."

**The Result:**
You will see IP addresses. You will not see domain names immediately. You will see:
`197.232.xx.xx`

## Google Dorks

We use advanced Google search operators ("Dorks") to find Vibe Coded sites.

**Query 1 (The Error Log):**
`site:.ke "Warning: include()"`
This finds Kenyan sites that are currently crashing and displaying PHP errors to the world.

**Query 2 (The Exposed Config):**
`site:.ke intitle:"index of" "config.php"`
This finds servers with Directory Listing enabled that are exposing their configuration files.

**Query 3 (The Default Dashboard):**
`site:.ke "Welcome to Laravel"`
This finds sites that were deployed but never finished.

## From IP to Owner

Once you have a vulnerable IP or URL, you need to find the human to contact.

1.  **Whois Lookup**: `whois marlizintel.com`
    - Look for "Registrant Phone" or "Admin Email."
2.  **The Site Footer**: Look for "Designed by [Agency Name]." The Agency is often the better contact than the client, because the Agency knows they made a mistake.
3.  **M-Pesa Paybill**: If it's a shop, try to buy something. The M-Pesa prompt will give you the registered business name.

---

"We do not hunt the prey. We listen for the wounded."
Marliz Intel Field Manual
