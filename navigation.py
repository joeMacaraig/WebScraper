from bs4 import BeautifulSoup
import requests

url = "https://coinmarketcap.com/" #website of crypto
result = requests.get(url).text
file = BeautifulSoup(result, "lxml")

tbody = file.tbody 
trs = tbody.contents

prices = {}

for tr in trs[:5]: 
    crypto, price = tr.contents[2:4]
    name_result = crypto.p.string
    price_result = price.a.string

    prices[name_result] = price_result

print(prices)
