# Extracting data frm myhome.ie and sending to a csv file 

import requests
import csv
from bs4 import BeautifulSoup
page = requests.get("https://www.myhome.ie/residential/offaly/property-for-sale?page=2")

soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

# creating a csv file to write the contents to
home_file = open('week03MyHome.csv', mode='w')
home_writer = csv.writer(home_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)

# view page source on the webpage and searched for the div we need to find which was PropertyListingCard
listings = soup.findAll("div", class_="PropertyListingCard")

# finall entries and store in a list
for listing in listings:
    entryList = []

    # append the price and address of each listings to the list
    price = listing.find(class_="PropertyListingCard__Price").text
    entryList.append(price)
    address = listing.find(class_="PropertyListingCard__Address").text
    entryList.append(address)
    #print(price)
    #print(address)

    home_writer.writerow(entryList)
home_file.close() # csv file closed when for loop terminates