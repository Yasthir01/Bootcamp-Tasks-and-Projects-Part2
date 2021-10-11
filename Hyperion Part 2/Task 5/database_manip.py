import sqlite3


# create a connection
db = sqlite3.connect('student_db')

# create a cursor
cursor = db.cursor()

# first person
id1 = 55
name1 = 'Carl Davis'
grade1 = 61

# second person
id2 = 66
name2 = 'Dennis Fredrickson'
grade2 = 88

# third person
id3 = 77
name3 = 'Jane Richards'
grade3 = 78

# fourth person
id4 = 12
name4 = 'Peyton Sawyer'
grade4 = 45

# fifth person
id5 = 2
name5 = 'Lucas Brooke'
grade5 = 99

# create a table
cursor.execute("""CREATE TABLE python_programming 
				(id INTEGER, 
				name TEXT, 
				grade INTEGER)""")


people_ = [(id1, name1, grade1), (id2, name2, grade2), (id3, name3, grade3), (id4, name4, grade4), (id5, name5, grade5)]

# insert data
cursor.executemany("""INSERT INTO python_programming (id, name, grade) 
				VALUES(?, ?, ?)""", people_)


# Select all records with a grade between 60 and 80
cursor.execute("""SELECT * FROM python_programming 
				WHERE grade BETWEEN 60 AND 80""")

sixty_eighty = cursor.fetchall()
print(sixty_eighty)


# Change Carl Davis’s grade to 65.
cursor.execute("""UPDATE python_programming SET grade = 65 WHERE id = 55""")


# Delete Dennis Fredrickson’s row.
cursor.execute("""DELETE FROM python_programming WHERE id = 66""")


# Change the grade of all people with an id below than 55.
cursor.execute("""UPDATE python_programming SET grade = 60 WHERE grade < 55""")


# have a look at the final result
cursor.execute("""SELECT * FROM python_programming""")
everything = cursor.fetchall()
print(everything)



db.commit()
db.close()
