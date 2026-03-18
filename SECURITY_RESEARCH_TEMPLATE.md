# Security Research Post Template

This template is designed for documenting security research, penetration testing reports, and CTF/OSCP/OSWA writeups.

## How to Use

1. Copy this template for each new security research post
2. Replace all `[PLACEHOLDER]` sections with your content
3. Save as `_posts/YYYY-MM-DD-[slug].markdown` in your blog
4. Update the frontmatter with your specific details

---

## Template

```markdown
---
layout: post
title: "[CHALLENGE/LAB NAME] - [BRIEF DESCRIPTION]"
subtitle: "[Platform] - [Difficulty Level]"
date: YYYY-MM-DD
author: "Your Name"
categories: [security, penetration-testing]
tags: [vulnerability-type, tool1, tool2, technique]
img: "/assets/img/posts/[date]/[screenshot].png"
image_viewer_on: true
image_lazy_loader_on: true
---

## Overview

**Challenge/Lab:** [Name]
**Platform:** [Hack The Box / TryHackMe / OffSec Labs / etc.]
**Difficulty:** [Easy / Medium / Hard / Insane]
**Status:** ✅ Completed

### Summary

[1-2 sentence high-level summary of what this challenge/lab is about and what vulnerability/technique is demonstrated]

---

## Reconnaissance & Enumeration

### Initial Scan

```bash
[Insert reconnaissance commands]
```

**Findings:**
- Service 1: [version/info]
- Service 2: [version/info]
- Open ports: [list ports]

### Detailed Enumeration

#### [Service Name] - Port [XX]

[Describe what you discovered about this service]

```bash
[Enumeration commands]
```

**Results:**
- Finding 1
- Finding 2

---

## Vulnerability Analysis

### Vulnerability Identified: [Name]

**Type:** [SQL Injection / RCE / Authentication Bypass / etc.]
**Severity:** [Critical / High / Medium / Low]
**CVSS Score:** [X.X] (if applicable)

### Technical Details

[Explain the vulnerability in detail - how it works, why it exists, what makes it exploitable]

```
[Code snippet showing vulnerable code or configuration]
```

### Exploitation Feasibility

[Discuss likelihood of exploitation, requirements, mitigations]

---

## Exploitation

### Tools Used

| Tool | Version | Purpose |
|------|---------|---------|
| [Tool 1] | [version] | [What it does] |
| [Tool 2] | [version] | [What it does] |
| [Python Script] | Custom | [What it does] |

### Exploitation Steps

#### Step 1: [Action Description]

[Detailed explanation of what you're doing and why]

```bash
[Command or code]
```

**Output:**
```
[Expected or actual output]
```

#### Step 2: [Next Action]

[Continue with numbered steps...]

### Payload Development (if applicable)

#### Initial Payload

```
[Payload code/command]
```

**Explanation:**
[Break down what the payload does, line by line if complex]

#### Refined Payload

```
[Improved/working payload]
```

**Improvements:**
- Change 1
- Change 2

---

## Post-Exploitation

### Access Achieved

**User:** [username]
**Privilege Level:** [User / Admin / System / etc.]
**Shell Type:** [Reverse shell / Bind shell / Interactive terminal / etc.]

### Privilege Escalation (if applicable)

#### Enumeration

```bash
[Commands to find privilege escalation vector]
```

**Discovered:** [PE vector found]

#### Exploitation

```bash
[Commands to escalate privileges]
```

**Result:** [Escalated to root/admin level]

### Post-Exploitation Activities

- [Activity 1 - what you found/did]
- [Activity 2 - what you found/did]
- Flag Location: `/path/to/flag.txt` or `Environment Variable`

---

## Key Findings & Lessons Learned

### What Worked Well

1. [Technique/Tool 1] - Quickly identified [vulnerability]
2. [Technique/Tool 2] - Enabled efficient [exploitation step]

### Challenges Encountered

1. **Challenge:** [What went wrong]
   **Resolution:** [How you solved it]

2. **Challenge:** [What was difficult]
   **Resolution:** [How you overcame it]

### Key Lessons

- **Lesson 1:** [Important takeaway relevant to the penetration testing/certification]
- **Lesson 2:** [Another key insight]
- **Lesson 3:** [Technique/concept that enhanced your understanding]

---

## Remediation & Prevention

### For Systems Administrators

**Quick Fixes:**
1. [Immediate fix 1] - High priority
2. [Immediate fix 2] - High priority

**Long-term Solutions:**
1. [Solution 1] - Better practice
2. [Solution 2] - Security hardening

### Configuration Examples

```bash
# Secure configuration
[Recommended config]
```

---

## References

- **Vulnerability:** [Link to CVE / Security Advisory]
- **Tool Documentation:** [Link to tool guide]
- **Related Writeups:** [Link to similar challenge writeup]
- **Security Research:** [Link to relevant research paper/blog]
- **Methodology:** [OWASP Top 10, NIST Guidelines, etc.]

### Additional Resources

- [Video Tutorial / Course]
- [Documentation Link]
- [Related Certificate Info]

---

## Appendix

### Full Exploitation Script (if applicable)

```python
#!/usr/bin/env python3
"""
[Script description]
Usage: python3 exploit.py [target] [options]
"""

