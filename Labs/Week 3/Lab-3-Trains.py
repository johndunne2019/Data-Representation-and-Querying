import requests
import csv
from bs4 import BeautifulSoup

url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'xml')
# print statement to test, commented out
#print (soup.prettify())
retrieveTags=['TrainStatus',
            'TrainLatitude',
            'TrainLongitude',
            'TrainCode',
            'TrainDate',
            'PublicMessage',
            'Direction'
            ]
# creating a csv file and writing to it
with open('week03_train.csv', mode='w') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    listings = soup.findAll("objTrainPositions")
    for listing in listings:
        #only show trains that have a latitude below Dublin 53.4
        lat = float(listing.TrainLatitude.string)
        if (lat < 53.4):
            # print statements for testing 
            #print(listing)
            #print(listing.TrainLatitude.string)
            entryList = []
            for retrieveTag in retrieveTags:
                #entryList.append(listing.find('TrainLatitude').string)
                entryList.append(listing.find(retrieveTag).string)
            train_writer.writerow(entryList)