# Chapter 2.1: Reconnaissance: From Domain to IP in 2 Seconds

---

## The Art of Finding

Reconnaissance (Recon) is the most critical phase of any engagement. If you fail here, you will spend hours attacking a firewall instead of the vulnerable application behind it.

In 90% of the cases we see at Marliz Intel, the attacker wins not because they used a complex exploit, but because they found a forgotten subdomain that the admin left unprotected.

## The Basic Ping

The journey usually begins with a simple question. "Is it alive?"

```bash
ping marlizintel.com
```

This tells us two things:
1. The server is up (if it replies).
2. The IP address where the domain points.

However, a smart target will block ICMP packets (ping requests). A lack of reply does not mean the target is down. It just means they aren't talking to strangers.

## Digging Deeper with DNS

When `ping` fails or gives us little metadata, we query the Name Servers.

```bash
nslookup -type=any marlizintel.com
```

We are looking for:
- **A Records**: The direct IP address (IPv4).
- **AAAA Records**: The IPv6 address.
- **MX Records**: The mail server. This is often hosted on the same infrastructure or by a third party (like Google Workspace or ProtonMail).
- **TXT Records**: These can verify ownership for services. Sometimes lazy admins leave sensitive info here.

## The Cloudflare Wall

If the IP address belongs to Cloudflare, Akamai, or AWS CloudFront, you have a problem. You are not seeing the server; you are seeing the shield.

Attacking Cloudflare is a waste of time. You need the **Origin IP**.

### Finding the Origin

1. **DNS History**: Services like SecurityTrails record historical DNS data. The domain might use Cloudflare today, but two months ago, it might have pointed directly to `192.168.x.x`.
2. **Subdomains**: The main site `www.target.com` might be proxied, but the developer portal `dev.target.com` often exposes the direct server IP.

## Passive vs Active

- **Active Recon**: You touch the server. `ping`, `nmap`, directory busting. The target creates logs. You can be detected.
- **Passive Recon**: You query third-party databases (Shodan, Whois, Censys). You never touch the target. You are invisible.

The professional starts with Passive. The amateur starts with Active and gets banned in 5 minutes.

---

"Knowing where to strike is more important than knowing how simple the strike is."
Marliz Intel Field Manual
