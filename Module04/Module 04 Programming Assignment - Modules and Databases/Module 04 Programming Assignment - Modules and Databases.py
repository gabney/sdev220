"""
Module 04 Programming Assignment - Modules and Databases
SDEV 220 Software Development Using Python
Gabriel Abney

This assignment asks us to complete specific exercises from our textbook \
found at the end of the chapters 11 and 16.  Specifically, the exercises \
11.1 and 11.2 from chapter 11, and 16.8 from chapter 16.

My work for these exercises can be found in the program below.
Additionally, the prompt for each exercise is commented above my work.
"""



# 11.1 Create a file called zoo.py. In it, define a function called hours() \
# that prints the string 'Open 9-5 daily'. Then, use the interactive interpreter \
# to import the zoo module and call its hours() function.

# note: see the additional file in the assignment folder called zoo.py 

#imports zoo package
import zoo

#calls hours function defined in zoo package
zoo.hours()




# 11.2 In the interactive interpreter, import the zoo module as menagerie \
# and call its hours() function.

# imports zoo package as 'menagerie'
import zoo as menagerie

#calls the hours function with the name menagerie
menagerie.hours()




# 16.8 Use the sqlalchemy module to connect to the sqlite3 database books.db \
# that you just made in exercise 16.4. As in 16.6, select and print the title \
# column from the book table in alphabetical order.

# This requires additionally doing exercise 16.4, which is described below:
# 16.4 Use the sqlite3 module to create a SQLite database called books.db and \
# a table called books with these fields: title (text), author (text), and year (integer).

# 16.4 setup for use in 16.8
import sqlite3
conn = sqlite3.connect("books.db")
curs = conn.cursor()
#curs.execute("DROP TABLE books") # in case this program is run again, drops the table to recreate it rather than generating an error
curs.execute("""
             CREATE TABLE books
             (title TEXT,
             author TEXT,
             year INT)
             """)

# populating the table for 16.8
curs.execute("INSERT INTO books VALUES('The Weirdstone of Brisingamen','Alan Garner',1960)")
curs.execute("INSERT INTO books VALUES('Perdido Street Station','China Miéville',2000)")
curs.execute("INSERT INTO books VALUES('Thud!','Terry Pratchett',2005)")
curs.execute("INSERT INTO books VALUES('The Spellman Files','Lisa Lutz',2007)")
curs.execute("INSERT INTO books VALUES('Small Gods','Terry Pratchett',1992)")

# closes the cursor and database connection when done
curs.close()
conn.close()


# this section required installing sqlalchemy library with command 'pip install sqlalchemy' in command prompt

# imports sqlalchemy
import sqlalchemy as sa

# creates a connection to the books database using an sqllite instance
engine = sa.create_engine("sqlite:///books.db", echo = True)

# creates columns using SELECT query and orders them alphabetically
cols = engine.execute("SELECT title FROM books ORDER BY title")

# prints the columns
for col in cols:
    print(col)