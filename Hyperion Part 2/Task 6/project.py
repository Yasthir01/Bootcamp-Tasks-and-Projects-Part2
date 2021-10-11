import sqlite3



def enter_book():
	"""Enters in a new book into the database"""
	book_id = input("Enter the ID of the book: ")
	title = input("Enter the title of the book: ")
	author = input("Enter the author of the book: ")
	qty = input("Enter the quantity: ")

	cursor.execute("""INSERT INTO books(id, title, author, qty) values(?, ?, ?, ?)""",\
					(book_id, title, author, qty))
	db.commit()


def update_book():
	"""Updates the quantity of an existing book"""
	book_id = input("Enter the ID of the book to update: ")
	qty = input("Enter the new quantity: ")
	cursor.execute("""UPDATE books SET qty = qty WHERE id = book_id""")
	db.commit()


def delete_book():
	"""Deletes a book from the database"""
	book_id = input("Enter the ID of the book you want to DELETE: ")
	cursor.execute("""DELETE FROM books WHERE id = book_id""")
	db.commit()


def search_book():
	"""Uses the author name to search for a book"""
	author = input("Enter the name of the author: ")
	cursor.execute("""SELECT * FROM books WHERE author LIKE ?""", (author))
	results = cursor.fetchall()
	print(results)






# create a connection
db = sqlite3.connect('ebookstore.db')

# create a cursor
cursor = db.cursor()

# first entry
id1 = 3001
title1 = 'A Tale of Two Cities'
author1 = 'Charles Dickens'
qty1 = 30

# second entry
id2 = 3002
title2 = 'Harry Potter and the Philosophers Stone'
author2 = 'J.K Rowling'
qty2 = 40

# third entry
id3 = 3003
title3 = 'The Lion, the Witch and the Wardrobe'
author3 = 'C.S Lewis'
qty3 = 25

# fourth entry
id4 = 3004
title4 = 'The Lord of the Rings'
author4 = 'J.R.R Tolkien'
qty4 = 37

# fifth entry
id5 = 3005
title5 = 'Alice in Wonderland'
author5 = 'Lewis Caroll'
qty5 = 12

# create a table
cursor.execute("""CREATE TABLE IF NOT EXISTS books
				(id INTEGER PRIMARY KEY,
				title varchar(255),
				author varchar(30),
				qty INTEGER)""")

entries = [(id1, title1, author1, qty1), (id2, title2, author2, qty2), (id3, title3, author3, qty3), \
			(id4, title4, author4, qty4), (id5, title5, author5, qty5)]

# insert the entries into the table 
cursor.executemany("""INSERT INTO books (id, Title, Author, Qty)
					VALUES (?, ?, ?, ?)""", entries)


# test to see if everything got stored correctly
# cursor.execute("""SELECT * FROM books""")
# testing = cursor.fetchall()
# print(testing)


# have a menu that will display the options of actions to take
while True:
	option = input("1. Enter new book\n2. Update book\n3. Delete book\n4. Search book\n0. Exit")
	if option == '1':
		enter_book()
	elif option == '2':
		update_book()
	elif option == '3':
		delete_book()
	elif option == '4':
		search_book()
	elif option == '0':
		break
	else:
		print("Invalid Input")



db.close()