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

## Skills

This project demonstrates:

- Python scripting
- Regular expressions
- File parsing
- Indicator extraction
- Frequency counting
- Security log analysis
- Command-line tool development

---

---

## `ioc_parser.py`

`ioc_parser.py` extracts common indicators of compromise from a text file or log file.

Indicators of compromise, often called IOCs, are pieces of evidence that may help identify suspicious or malicious activity. Common examples include IP addresses, URLs, email addresses, and cryptographic file hashes.

This tool is designed to support basic log review, threat analysis, and incident response workflows by quickly identifying security-relevant indicators inside a file.

The current version extracts:

- IPv4 addresses
- URLs
- Email addresses
- MD5 hashes
- SHA-1 hashes
- SHA-256 hashes

### How to Use

Example:

```bash
python3 tools/ioc_parser.py sample-data/example.log
```

Example output:

```text
IPv4 Addresses
--------------
192.168.1.25: 3
203.0.113.55: 2
10.0.0.14: 1
198.51.100.22: 1

URLs
----
http://malicious-example.com/login: 1
https://example-bad-domain.com/payload: 1

Email Addresses
---------------
attacker@example.com: 1

Hashes
------
e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855: 1
5d41402abc4b2a76b9719d911017c592: 1
```

## Skills

This project demonstrates:

- Python scripting
- Regular expressions
- Indicator extraction
- File parsing
- Frequency counting
- Log review
- Incident response support
- Threat analysis fundamentals

---

---

## `url_analyzer.py`

`url_analyzer.py` performs a basic review of a URL and identifies simple warning signs that may appear in phishing links or suspicious web activity.

This tool is not a malware scanner or reputation checker. It is designed to practice URL parsing, basic security review, and command-line automation.

The current version checks for:

- Non-HTTPS URLs
- Suspicious keywords
- Unusually long URLs
- `@` symbols
- Multiple hyphens in the domain

### How to Use

Example:

```bash
python3 tools/url_analyzer.py "http://secure-login-example.com/update-password"
```

Example output:

```text
URL Analysis
----------------------------------------
Original URL: http://secure-login-example.com/update-password
Scheme: http
Domain: secure-login-example.com
Path: /update-password
Query String: None

Findings
----------------------------------------
[WARNING] URL does not use HTTPS.
[WARNING] Suspicious keyword found: login
[WARNING] Suspicious keyword found: secure
[WARNING] Suspicious keyword found: update
[WARNING] Suspicious keyword found: password
```

## Skills

This project demonstrates:

- Python scripting
- URL parsing
- Basic phishing analysis
- String matching
- Command-line tool development
- Security automation

---

---

## `hash_compare.py`

`hash_compare.py` compares a file's SHA-256 hash against a known hash value.

Hash comparison is useful in cybersecurity because analysts often need to verify whether a file matches a known-good file, a suspicious file, or a known malware indicator.

The tool calculates the SHA-256 hash of the provided file and compares it to the known hash supplied by the user.

### How to Use

Example:

```bash
python3 tools/hash_compare.py sample-data/example.txt <known_sha256_hash>
```

Example output:

```text
Hash Comparison
----------------------------------------
File: sample-data/example.txt
Calculated SHA-256: <calculated_hash>
Known SHA-256:      <known_hash>

[MATCH] The file hash matches the known hash.
```

## Skills

This project demonstrates:

- Python scripting
-File hashing
- Hash comparison
- File integrity verification
- Incident response support
- Command-line tool development

---

---

## Project Structure

```text
security-automation/
├── README.md
├── tools/
│   ├── hash_file.py
│   ├── hash_compare.py
│   ├── log_keyword_scanner.py
│   ├── ip_extractor.py
│   ├── ioc_parser.py
│   └── url_analyzer.py
└── sample-data/
    ├── example.txt
    └── example.log

```

## Planned Additions

Future tools include:

- Simple incident response helper scripts

## Status

This project is in progress and will be updated as new tools are added.
