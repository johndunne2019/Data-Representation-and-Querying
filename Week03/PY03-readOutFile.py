import requests
from bs4 import BeautifulSoup
with open("../Week02/carviewer2.html") as fp:
    soup = BeautifulSoup(fp, 'html.parser')
rows = soup.findAll("tr")
for row in rows:
    print("----------")
    #print(row)
    cols = row.findAll("td")
    datalist = []
    for col in cols:
        datalist.append(col.text)
    print(datalist)