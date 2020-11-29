import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="datarepresentation"
)

mycursor = mydb.cursor()
sql="CREATE TABLE books (ISBN int PRIMARY KEY, title varchar(250), author varchar(250), price int)"

mycursor.execute(sql)