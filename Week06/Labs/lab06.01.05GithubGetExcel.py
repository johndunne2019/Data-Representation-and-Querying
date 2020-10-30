# Get all the followers from Github and write to an excel file

import requests, json 
from xlwt import *

def getJSONFromUrl(url):
    response = requests.get(url)
    data = response.json()
    return data

#url = "https://api.github.com/users?since=100"
url = "https://api.github.com/users/andrewbeattycourseware/followers"

data = getJSONFromUrl(url)
#print (data)
#Get the file name for the new file to write

filename = 'githubusers.json'

# If the file name exists, write a JSON string into the file.
if filename:
    # Writing JSON data
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

#Write to an excel file
w = Workbook()
ws = w.add_sheet('followers')
row = 0;
ws.write(row,0,"login")
ws.write(row,1,"id")
ws.write(row,2,"node_id")
ws.write(row,3,"gravatar_url")
ws.write(row,4,"url")
ws.write(row,5,"html_url")
ws.write(row,6,"followers_url")
ws.write(row,7,"following_url")
ws.write(row,8,"gists_url")
ws.write(row,9,"starred_url")
ws.write(row,10,"subscriptions_url")
ws.write(row,11,"organizations_url")
ws.write(row,12,"respos_url")
ws.write(row,13,"events_url")
ws.write(row,14,"received_events_url")
ws.write(row,15,"type")
ws.write(row,16,"site_admin")
row += 1
for follower in data["followers"]:
    ws.write(row,0,follower["login"])
    ws.write(row,1,follower["id"])
    ws.write(row,2,follower["node_id"])
    ws.write(row,3,follower["gravatar_url"])
    ws.write(row,4,follower["url"])
    ws.write(row,5,follower["html_url"])
    ws.write(row,6,follower["followers_url"])
    ws.write(row,7,follower["following_url"])
    ws.write(row,8,follower["gists_url"])
    ws.write(row,9,follower["starred_url"])
    ws.write(row,10,follower["subscriptions_url"])
    ws.write(row,11,follower["organizations_url"])
    ws.write(row,12,follower["respos_url"])
    ws.write(row,13,follower["events_url"])
    ws.write(row,14,follower["received_events_url"])
    ws.write(row,15,follower["type"])
    ws.write(row,16,follower["site_admin"])


w.save('followers.xls')
