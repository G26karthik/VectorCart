import requests
import time
import sys

def verify():
    # 1. Check Backend
    try:
        print("Checking Backend...")
        resp = requests.get("http://localhost:8000/")
        if resp.status_code == 200:
            print("Backend is UP!")
        else:
            print(f"Backend returned {resp.status_code}")
            sys.exit(1)
    except Exception as e:
        print(f"Backend check failed: {e}")
        sys.exit(1)

    # 2. Trigger Scraping
    try:
        print("Triggering Scraping...")
        resp = requests.post("http://localhost:8000/api/v1/scrape/run")
        if resp.status_code == 200:
            print("Scraping started successfully!")
        else:
            print(f"Scraping trigger failed: {resp.status_code} - {resp.text}")
    except Exception as e:
        print(f"Scraping trigger failed: {e}")

    # 3. Check Frontend
    try:
        print("Checking Frontend...")
        resp = requests.get("http://localhost:3000/")
        if resp.status_code == 200:
            print("Frontend is UP!")
        else:
            print(f"Frontend returned {resp.status_code}")
    except Exception as e:
        print(f"Frontend check failed: {e}")

if __name__ == "__main__":
    verify()
