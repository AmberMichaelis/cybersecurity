import re
import sys
from collections import Counter

# This regular expression looks for IPv4-style addresses.
# Example matches:
# 192.168.1.25
# 10.0.0.14
# 203.0.113.55
#
# Note:
# This pattern finds IPv4-looking strings, but it does not fully validate
# whether each number is between 0 and 255.
IPV4_PATTERN = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"


def extract_ip_addresses(filename):
    """
    Read a file, extract IPv4 addresses, count how often each address appears,
    and print the results in order from most common to least common.
    """

    # Open the file in read mode.
    # errors="ignore" prevents the script from crashing if the file contains
    # unexpected characters.
    with open(filename, "r", errors="ignore") as file:
        content = file.read()

    # Find all IPv4-looking addresses in the file content.
    ip_addresses = re.findall(IPV4_PATTERN, content)

    # Count how many times each IP address appears.
    ip_counts = Counter(ip_addresses)

    # If no IP addresses were found, tell the user and stop the function.
    if not ip_counts:
        print("No IP addresses found.")
        return

    print("IP addresses found:")
    print("-" * 40)

    # Print IP addresses from most common to least common.
    for ip_address, count in ip_counts.most_common():
        print(f"{ip_address}: {count}")


if __name__ == "__main__":
    # Make sure the user provided a file path.
    # Example:
    # python3 tools/ip_extractor.py sample-data/example.log
    if len(sys.argv) < 2:
        print("Usage: python3 tools/ip_extractor.py <filename>")
        sys.exit(1)

    # Store the filename provided by the user.
    filename = sys.argv[1]

    # Run the IP extraction function.
    extract_ip_addresses(filename)
