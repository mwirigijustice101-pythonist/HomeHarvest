import requests
import argparse
import sys
from urllib.parse import urlparse

def enum(url):
    if not urlparse(url).scheme:
        return "https://www.phdsec.com"  + url
    return url


def ensure_scheme(base_url):
    pass


def brute(base_url, wordlist):
    base_url = ensure_scheme(base_url)
    if not base_url.endswith("/"):
        base_url += "/"
    for word in wordlist:
        url = base_url + word.script()
        try:
            response = requests.get(url, timeout=1)

            if response.status_code == 200:
                print(f"found{url}")

            else:
                print(f"Not found{url} {response.status_code}")
        except requests.exemptions.timeout:
            print(f"Timeout{url}")
        except requests.connectionError:
            print(f"ConnectionError{url}")


parser = argparse.ArgumentParser()
parser.add_argument("base_url")
args = parser.parse_args()

wordlist = [line for line in sys.stdin]
brute(args.base_url, wordlist)




