# Chapter 3.5: Docker as a Security Tool

---

## The Containment Strategy

In a traditional implementation (Hostinger, cPanel, XAMPP), the application runs directly on the operating system. If an attacker achieves Remote Code Execution (RCE), they are running commands on the host server. They can pivot to other websites, access system configurations, and install permanent rootkits.

Docker changes the battlefield. It places the application inside a sealed box.

## Ephemeral Infrastructure

The strongest feature of Docker is that containers are temporary.

If an attacker hacks a WordPress container and installs a backdoor in the `/var/www/html/wp-includes` folder:
1. You identify the breach.
2. You patch the vulnerability in your source code.
3. You restart the container.
4. The container is destroyed and rebuilt from the clean image.
5. The backdoor is gone.

Unless the attacker wrote to a "Persistent Volume" (like `uploads/`), their foothold is wiped clean.

## Network Isolation

Docker allows us to define strict network barriers.

**The Database Pattern:**
In a secure Docker Compose setup, the Database container has **no ports mapped to the host**.

```yaml
services:
  db:
    image: mysql:8.0
    expose:
      - 3306 # Only visible to other containers
    # No "ports" section
  
  app:
    image: php:8.1-apache
    links:
      - db
```

Attackers cannot try to brute-force port 3306 because port 3306 does not exist on the public internet. It only exists inside the private Docker network.

## The Principle of Least Privilege

By default, Docker containers run as `root`. This is dangerous.
You should configure your `Dockerfile` to create a generic user and switch to it.

```dockerfile
RUN groupadd -r appuser && useradd -r -g appuser appuser
USER appuser
```

If the attacker gets a shell, they are `appuser`. They cannot install packages (`apt-get install`), they cannot modify system files, and they cannot break out of the container easily.

---

"If you cannot secure the code, you must secure the box it lives in."
Marliz Intel Field Manual
