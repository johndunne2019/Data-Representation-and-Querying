# import the new instance of the bookDao class from the bookDAO file
from BookDAO import bookDao


book1 = {
    'ISBN': 123456,
    'price': 12,
    'author' : 'jk',
    'title' : 'some fantasy book'

}

book2 = {
    'ISBN': 1234567,
    'price': 999,
    'author' : 'mary',
    'title' : 'had a little lamb'

}

# functions called from BookDAO file

# create book 2 in the datbase table
#returnValue = bookDao.create(book2)
#print(returnValue)

# find By Id
print("Find By Id")
returnValue = bookDao.findById(book2['ISBN'])
print(returnValue)

# update
returnValue = bookDao.update(book1)
print(returnValue)

# find By Id
returnValue = bookDao.findById(book2['ISBN'])
print(returnValue)

# delete
returnValue = bookDao.delete(book2['ISBN'])
print(returnValue)
