---
layout: links
# multilingual page pair id, this must pair with translations of this page. (This name must be unique)
lng_pair: id_links

# publish date (used for seo)
# if not specified, site.time will be used.
#date: 2022-03-03 12:32:00 +0000

# for override items in _data/lang/[language].yml
#title: My title
#button_name: "My button"
# for override side_and_top_nav_buttons in _data/conf/main.yml
#icon: "fa fa-bath"

# seo
# if not specified, date will be used.
#meta_modify_date: 2022-03-03 12:32:00 +0000
# check the meta_common_description in _data/owner/[language].yml
#meta_description: ""

# optional
# please use the "image_viewer_on" below to enable image viewer for individual pages or posts (_posts/ or [language]/_posts folders).
# image viewer can be enabled or disabled for all posts using the "image_viewer_posts: true" setting in _data/conf/main.yml.
#image_viewer_on: true
# please use the "image_lazy_loader_on" below to enable image lazy loader for individual pages or posts (_posts/ or [language]/_posts folders).
# image lazy loader can be enabled or disabled for all posts using the "image_lazy_loader_posts: true" setting in _data/conf/main.yml.
#image_lazy_loader_on: true
# exclude from on site search
#on_site_search_exclude: true
# exclude from search engines
#search_engine_exclude: true
# to disable this page, simply set published: false or delete this file
#published: false


# you can always move this content to _data/content/ folder
# just create new file at _data/content/links/[language].yml and move content below.
###########################################################
#                Links Page Data
###########################################################
page_data:
  main:
    header: "Links"
    info: "Useful security resources, tools, and learning platforms."

  category:
    - title: "Practice Labs"
      type: id_labs
      color: "#e94560"
    - title: "Learning"
      type: id_learning
      color: "#62b462"
    - title: "Tools & References"
      type: id_tools
      color: "#2FD0ED"
    - title: "Communities"
      type: id_community
      color: "#F4A273"

  list:
    # labs
    - type: id_labs
      title: "Hack The Box"
      url: "https://www.hackthebox.com/"
      info: "Leading cybersecurity upskilling platform with hands-on labs and CTF challenges."
    - type: id_labs
      title: "TryHackMe"
      url: "https://tryhackme.com/"
      info: "Learn cybersecurity through browser-based guided learning paths and hands-on labs."
    - type: id_labs
      title: "OffSec Proving Grounds"
      url: "https://www.offsec.com/labs/"
      info: "Practice labs from OffSec — the team behind OSCP. Includes Play (free) and Practice tiers."
    - type: id_labs
      title: "PicoCTF"
      url: "https://picoctf.org/"
      info: "Beginner-friendly CTF platform from Carnegie Mellon. Great for web, forensics, and crypto."
    - type: id_labs
      title: "VulnHub"
      url: "https://www.vulnhub.com/"
      info: "Download vulnerable VMs to practice offensive security locally."

    # learning
    - type: id_learning
      title: "HackTricks"
      url: "https://book.hacktricks.wiki/"
      info: "Comprehensive wiki of hacking techniques, privilege escalation, web exploits, and more."
    - type: id_learning
      title: "OWASP Top 10"
      url: "https://owasp.org/www-project-top-ten/"
      info: "The standard awareness document for web application security risks."
    - type: id_learning
      title: "GTFOBins"
      url: "https://gtfobins.github.io/"
      info: "Curated list of Unix binaries that can be used to bypass local security restrictions."
    - type: id_learning
      title: "LOLBAS"
      url: "https://lolbas-project.github.io/"
      info: "Living Off The Land Binaries, Scripts, and Libraries for Windows."
    - type: id_learning
      title: "PayloadsAllTheThings"
      url: "https://github.com/swisskyrepo/PayloadsAllTheThings"
      info: "A list of useful payloads and bypass techniques for web application security."

    # tools
    - type: id_tools
      title: "ExploitDB"
      url: "https://www.exploit-db.com/"
      info: "The Exploit Database — a CVE-compliant archive of public exploits and vulnerable software."
    - type: id_tools
      title: "CyberChef"
      url: "https://gchq.github.io/CyberChef/"
      info: "A web app for encryption, encoding, compression, and data analysis."
    - type: id_tools
      title: "Shodan"
      url: "https://www.shodan.io/"
      info: "Search engine for internet-connected devices. Great for reconnaissance."
    - type: id_tools
      title: "CVE Details"
      url: "https://www.cvedetails.com/"
      info: "Free CVE security vulnerability database and search engine."
    - type: id_tools
      title: "RevShells"
      url: "https://www.revshells.com/"
      info: "Reverse shell payload generator for various languages and shells."

    # community
    - type: id_community
      title: "r/netsec"
      url: "https://www.reddit.com/r/netsec/"
      info: "Technical information security community on Reddit."
    - type: id_community
      title: "InfoSec.exchange"
      url: "https://infosec.exchange/"
      info: "Mastodon instance for the information security community."
---
