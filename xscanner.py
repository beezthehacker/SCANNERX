# MIT License
# Copyright (c) 2023 Beez

import requests
from bs4 import BeautifulSoup
import argparse
import re
from colorama import init, Fore
import random

# Initialize colorama
init(autoreset=True)

# Function to request a URL and parse the HTML content
def fetch_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
        else:
            return False
    except requests.exceptions.RequestException as e:
        return False

# Function to find and report vulnerabilities
def scan_url(url, show_response_codes, wordlist_path):
    print(f"{random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])}Scanning URL: {url}")
    success = fetch_url(url)
    if not success:
        print(f"{Fore.RED}ERROR")
        return

    if show_response_codes:
        print(f"{Fore.CYAN}Response Code: {requests.get(url).status_code}")

    # Perform vulnerability scanning logic here
    # Example: Look for common vulnerabilities like XSS, SQL injection, etc.
    # Example: Analyze form inputs for potential injection points
    # Example: Analyze HTTP headers for security misconfigurations

    # For demonstration purposes, let's use a wordlist to check for a specific directory
    with open(wordlist_path, 'r') as wordlist_file:
        wordlist = wordlist_file.read().splitlines()

    for directory in wordlist:
        test_url = f"{url}/{directory}"
        success = fetch_url(test_url)
        if success:
            print(f"{random.choice([Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN])}DIRECTORY: /{directory} [200] OK")
        else:
            print(f"{Fore.RED}ERROR")

def add_scheme(url):
    if not re.match(r'^https?://', url):
        url = 'http://' + url
    return url

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simple Web Vulnerability Scanner")
    parser.add_argument("url", help="Target URL to scan")
    parser.add_argument("--show-response-codes", action="store_true", help="Show the HTTP response codes")
    parser.add_argument("-w", "--wordlist", default="wordlist.txt", help="Path to the wordlist file (default: wordlist.txt)")
    args = parser.parse_args()

    target_url = add_scheme(args.url)
    scan_url(target_url, args.show_response_codes, args.wordlist)

