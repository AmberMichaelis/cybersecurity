<!-- @format -->

# Security Automation

This repository contains security automation tools for file analysis, log review, indicator extraction, and incident response support.

## Security Automation Tools

### `hash_file.py`

`hash_file.py` calculates the cryptographic hash of a file.

File hashing is commonly used in cybersecurity to identify files, verify file integrity, compare suspicious files against known indicators of compromise, and support incident response investigations.

The current version calculates a SHA-256 hash.

## Why File Hashing Matters

A file hash acts like a digital fingerprint for a file. If even one small part of the file changes, the hash value changes.

Security analysts use hashes to:

- Verify that a downloaded file has not been altered
- Compare files against known malware hashes
- Track suspicious files during investigations
- Document evidence during incident response
- Confirm whether two files are identical

## How to Use

Run the script from the command line:

```bash
python3 tools/hash_file.py path/to/file
```

Example:

```bash
python3 tools/hash_file.py sample-data/example.txt
```

Expected output:

```text
SHA-256: <calculated_hash_value>
```

## Skills

This project demonstrates:

- Python scripting
- Command-line tool development
- File handling
- Hashing with Python's `hashlib` library
- Basic cybersecurity automation
- Security documentation

---
---

### `log_keyword_scanner.py`

`log_keyword_scanner.py` scans log files for potentially suspicious keywords that may indicate errors, unauthorized activity, failed authentication attempts, or other security-relevant events.

Security analysts frequently review large log files during investigations. Automating keyword searches can help identify important events more quickly and reduce manual review time.

The current version searches for predefined keywords and displays matching log entries.

Predefined keywords:

- failed
- error
- denied
- unauthorized
- suspicious
- blocked
- malware

## How to Use

```bash
python3 tools/log_keyword_scanner.py path/to/file
```

Example:

```bash
python3 tools/log_keyword_scanner.py sample-data/example.log
```

Expected output:

```text
[FOUND] failed
Failed login attempt from 192.168.1.25

[FOUND] unauthorized
Unauthorized access detected
```

## Skills

This project demonstrates:

- Python scripting
- File handling
- String searching
- Log analysis fundamentals
- Security automation
- Incident response support
- Command-line tool development

---
---

## `ip_extractor.py`

`ip_extractor.py` extracts IPv4 addresses from a file and counts how often each address appears.

IP extraction is useful during log review, incident response, and threat analysis because analysts often need to identify repeated source addresses, suspicious external connections, or systems involved in an event.

The current version searches for IPv4 address patterns and displays each address with its occurrence count.

### How to Use

```bash
python3 tools/ip_extractor.py sample-data/example.log
```

Example:

```bash
python3 tools/ip_extractor.py sample-data/example.log
```

Expected output:

```text
IP addresses found:
----------------------------------------
192.168.1.25: 3
10.0.0.14: 1
203.0.113.55: 1
198.51.100.22: 1
```

---
---

## Project Structure

```text
security-automation/
├── README.md
├── tools/
│   ├── hash_file.py
│   ├── log_keyword_scanner.py
│   └── ip_extractor.py
└── sample-data/
    ├── example.txt
    └── example.log

```

## Planned Additions

Future tools include:

- IOC parser
- Basic URL analyzer
- Hash comparison tool
- Simple incident response helper scripts

## Status

This project is in progress and will be updated as new tools are added.
