import requests
import re
import json

url = "https://books.toscrape.com/catalogue/page-1.html"
response = requests.get(url)
if response.status_code != 200:
    print(f"Not able to fetch: {response.status_code}")
    exit()

html = response.text

# ✅ Corrected regex patterns
titles = re.findall(r'<h3><a href=".*?" title="(.*?)">', html)
prices = re.findall(r'<p class="price_color">£([\d\.]+)</p>', html)

books = []
for title, price in zip(titles, prices):
    books.append({
        "title": title,
        "price": f"£{price}"
    })

for book in books:
    print(f"{book['title']} — {book['price']}")