import requests
def service_check(url):
    try:
        response = requests.get(url, timeout = 5)
        if response.status_code == 200:
            print(f"Service at {url} is up")
        else:
            print(f"Service at {url} is not up")
    except requests.RequestException as e:
        print(f"Service at {url} is down. Error: {e}")
if __name__=="__main__":
    service_url = "https://www.chatgpt.com"
    service_check(service_url)

        