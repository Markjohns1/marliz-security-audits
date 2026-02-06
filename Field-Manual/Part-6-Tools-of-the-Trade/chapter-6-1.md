# Chapter 6.1: Burp Suite Essentials

---

## The Surgeon's Scalpel

If you are attacking a web application using only a browser, you are fighting with one hand tied behind your back.
Browsers hide things. They render HTML. They execute JavaScript. They manage cookies.

To see the truth, you need **Burp Suite**.

Burp Suite is a proxy. It sits between your browser and the server. Every request hangs in the air, waiting for your permission to proceed. You can edit the data *after* it leaves the browser but *before* it hits the server.

## Installation

1. Download Burp Suite Community Edition (Free).
2. Configure your browser (Firefox is best) to proxy traffic to `127.0.0.1:8080`.
3. Install the Burp CA Certificate so you can intercept HTTPS traffic.

## Key Modules

### 1. Proxy (Intercept)
This is the core.
**Scenario**: The website has a dropdown menu for "User Role" that is disabled.
**Attack**:
- Submit the form.
- Catch the request in Burp.
- See `role=user`.
- Change it to `role=admin`.
- Forward the request.
- The server receives `role=admin`. The frontend validation is bypassed.

### 2. Repeater
This is for manual testing.
**Scenario**: You suspect SQL Injection on a search bar.
**Action**:
- Send the search request to Repeater.
- Change `search=shoes` to `search=shoes'`.
- Click Send.
- Check response.
- Change to `search=shoes'--`.
- Click Send.
You can fire 100 variations in a minute without reloading the page.

### 3. Intruder (Rate Limited in Free Version)
This is for brute force.
**Scenario**: You want to guess the admin password.
**Action**:
- send login request to Intruder.
- Highlight the password field.
- Load a wordlist.
- Burp sends 1000 requests, swapping the password each time.

## The Marliz Workflow

1. Open Browser.
2. Turn on Burp Intercept.
3. Click every button on the target site.
4. "Map the Application" in Burp's history tab.
5. Send interesting requests to Repeater.
6. Break things.

---

"The browser lies. The proxy tells the truth."
Marliz Intel Field Manual
