import re
import sys
from collections import Counter

# IOC = Indicator of Compromise.
# IOCs are pieces of evidence that may help identify suspicious or malicious activity.
# Common IOCs include IP addresses, domains, URLs, email addresses, and file hashes.

# Regex pattern for IPv4-looking addresses.
IPV4_PATTERN = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"

# Regex pattern for URLs beginning with http or https.
URL_PATTERN = r"https?://[^\s\"']+"

# Regex pattern for email addresses.
EMAIL_PATTERN = r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b"

# Regex pattern for common cryptographic hashes:
# MD5 = 32 hex characters
# SHA-1 = 40 hex characters
# SHA-256 = 64 hex characters
HASH_PATTERN = r"\b[a-fA-F0-9]{32}\b|\b[a-fA-F0-9]{40}\b|\b[a-fA-F0-9]{64}\b"


def extract_indicators(filename):
    """
    Read a file, extract common indicators of compromise,
    count occurrences, and print the results by category.
    """

    # Read the entire file as text.
    # errors="ignore" prevents crashes if the file contains unusual characters.
    with open(filename, "r", errors="ignore") as file:
        content = file.read()

    # Extract indicators using regex patterns.
    ipv4_addresses = re.findall(IPV4_PATTERN, content)
    urls = re.findall(URL_PATTERN, content)
    email_addresses = re.findall(EMAIL_PATTERN, content)
    hashes = re.findall(HASH_PATTERN, content)

    # Store results in a dictionary so each IOC type is easy to process.
    indicators = {
        "IPv4 Addresses": ipv4_addresses,
        "URLs": urls,
        "Email Addresses": email_addresses,
        "Hashes": hashes
    }

    # Track whether any indicators were found at all.
    found_any_indicators = False

    # Print results by category.
    for category, values in indicators.items():
        if values:
            found_any_indicators = True

            print(f"\n{category}")
            print("-" * len(category))

            # Count repeated indicators and print the most common first.
            counts = Counter(values)

            for indicator, count in counts.most_common():
                print(f"{indicator}: {count}")

    if not found_any_indicators:
        print("No indicators found.")


if __name__ == "__main__":
    # Make sure the user provided a file path.
    # Example:
    # python3 tools/ioc_parser.py sample-data/example.log
    if len(sys.argv) < 2:
        print("Usage: python3 tools/ioc_parser.py <filename>")
        sys.exit(1)

    # Store the filename provided by the user.
    filename = sys.argv[1]

    # Run the IOC parser.
    extract_indicators(filename)
