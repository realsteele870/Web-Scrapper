import requests, statistics
from bs4 import BeautifulSoup

searchItem= input("What ebay item to search?: ")

def Average(lst):
    return sum(lst)/len(lst)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

searchItem = searchItem.replace(" ","+")

print(searchItem)


URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=" + searchItem + "&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=1"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

results = soup.find(id="srp-river-main")
priceList = []
flag =1
item_elements = results.find_all("div", class_="s-item__info clearfix")
for item_element in item_elements:
    if flag == 0:
        title_element = item_element.find("h3", class_="s-item__title")
        price_element = item_element.find("span", class_="s-item__price")
        price_element =price_element.text.strip()
        realprice=price_element[1:]
        if is_number(realprice):
            realprice=float(realprice)
            priceList.append(realprice)
        
        print(title_element.text.strip())
        print(realprice)
        
    flag = 0


print("average price is: "+ str(round(Average(priceList),2)))
print("median of price is: "+ str(statistics.median(priceList)))





