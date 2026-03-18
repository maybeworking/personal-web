# Security Research Template Quick Reference

You now have a complete system for creating security research content!

## Files Created

| File | Purpose |
|------|---------|
| `SECURITY_RESEARCH_TEMPLATE.md` | Full template with all sections and examples |
| `SECURITY_CONTENT_GUIDE.md` | Comprehensive guide on how to write security posts |
| `new-security-post.py` | Python script to auto-generate new posts |

---

## Quick Start (30 seconds)

### Method 1: Using the Script (Easiest)

```bash
# Generate new post
python3 new-security-post.py "HTB Lame" "easy" "security"

# Or
python3 new-security-post.py "WebGoat SQL Injection" "medium" "web-security"

# With no arguments, shows help
python3 new-security-post.py
```

**What it does:**
- Creates `_posts/YYYY-MM-DD-[slug].markdown`
- Pre-fills basic structure
- Creates `assets/img/posts/YYYY-MM-DD/` for images
- Ready to edit and customize

### Method 2: Manual Copy

```bash
cp SECURITY_RESEARCH_TEMPLATE.md _posts/2024-03-16-lab-name.markdown
# Edit and customize as needed
```

---

## Post Structure at a Glance

```
📄 Your Security Post
├── 📋 Overview (Challenge details, difficulty, status)
├── 🔍 Reconnaissance & Enumeration (How you discovered services)
├── 🎯 Vulnerability Analysis (What vulnerability exists)
├── 💥 Exploitation (Step-by-step how you exploited it)
├── 🔓 Post-Exploitation (Privilege escalation, data collection)
├── 📚 Lessons Learned (Key takeaways and insights)
├── 🛡️ Remediation (How to fix/prevent)
├── 📖 References (CVEs, tools, resources)
└── 📎 Appendix (Full scripts, cheatsheets)
```

---

## Template Features

### Frontmatter (Auto-generated or customize)
```yaml
---
layout: post
title: "Lab Name - Vulnerability"
subtitle: "Difficulty Level"
date: YYYY-MM-DD
categories: [security, penetration-testing]
tags: [sql-injection, rce, linux]
img: "/assets/img/posts/YYYY-MM-DD/screenshot.png"
image_viewer_on: true
image_lazy_loader_on: true
---
```

### Sections Included
- ✅ Overview with challenge metadata
- ✅ Reconnaissance & enumeration
- ✅ Vulnerability analysis with CVSS
- ✅ Step-by-step exploitation
- ✅ Post-exploitation findings
- ✅ Privilege escalation (if applicable)
- ✅ Lessons learned & key takeaways
- ✅ Remediation guidance
- ✅ References & resources
- ✅ Timeline tracking
- ✅ Appendix for scripts

---

## Categories & Tags to Use

### Categories (pick main one)
- `security` - Always
- `penetration-testing` - General pen-testing
- `ctf` - CTF challenges
- `web-security` - Web vulns
- `network-security` - Network stuff

### Tags (multiple, security-specific)

**Vulnerability Types:**
- `sql-injection` `xss` `csrf` `lfi` `rfi` `rce`
- `authentication-bypass` `privilege-escalation`
- `buffer-overflow` `command-injection`
- `xxe` `insecure-deserialization`

**Platforms:**
- `hackthebox` `tryhackme` `offsec-labs`
- `htb-easy` `htb-medium` `htb-hard`

**Tools:**
- `metasploit` `burp-suite` `nmap` `gobuster`
- `sqlmap` `nikto` `john` `hashcat`

**OS/Services:**
- `linux` `windows` `apache` `nginx`
- `php` `aspnet` `nodejs` `python`

---

## Writing Workflow

### 1️⃣ Create Post
```bash
./new-security-post.py "Challenge Name" "difficulty" "oscp"
```

### 2️⃣ Open Editor
```bash
code "_posts/2024-03-16-slug.markdown"
```

