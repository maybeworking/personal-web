# Name - 192.168.XX.XX

IP:
OS:
Web-Technology: 
Users & Credentials (any):

**Linux**
find loot
```
find . -type -f -name "*.txt"
```
```
hostname && whoami && cat /root/proof.txt && ip a
```
**Windows**
find loot
```
for /R ".\" %A in (*.txt) do echo %~fA %~zA) | findstr /v"echo
```
```
hostname && whoami.exe && type C:\Users\Administrator\Desktop\proof.txt && ipconfig
```
```
hostname; whoami; Get-Content C:\Users\Administrator\Desktop\proof.txt; Get-FileHash C:\Users\Administrator\Desktop\proof.txt -Algorithm MD5; ipconfig
```
local.txt flag:
proof.txt flag:

## To Try



## Findings



# Recon

## Nmap
```bash
rustscan -a $ip --accessible -r 1-65535 --ulimit 5000 -- -A -sC -sV
```
```
feroxbuster -u http://$ip -C 403 404 405 503 -x php,txt,json,docx,html -t 5 -r -q
```
```
grep -nir "" /usr/share/wordlists/seclists
```
## Web Service Enumeration

### Nikto

### Wfuzz

#### Files / (web root)

#### Directories / (Web root)

# Other