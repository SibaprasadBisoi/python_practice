import requests
import time

websites = [
    "https://www.google.com",
    "https://www.amazon.com",
    "https://www.flipkirt.com",
    "https://nonexistent.com"
]

def check_website(url):
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"{url} is up and running!")
        else:
            print(f"{url} returned status: {response.status_code}")
    except Exception as e:
        print(f" {url} is down: {e}")

if __name__ == "__main__":
    while True:
        print("\n checking websites....")
        for site in websites:
            check_website(site)
        print(f" waiting 60 seconds before next check..\n")
        time.sleep(60)