### 3️⃣ Fill in Sections
- Start with Overview (challenge details)
- Add Reconnaissance findings
- Document Vulnerability discovered
- Write Exploitation steps (most important!)
- Add Post-Exploitation results
- Conclude with Lessons Learned and insights

### 4️⃣ Add Images
```
Assets saved to: assets/img/posts/2024-03-16/
├── screenshot1.png
├── burp-request.png
└── exploitation-flow.png
```

Reference in post:
```markdown
![Description](/assets/img/posts/2024-03-16/screenshot1.png "Optional title")
```

### 5️⃣ Test Locally
```bash
bundle exec jekyll serve
# Visit http://localhost:4000 and find your post
```

### 6️⃣ Publish
```bash
git add _posts/2024-03-16-lab-name.markdown
git commit -m "Add security writeup: Challenge Name"
git push origin main
# Auto-deploys to Netlify
```

---

## Example Usage

### Security Lab Writeup
```bash
python3 new-security-post.py "HTB Lame - RCE" "easy" "security"
# Creates: _posts/2024-03-16-htb-lame-rce.markdown
```

### Web Security Writeup
```bash
python3 new-security-post.py "WebGoat SQL Injection" "medium" "web-security"
# Creates: _posts/2024-03-16-webgoat-sql-injection.markdown
```

### CTF Writeup
```bash
python3 new-security-post.py "Picoctf Web Challenge" "medium" "ctf"
# Creates: _posts/2024-03-16-picoctf-web-challenge.markdown
```

---

## Best Practices Checklist

**Before Publishing:**
- ✅ Title is descriptive (includes vulnerability type)
- ✅ Tags are relevant (tools, techniques, vulnerability)
- ✅ All sections are filled in
- ✅ Code blocks have syntax highlighting
- ✅ Images are sanitized (no real IPs/credentials)
- ✅ Lessons Learned section is insightful
- ✅ References are complete
- ✅ Post tested locally with `jekyll serve`
- ✅ Spelling/grammar check
- ✅ Links are working

**Content Quality:**
- ✅ Explain the "why" not just "how"
- ✅ Show command output
- ✅ Document challenges & solutions
- ✅ Include timing information
- ✅ Reference CVE/OWASP standards
- ✅ Make it readable (not a wall of text)

---

## File Locations

```
personal-web/
├── SECURITY_RESEARCH_TEMPLATE.md       ← Reference full template
├── SECURITY_CONTENT_GUIDE.md           ← Read detailed guide
├── new-security-post.py                ← Run to create posts
├── _posts/
│   └── 2024-03-16-your-lab.markdown    ← Your posts here
└── assets/img/posts/
    └── 2024-03-16/
        ├── screenshot1.png
        ├── diagram.png
        └── ...                          ← Images here
```

---

## Common Commands

```bash
# Generate security post
python3 new-security-post.py "Lab Name" "easy" "security"

# Generate web security post
python3 new-security-post.py "Lab Name" "medium" "web-security"

# Test locally
bundle exec jekyll serve

# View posts
# Browse to: http://localhost:4000/categories/security/

# Publish
git add _posts/2024-03-16-lab-name.markdown
git commit -m "Add security writeup: Lab Name"
git push
```

---

## Need Help?

**For template structure:** See `SECURITY_RESEARCH_TEMPLATE.md`

**For detailed guide:** See `SECURITY_CONTENT_GUIDE.md`

**For blog setup:** See `README.md`

**For development:** See `CONTRIBUTING.md`

---

## Tips for Success

1. **Capture while fresh**: Document immediately after completing challenge
2. **Show your process**: Include dead ends and troubleshooting
3. **Explain thoroughly**: Others should learn from your post
4. **Time management**: Track how long each phase took
5. **Stay updated**: Revisit posts if exploits/techniques change
6. **Reuse templates**: Consistent structure makes writing faster
7. **Cross-reference**: Link to related posts and resources

---

**You're all set! Start documenting your security journey.** 🔐🎯

Questions? Check the guides above or refer to main `README.md` for general blog setup.
