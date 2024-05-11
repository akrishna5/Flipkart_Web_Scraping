import pandas as pd
import requests
from bs4 import BeautifulSoup

Product_name = []
Prices = []
Description = []
Rating = []

for i in range(1,6):
    url = "https://www.flipkart.com/search?q=mobiles+under+50000&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_16_na_na_ps&otracker1=AS_Query_OrganicAutoSuggest_2_16_na_na_ps&as-pos=2&as-type=RECENT&suggestionId=mobiles+under+50000&requestId=fc39be41-5ae0-4280-94d9-0ae85ebb272f&as-searchtext=mobiles+under+50000&page="+str(i)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    box = soup.find("div", class_ = "DOjaWF gdgoEp")

    names = box.find_all("div", class_ = "KzDlHZ")
    for i in names:
        name = i.text
        Product_name.append(name)

    prices = box.find_all("div", class_ = "Nx9bqj _4b5DiR")
    for i in prices:
        name = i.text
        Prices.append(name)

    desc = box.find_all("ul", class_ = "G4BRas")
    for i in desc:
        name = i.text
        Description.append(name)

    rating = box.find_all("div", class_ = "XQDdHH")
    for i in rating:
        name = i.text
        Rating.append(name)

df = pd.DataFrame({"Product Name": Product_name,
                   "Prices": Prices,
                   "Description": Description,
                   "Rating": Rating})
print(df)

df.to_csv("flipkart_mobiles_under_50000")