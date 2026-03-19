import requests
import argparse
import sys
from urllib.parse import urlparse

def ensure_scheme(url):
    """Ensure the URL has a scheme (http:// or https://)."""
    if not urlparse(url).scheme:
        return "https://https://www.phdsec.com" + url.lstrip("/")  # Prepend https if no scheme
    return url

def brute(base_url, wordlist):
    base_url = ensure_scheme(base_url)
    if not base_url.endswith("/"):
        base_url += "/"

    for word in wordlist:
        word = word.strip()  # Remove newlines and whitespace
        if not word:
            continue
        url = base_url + word
        try:
            response = requests.get(url, timeout=1)
            if response.status_code == 200:
                print(f"Found: {url}")
            else:
                print(f"Not found: {url} (Status: {response.status_code})")
        except requests.exceptions.Timeout:
            print(f"Timeout: {url}")
        except requests.exceptions.ConnectionError:
            print(f"ConnectionError: {url}")

# Parse command-line arguments
parser = argparse.ArgumentParser(description="Simple directory brute-forcer")
parser.add_argument("base_url", help="Base URL to scan (e.g., http://https://www.phdsec.com)")
args = parser.parse_args()

# Read wordlist from stdin
wordlist = sys.stdin.readlines()
brute(args.base_url, wordlist)