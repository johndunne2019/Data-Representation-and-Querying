import mysql.connector 

# create a class 
class BookDAO:
    # db variable to store the database connection
    db  = ""
    # function that initialises the  connection to db
    def __init__(self):
        # should be read from a configuration file in production environment 
        self.db = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'datarepresentation'
        )
        #print("connection made")

    # function to create data in the database table
    # function takes in book which is a a JSON object
    def create(self, book):
        cursor = self.db.cursor()
        # if using an auto increment id this code will be different, look at student files
        sql = "insert into books (ISBN, title, author, price) values (%s, %s, %s, %s)"
        values = [
                book['ISBN'],
                book['title'],
                book['author'],
                book['price']
                ]
        cursor.execute(sql, values)
        self.db.commit()
        return cursor.lastrowid

    # function to return everything from the database
    def getAll(self):
        cursor = self.db.cursor()
        sql = 'select * from books'
        cursor.execute(sql)
        # fetch all returns everything in tuples, 
        results = cursor.fetchall()
        returnArray = []
        print(results)
        # we need to return as dict objects that can be converted to JSON objects
        # convertToDict function used to do this
        for result in results:
            resultAsDict = self.convertToDict(result)
            returnArray.append(resultAsDict)

        # array of dict objects should be returned
        return returnArray

    # function to return just one book from the database
    def findById(self, ISBN):
        cursor = self.db.cursor()
        sql="select * from books where ISBN = %s"
        values = [ISBN]
        cursor.execute(sql, values)
        result = cursor.fetchone()
        # return to dict object
        return self.convertToDict(result)

    # function to update data in the table
    def update(self, book):
        cursor = self.db.cursor()
        sql = "update books set title = %s, author = %s, price = %s where ISBN = %s"
        # values in array below must be in same order as sql command above
        values = [
                book['title'],
                book['author'],
                book['price'],
                book['ISBN']
                ]
        cursor.execute(sql, values)
        self.db.commit()
        return book

    # function to delete from database table
    def delete(self, ISBN):
        cursor = self.db.cursor()
        sql="delete from books where ISBN = %s"
        values = [ISBN]
        cursor.execute(sql, values)
      
        return {}


    # function to convert tuple to dict for getAll, meaning the output can be sent straight to html file later on
    def convertToDict(self,result):
        # columns names should be in same order as they appear in database table 
        colnames = ['ISBN', 'title', 'author', 'price']
        book = {}

        if result:
            for i, colName in enumerate(colnames):
                value = result[i]
                book[colName] = value 
        return book


# make a new instance of the Book DAO class to be imported to the test BookDAO file
bookDao = BookDAO()