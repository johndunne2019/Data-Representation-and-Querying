# pip install PyGithub on command line
# done successful

from github import Github
import requests

# remove the minus sign from the key
# you can add this to your code just don't commit it
# or use an API key to your own repo
g = Github("7aa146eafee094d3a7b1e81aa1d8fcb0eec8b91-0")

# for repo in g.get_user().get_repos():
    #print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    #print(dir(repo))

# Get the clone url of the repository 
repo = g.get_repo("datarepresentationstudent/aPrivateOne")
#print(repo.clone_url)

# Get the download url in a file test.txt
fileInfo = repo.get_contents("test.txt")
urlOfFile = fileInfo.download_url
#print (urlOfFile)

# Use the download_url to make a http request to the file can output the contents of the file 
response = requests.get(urlOfFile)
contentOfFile = response.text
#print (contentOfFile)

# Append the text more stuff (with a newline character) to the contents of the file
newContents = contentOfFile + " more stuff \n"
print (newContents)

# . Update the contents of the file on git up by using the function 
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)