# Security Research Post Guide

Quick guide for writing security research posts on your blog (OSCP, OSWA, CTF writeups, penetration testing reports).

---

## Quick Start

### 1. Create a New Post

**Option A: Using Python Script (Recommended)**
```bash
# Security Lab
python3 new-security-post.py "HTB Lame" "easy" "security"

# Web Security Challenge
python3 new-security-post.py "WebGoat SQL Injection" "medium" "web-security"

# CTF Challenge
python3 new-security-post.py "PicoCTF Web-100" "easy" "ctf"
```

**Option B: Manual Copy**
```bash
# Copy template
cp SECURITY_RESEARCH_TEMPLATE.md _posts/2024-03-16-oscp-lab-name.markdown

# Edit in your editor
code _posts/2024-03-16-oscp-lab-name.markdown
```

### 2. Update Post Metadata (Frontmatter)

```yaml
---
layout: post
title: "HTB Lame - SQL Injection RCE"
subtitle: "Easy Difficulty"
date: 2024-03-16
author: "Your Name"
categories: [security, penetration-testing]
tags: [sql-injection, rce, linux]
img: "/assets/img/posts/2024-03-16/screenshot.png"
image_viewer_on: true
image_lazy_loader_on: true
---
```

**Key Fields:**
- `title` - Challenge/Lab name + main vulnerability
- `subtitle` - Difficulty level (keep brief)
- `categories` - [security, penetration-testing, web-security, etc.]
- `tags` - Vulnerability types, tools, techniques used
- `img` - Thumbnail (place image in `assets/img/posts/YYYY-MM-DD/`)

### 3. Write Your Content

Start filling in sections from the template:
- Overview
- Reconnaissance & Enumeration
- Vulnerability Analysis
- Exploitation
- Post-Exploitation
- Lessons Learned
- References

### 4. Test Locally

```bash
bundle exec jekyll serve
# Visit http://localhost:4000 and find your post
```

### 5. Publish

```bash
git add _posts/2024-03-16-lab-name.markdown
git commit -m "Add OSCP writeup: Lab Name"
git push origin main
# Auto-deploys to Netlify
```

---

## Section Breakdown

### Overview
- **What it is**: 1-2 sentence summary + key details
- **Keep it brief**: Reader should know if this is relevant to them
- **Include**: Difficulty, platform, challenge type

### Reconnaissance & Enumeration
- **Show your methodology**: nmap, service enumeration, web crawling
- **Include output**: Show what you found (sanitize sensitive data)
- **Organize by service**: Group findings by port/service discovered
- **Use code blocks**: Make output readable

### Vulnerability Analysis
- **Explain the "why"**: Why the vulnerability exists
- **Technical details**: How the vulnerability works
- **CVSS/CVE info**: Reference official CVE if available
- **Proof of concept**: Show the vulnerability in action

### Exploitation
- **Step-by-step**: Number each exploitation step
- **Show commands**: Full command examples with context
- **Include output**: Show what success looks like
- **Tools needed**: List of tools and versions used
- **Custom scripts**: Include full code in appendix

### Post-Exploitation
- **Access level**: What user/permissions you achieved
- **Privilege escalation**: How you escalated (if applicable)
- **Data collected**: What you found on the system
- **Flag/Goal**: How you obtained the final flag

### Lessons Learned
- **Key techniques**: Methods that were effective
- **Challenges**: What was tricky and how you solved it
- **Takeaways**: Important security concepts learned
- **Time tracking**: How long each phase took

### References
- **CVE/Advisories**: Security bulletins
- **Tools**: Links to tool documentation
- **Similar writeups**: Other resources on the topic
- **Learning resources**: Books, courses, videos

---

## Best Practices

### Content Quality

✅ **DO:**
- Explain your reasoning and methodology
- Include terminal output and screenshots
- Document dead ends and debugging
- Reference official resources (CVE, CVSS, OWASP)
- Use code syntax highlighting
- Include timing information
- Show both automated and manual techniques

❌ **DON'T:**
- Just paste commands without explanation
- Skip showing output/results
- Assume reader knows the vulnerability type
- Include sensitive/real data (credentials, IPs)
- Use outdated tool versions without noting it
- Forget to explain "why" behind each step

### Security Considerations

