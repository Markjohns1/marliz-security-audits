# Chapter 2.2: Directory Enumeration: Finding the Hidden Doors

---

## The Unlisted Map

A web browser only shows you what the developer wants you to see. But the web server contains files that were never meant to be public. Backups, old versions, configuration files, and "hidden" admin panels.

Directory Enumeration (or "Dirbusting") is the process of guessing these filenames.

## The Logic of Brute Force

We do not randomly guess characters. We use "Wordlists". These are massive text files containing the most common directory names found on the internet.

- `admin`
- `login`
- `backup`
- `test`
- `config`
- `db`

Tools like **Gobuster** or **Dirb** take this list and send a request for each one.

`GET /admin` -> 404 (Not Found)
`GET /login` -> 200 (Found!)

## Using Gobuster

The standard command for directory enumeration:

```bash
gobuster dir -u https://marlizintel.com -w /usr/share/wordlists/common.txt
```

**Key Flags:**
- `-u`: The target URL.
- `-w`: The wordlist to use.
- `-x`: Extensions to search for (e.g., `php,html,zip,bak`).

Addition of the `-x` flag is crucial. Finding `config` (404) is useless. Finding `config.php.bak` (200) gives you the database passwords.

## Interpreting Status Codes

The server response tells you the state of the door:

1. **200 OK**: The door is open. The file exists and you can read it.
2. **301 Redirect**: You are being moved. Usually from `/admin` to `/admin/login.php`. This confirms the directory exists.
3. **403 Forbidden**: The door is locked. The server acknowledges the file exists but refuses to show it. This is often *more* interesting than a 200, because it implies there is something worth hiding.
4. **404 Not Found**: The door does not exist. Move on.

## The ".git" Catastrophe

One of the most devastating findings is a **200 OK** on the `/.git/` directory.

If a developer deploys their entire git repository to the live server, you can download the entire version history of the project. This includes every previous version of the code, and often, secrets that were "deleted" in later commits.

Tools like `git-dumper` can reconstruct the entire source code on your local machine.

---

"The most dangerous file on a server is often the one the developer forgot to delete."
Marliz Intel Field Manual