[Complete exploit code]
```

### Command Cheatsheet

```bash
# Reconnaissance
[command] - [what it does]

# Exploitation
[command] - [what it does]

# Post-Exploitation
[command] - [what it does]
```

---

## Timeline

| Step | Tool/Technique | Duration | Notes |
|------|----------------|----------|-------|
| Reconnaissance | nmap/Enum4linux | 5-10 min | Initial service discovery |
| Enumeration | [Tool] | 10-15 min | [Finding] |
| Exploitation | [Tool/Script] | 5 min | [Method] |
| Privilege Escalation | [Tool/Technique] | 10 min | [Method] |
| Post-Exploitation | Manual | 5 min | Flag collection |
| **Total** | - | **~45 min** | - |

---

**Status:** Complete ✅
**Last Updated:** YYYY-MM-DD
**Difficulty Assessment:** [Your honest difficulty rating]

```

---

## Tips for Using This Template

### 1. **Security Research Best Practices**
   - Document your entire process, including dead ends
   - Explain the "why" not just the "how"
   - Include relevant CVE numbers and CVSS scores
   - Reference industry standards (OWASP, NIST, etc.)

### 2. **Code/Command Formatting**
   - Use syntax highlighting (bash, python, etc.)
   - Include full context (command line prompts)
   - Show expected output when relevant
   - Comment complex one-liners

### 5. **Images & Screenshots**
   - Include terminal output screenshots
   - Show tool UI for important findings
   - Annotate diagrams showing attack flow
   - Place in `assets/img/posts/YYYY-MM-DD/` directory

---

## Example Frontmatter Values

```yaml
# Lab Example
---
layout: post
title: "HacktheBox - Lame - SQL Injection to RCE"
subtitle: "Easy Difficulty"
date: 2024-03-16
categories: [security, penetration-testing]
tags: [sql-injection, rce, linux, apache]
img: "/assets/img/posts/2024-03-16/lame-dashboard.png"
---

# Web Security Lab Example
---
layout: post
title: "WebGoat - SQL Injection Challenge"
subtitle: "Medium Difficulty"
date: 2024-03-16
categories: [security, web-security]
tags: [sql-injection, web-vulnerability, database]
img: "/assets/img/posts/2024-03-16/sql-injection-example.png"
---
```

---

## Post Generation Script (Optional)

If you want to generate posts from command line:

```bash
#!/bin/bash
# Create new security research post

DATE=$(date +%Y-%m-%d)
SLUG="$1"
FILENAME="_posts/${DATE}-${SLUG}.markdown"

cp SECURITY_RESEARCH_TEMPLATE.md "$FILENAME"
echo "Created: $FILENAME"
```

Save as `new-security-post.sh`, make executable with `chmod +x new-security-post.sh`, then use:
```bash
./new-security-post.sh oscp-lab-name
```

---

**Happy researching!** 🔐
