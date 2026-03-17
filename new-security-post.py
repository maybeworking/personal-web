#!/usr/bin/env python3
"""
Security Research Post Generator

Generates new security research blog posts with proper structure and metadata.
Used for documenting OSCP, OSWA, CTF challenges, and penetration testing writeups.

Usage:
    python3 new-security-post.py "Lab Name" "difficulty" "category"
    python3 new-security-post.py "HTB Lame" "easy" "oscp"
    python3 new-security-post.py "WebGoat SQL" "medium" "oswa"
    python3 new-security-post.py  # Shows help
"""

import sys
import os
import re
from datetime import datetime
from pathlib import Path


class Colors:
    """ANSI color codes for terminal output"""
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color


def print_header(text):
    """Print colored header"""
    print(f"{Colors.YELLOW}{text}{Colors.NC}")


def print_success(text):
    """Print success message"""
    print(f"{Colors.GREEN}✓ {text}{Colors.NC}")


def print_error(text):
    """Print error message"""
    print(f"{Colors.RED}✗ {text}{Colors.NC}")
    sys.exit(1)


def print_info(text):
    """Print info message"""
    print(f"{Colors.BLUE}ℹ {text}{Colors.NC}")


def generate_slug(lab_name):
    """
    Convert lab name to URL-friendly slug.

    Args:
        lab_name: Lab name (e.g., "HTB Lame")

    Returns:
        Slug (e.g., "htb-lame")
    """
    # Convert to lowercase
    slug = lab_name.lower()
    # Replace spaces and special chars with hyphens
    slug = re.sub(r'[^a-z0-9]+', '-', slug)
    # Remove leading/trailing hyphens
    slug = slug.strip('-')
    # Replace multiple consecutive hyphens with single hyphen
    slug = re.sub(r'-+', '-', slug)
    return slug


def create_post_template(lab_name, difficulty, category, date_str):
    """
    Create the markdown template for a new post.

    Args:
        lab_name: Name of the lab/challenge
        difficulty: Difficulty level (easy, medium, hard, insane)
        category: Category (oscp, oswa, ctf, etc.)
        date_str: Date string (YYYY-MM-DD)

    Returns:
        Markdown template string
    """
    template = f"""---
layout: post
title: "{lab_name}"
subtitle: "{category} - {difficulty}"
date: {date_str}
author: "Your Name"
categories: [security, {category}]
tags: [todo-update-tags]
img: ":{date_str}/[screenshot].png"
image_viewer_on: true
image_lazy_loader_on: true
---

## Overview

**Challenge/Lab:** {lab_name}
**Platform:** [Hack The Box / TryHackMe / OffSec Labs / etc.]
**Difficulty:** {difficulty.capitalize()}
**Certification:** [OSCP / OSWA / CEH / etc.]
**Status:** 🔄 In Progress

### Summary

[Add 1-2 sentence summary of what this challenge/lab demonstrates]

---

## Reconnaissance & Enumeration

### Initial Scan

```bash
# Add reconnaissance commands
```

**Findings:**
- [Finding 1]
- [Finding 2]

---

## Vulnerability Analysis

### Vulnerability Identified

**Type:** [Vulnerability Type]
**Severity:** [Critical / High / Medium / Low]

[Explain the vulnerability]

---

## Exploitation

### Tools Used

| Tool | Purpose |
|------|---------|
| [Tool 1] | [Purpose] |
| [Tool 2] | [Purpose] |

### Exploitation Steps

**Step 1:** [Description]

```bash
[Command]
```

---

## Post-Exploitation

### Access Achieved

**User:** [username]
**Privilege Level:** [Level]

---

## Key Findings & Lessons Learned

### What Worked Well
- [Lesson 1]
- [Lesson 2]

### Challenges Encountered
- **Challenge:** [What was difficult]
- **Resolution:** [How you solved it]

---

## References

- [Reference 1]
- [Reference 2]

---

**Status:** 🔄 In Progress
**Last Updated:** {date_str}

"""
    return template


def show_help():
    """Display help message"""
    print_header("Security Research Post Generator")
    print()
    print("Usage: python3 new-security-post.py <lab_name> <difficulty> <category>")
    print()
    print("Arguments:")
    print("  lab_name    - Name of the lab or challenge")
    print("  difficulty  - Difficulty level: easy, medium, hard, insane")
    print("  category    - Category: oscp, oswa, ctf, penetration-testing, web-security")
    print()
    print("Examples:")
    print("  python3 new-security-post.py \"HTB Lame\" easy oscp")
    print("  python3 new-security-post.py \"WebGoat SQL Injection\" medium oswa")
    print("  python3 new-security-post.py \"PicoCTF Web 100\" easy ctf")
    print()


def main():
    """Main function"""
    # Show help if no arguments
    if len(sys.argv) == 1:
        show_help()
        return

    # Validate arguments
    if len(sys.argv) < 2:
        print_error("Missing arguments. Use: python3 new-security-post.py \"Lab Name\" \"difficulty\" \"category\"")

    lab_name = sys.argv[1]
    difficulty = sys.argv[2] if len(sys.argv) > 2 else "medium"
    category = sys.argv[3] if len(sys.argv) > 3 else "security"

    # Validate difficulty
    valid_difficulties = ['easy', 'medium', 'hard', 'insane']
    if difficulty.lower() not in valid_difficulties:
        print_error(f"Invalid difficulty. Must be one of: {', '.join(valid_difficulties)}")

    # Generate slug and date
    slug = generate_slug(lab_name)
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"_posts/{date_str}-{slug}.markdown"
    img_dir = f"assets/img/posts/{date_str}"

    # Check if file already exists
    if os.path.exists(filename):
        print_error(f"File already exists: {filename}")

    # Create image directory
    Path(img_dir).mkdir(parents=True, exist_ok=True)

    # Create post file
    template = create_post_template(lab_name, difficulty.lower(), category, date_str)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(template)

    # Print success messages
    print()
    print_success(f"Created new post: {filename}")
    print_success(f"Image directory: {img_dir}")
    print()

    print_header("Next steps:")
    print(f"1. Edit the post: code \"{filename}\"")
    print(f"2. Add images to: {img_dir}")
    print("3. Update tags and fill in sections")
    print("4. Test locally: bundle exec jekyll serve")
    print(f"5. Commit: git add {filename}")
    print()
    print_info("Template structure: SECURITY_RESEARCH_TEMPLATE.md")
    print_info("Content guide: SECURITY_CONTENT_GUIDE.md")
    print()


if __name__ == "__main__":
    main()
