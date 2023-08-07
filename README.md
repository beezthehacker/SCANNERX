# SCANNERX

## Description
SCANNERX is a simple web vulnerability scanner tool written in Python 3. It can scan a target URL for common vulnerabilities and security misconfigurations. The tool uses a wordlist to check for specific directories and displays the scan results in a colorful output.

## Features
- Scans a target URL for vulnerabilities and security issues.
- Supports checking response codes for each scanned directory.
- Provides colorful output for better visibility.

## Requirements
SCANNERX requires the following to be installed:
- Python 3
- `requests` library
- `beautifulsoup4` library
- `colorama` library

You can install the required libraries using the following command:
```bash
pip install -r requirements.txt

Usage
To use SCANNERX, follow these steps:

Open a terminal or command prompt in the directory containing scannerx.py.
Run the scanner with the following command: python scannerx.py <target_url> [-w <wordlist_path>] [--show-response-codes]
Replace <target_url> with the URL you want to scan. Optionally, you can specify a custom wordlist using the -w flag. If not provided, the default wordlist.txt will be used. Use the --show-response-codes flag to display the HTTP response codes.

Example
To scan a target URL http://example.com with response codes displayed and a custom wordlist custom_wordlist.txt, use:python scannerx.py http://example.com -w custom_wordlist.txt --show-response-codes

License
SCANNERX is released under the MIT License.


This `README.md` file includes all the provided information in a grouped format to make it more organized and easily readable. Feel free to modify it according to your specific project details. Remember to add the relevant code files and the `requirements.txt` file to your project repository on GitHub.
