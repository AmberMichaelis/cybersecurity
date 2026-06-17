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

* Verify that a downloaded file has not been altered
* Compare files against known malware hashes
* Track suspicious files during investigations
* Document evidence during incident response
* Confirm whether two files are identical

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

## Project Structure

```text
security-automation/
├── README.md
├── tools/
│   └── hash_file.py
└── sample-data/
    └── example.txt
```

## Skills

This project demonstrates:

* Python scripting
* Command-line tool development
* File handling
* Hashing with Python's `hashlib` library
* Basic cybersecurity automation
* Security documentation

## Planned Additions

Future tools include:

* Log keyword scanner
* IP address extractor
* IOC parser
* Basic URL analyzer
* Hash comparison tool
* Simple incident response helper scripts

## Status

This project is in progress and will be updated as new tools are added.
