import sys

# Predefined keywords that may indicate security-relevant log events.
# Version 1 keeps these as constants so the tool stays simple and easy to test.
SUSPICIOUS_KEYWORDS = [
    "failed",
    "error",
    "denied",
    "unauthorized",
    "suspicious",
    "blocked",
    "malware"
]

def scan_log_file(filename):
    """
    Reads a log file line by line and prints lines that contain
    suspicious keywords.
    """

    matches_found = 0

    # Open the log file in read mode.
    # errors="ignore" helps prevent the script from crashing on unusual characters.
    with open(filename, "r", errors="ignore") as log_file:
        for line_number, line in enumerate(log_file, start=1):

            # Convert the line to lowercase so keyword matching is case-insensitive.
            lowercase_line = line.lower()

            # Check each keyword against the current log line.
            for keyword in SUSPICIOUS_KEYWORDS:
                if keyword in lowercase_line:
                    matches_found += 1

                    print(f"[MATCH] Line {line_number}")
                    print(f"Keyword: {keyword}")
                    print(f"Log Entry: {line.strip()}")
                    print("-" * 60)

                    # Stop checking more keywords for this same line
                    # so the same log entry does not print multiple times.
                    break

    print(f"Scan complete. Total matching lines: {matches_found}")


if __name__ == "__main__":
    # Make sure the user provided a log file path.
    if len(sys.argv) < 2:
        print("Usage: python3 tools/log_keyword_scanner.py <log_file>")
        sys.exit(1)

    filename = sys.argv[1]
    scan_log_file(filename)
