# steps to create a virtual environment 
# open cmder and cd to appropriate directory
# python -m venv venv
# create a .gitignore file and add venv/
# .\venv\Scripts\activate.bat
# pip freeze to see what packages are installed (should be none)
# pip install flask
# pip freeze > requirements.txt to send the list of packages installed to a text file
# run rest server in the newly created VM
# python rest_server.py
# copy and paste the local host to chrome 
# open a new console to do CURL requests

# first create and test the app route for each method, get, get all, create, update and delete 
# test in browser and with curl calls
# when all tested move on to writing the code for each function
# not linking to a database in this case, an array of books is created instead

from flask import Flask, url_for, request, redirect, abort, jsonify

app = Flask(__name__, static_url_path='', static_folder='staticpages')

# array of books created
books=[
    {"id": 1, "Title": "Harry Potter", "Author": "JK", "Price": 1000},
    {"id": 2, "Title": "some cook book", "Author": "Mr Angry Man", "Price": 2000},
    {"id": 3, "Title": "Python made easy", "Author": "Some Liar", "Price": 1500}
]
# to be incremented when creating a new book
nextId=4

# http://127.0.0.1:5000/ in browser or curl http://127.0.0.1:5000/
@app.route('/')
def index():
    return "hello"

# get all
# get method, no need to specify its a get as it defaults to get
# http://127.0.0.1:5000/books in browser or curl http://127.0.0.1:5000/books
@app.route('/books')
def getUser():
    #return "hello"
    return jsonify(books)

# find by id
# could re use this code for project if ID is unique identifier 
# http://127.0.0.1:5000/books/123 in browser or curl http://127.0.0.1:5000/books/123
@app.route('/books/<int:id>')
def findById(id):
    #return "server by find by id with " + str(id)
    foundBooks = list(filter (lambda t : t["id"]== id, books))
    # if nothing found return an empty book
    if len(foundBooks) == 0:
        return jsonify({}) , 204
    return jsonify(foundBooks[0])

# create
# cant use browser to test as browsers only do gets
# curl -X "POST" http://127.0.0.1:5000/books
# note single quotes not allowed in curl post request

# we need to pass up some data example below:
# curl -X POST -H "content-type:application/json" -d "{\"Title\":\"test\", \"Author\":\"some guy\", \"Price\":123}" http://127.0.0.1:5000/books
@app.route('/books', methods=['POST'])
def create():
    #return "served by Create "
    global nextId
    # if there isnt any json in the request
    if not request.json:
        abort(400)
    
    # make a new book with the data passed in curl request
    book = {
        "id": nextId,
        "Title": request.json["Title"],
        "Author": request.json["Author"],
        "Price": request.json["Price"]
    }

    books.append(book)
    nextId += 1
    return jsonify(book)

    #return "served by Create "

# update
# curl -X PUT http://127.0.0.1:5000/books/123
# curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
   #return "server by update with " + str(id)
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    currentBook = foundBooks[0]
    # if title in request update the title etc.
    if 'Title' in request.json:
        currentBook['Title'] = request.json['Title']
    if 'Author' in request.json:
        currentBook['Author'] = request.json['Author']
    if 'Price' in request.json:
        currentBook['Price'] = request.json['Price']

    return jsonify(currentBook)

# delete
# curl -X DELETE http://127.0.0.1:5000/books/123
# curl -X DELETE http://127.0.0.1:5000/books/1
# book will only be deleted when server is running 
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    #return "server by delete with " + str(id)
    foundBooks = list(filter(lambda t: t["id"] == id, books))
    if len(foundBooks) == 0:
        return jsonify({}), 404
    books.remove(foundBooks[0])

    return jsonify({"done":True})


if __name__ == "__main__":
    app.run(debug=True)