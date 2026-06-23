import sys
from urllib.parse import urlparse

# Common suspicious words that may appear in phishing or malicious URLs.
SUSPICIOUS_KEYWORDS = [
    "login",
    "verify",
    "update",
    "secure",
    "account",
    "password",
    "bank",
    "free",
    "urgent",
    "gift"
]


def analyze_url(url):
    """
    Analyze a URL for basic suspicious characteristics.
    This is not a malware scanner. It is a beginner-friendly URL review tool.
    """

    parsed_url = urlparse(url)

    scheme = parsed_url.scheme
    domain = parsed_url.netloc
    path = parsed_url.path
    query = parsed_url.query

    print("URL Analysis")
    print("-" * 40)
    print(f"Original URL: {url}")
    print(f"Scheme: {scheme}")
    print(f"Domain: {domain}")
    print(f"Path: {path}")
    print(f"Query String: {query if query else 'None'}")
    print()

    warnings = []

    # Check whether the URL uses HTTPS.
    if scheme != "https":
        warnings.append("URL does not use HTTPS.")

    # Check for suspicious keywords anywhere in the URL.
    lowercase_url = url.lower()
    for keyword in SUSPICIOUS_KEYWORDS:
        if keyword in lowercase_url:
            warnings.append(f"Suspicious keyword found: {keyword}")

    # Check for unusually long URLs.
    if len(url) > 100:
        warnings.append("URL is unusually long.")

    # Check for the @ symbol, which can be used in deceptive URLs.
    if "@" in url:
        warnings.append("URL contains '@', which can be used to obscure the real destination.")

    # Check for many hyphens in the domain.
    if domain.count("-") >= 3:
        warnings.append("Domain contains multiple hyphens.")

    print("Findings")
    print("-" * 40)

    if warnings:
        for warning in warnings:
            print(f"[WARNING] {warning}")
    else:
        print("No basic warning signs found.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 tools/url_analyzer.py <url>")
        sys.exit(1)

    url = sys.argv[1]
    analyze_url(url)
