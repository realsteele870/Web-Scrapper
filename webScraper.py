import requests
from bs4 import BeautifulSoup

searchItem= input("What ebay item to search?: ")

searchItem= input("What ebay item to search?: ")

searchItem = searchItem.replace(" ","+")

print(searchItem)


URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + searchItem + "&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="srp-river-main")

avg_price = 0
items = 0
flag =1
item_elements = results.find_all("div", class_="s-item__info clearfix")
for item_element in item_elements:
    if flag == 0:
        title_element = item_element.find("h3", class_="s-item__title")
        price_element = item_element.find("span", class_="s-item__price")
        price_element =price_element.text.strip()
        realprice=price_element[1:]
        realprice=float(realprice)
        avg_price=avg_price + realprice
        print(title_element.text.strip())
        print(realprice)
        items= items+1
    flag = 0
realAverage= avg_price/items
print("average price is "+str(round(realAverage,2)))