- ⚠️ **Never include**: Real credentials, API keys, private IPs (if shared lab)
- ✅ **Always sanitize**: Replace real values with placeholders `[REDACTED]`
- ✅ **Document carefully**: Enough detail for others to learn, not replicate on real systems
- ✅ **Add disclaimers**: Exploit on authorized systems only

### Image/Screenshot Tips

```markdown
# Good: Descriptive filename and alt text
![SQL Injection payload in Burp Suite parameter field](/assets/img/posts/2024-03-16/burp-sql-injection.png "Burp Suite showing successful SQL injection payload")

# Good: Annotated diagram
![Attack flow: Reconnaissance → Exploitation → Privilege Escalation](/assets/img/posts/2024-03-16/attack-flow.png)
```

**Image locations:**
```
assets/
└── img/
    └── posts/
        └── 2024-03-16/
            ├── screenshot1.png
            ├── diagram.png
            └── burp-request.png
```

### Code Formatting

**Good: With language and context**
```python
#!/usr/bin/env python3
# SQL Injection payload generator

import sys

def generate_payload(injection_point):
    """Generate SQL injection payload"""
    payload = f"' OR '1'='1"
    return payload
```

**Bad: No language, no context**
```
' OR '1'='1
```

---

## Common Categories & Tags

### Categories
- `security` - Always include for all posts
- `penetration-testing` - General pen-testing
- `ctf` - Capture The Flag challenges
- `web-security` - Web application security
- `network-security` - Network/infrastructure
- `malware-analysis` - Malware reverse engineering

### Tags (Examples)
**Vulnerabilities:**
- `sql-injection`, `xss`, `csrf`, `lfi`, `rfi`, `rce`
- `authentication-bypass`, `privilege-escalation`
- `buffer-overflow`, `command-injection`

**Platforms:**
- `hackthebox`, `tryhackme`, `offsec-labs`
- `htb-easy`, `htb-medium`, `htb-hard`

**Tools:**
- `metasploit`, `burp-suite`, `nmap`, `gobuster`
- `sqlmap`, `nikto`, `searchsploit`

**Techniques:**
- `reverse-shell`, `bind-shell`, `privilege-escalation`
- `password-cracking`, `exploitation`, `bypassing-waf`

**OS/Services:**
- `linux`, `windows`, `apache`, `nginx`
- `php`, `asp.net`, `nodejs`, `mysql`

---

## Template Structure

```
SECURITY_RESEARCH_TEMPLATE.md ← Reference this file

Your post sections (in order):
├── Overview
├── Reconnaissance & Enumeration
├── Vulnerability Analysis
├── Exploitation
├── Post-Exploitation
├── Key Findings & Lessons Learned
├── Remediation & Prevention
├── References
└── Appendix (scripts, cheatsheets)
```

---

## Example Posts (Structure)

### CTF/Lab Writeup (45 min lab)
```
Overview → Recon → Vuln Analysis → Exploitation → Lessons
Timeline: ~5-10 sections, 1500-2000 words
```

### Full Penetration Test Report (multi-day)
```
Overview → Methodology → Phase 1: Recon → Phase 2: Exploitation
→ Phase 3: Privilege Escalation → Post-Exploitation Findings
→ Remediation → Appendix
Timeline: Comprehensive, 3000-5000+ words
```

### Vulnerability Deep-Dive
```
Overview → Vulnerability Explanation → Attack Scenarios
→ Exploitation Examples → Mitigation Strategies → References
```

---

## Tips for Long-Form Content

**For 1000+ word posts:**
- Use headers and subheaders to break up content
- Include a table of contents (Jekyll auto-generates from headers)
- Use code blocks and images to reduce text density
- Break complex concepts into multiple sections

**For multiple commands:**
- Group related commands in code blocks
- Add comments explaining each step
- Show expected output below commands

---

## Staying Current

Check the template regularly for updates to include:
- New exploitation techniques
- Updated tool versions
- New vulnerability types
- Security best practices

Your template is located at: `SECURITY_RESEARCH_TEMPLATE.md`

---

## Questions?

Refer to:
- **Template file**: `SECURITY_RESEARCH_TEMPLATE.md`
- **General blog docs**: `README.md`
- **Development guide**: `CONTRIBUTING.md`

---

**Happy writing! Document your security journey.** 🔒🎯
