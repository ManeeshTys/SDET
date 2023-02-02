import datetime
import sqlite3

from utils.configuration import getConnection
print(sqlite3.version)
# Connect to a database (or create one if it doesn't exist)
conn = getConnection()

# Create a cursor object
c = conn.cursor()

# Delete the table if it already exists
c.execute("DROP TABLE IF EXISTS CustomerInfo")

# Execute a query to create a table
c.execute('''CREATE TABLE CustomerInfo
             (CourseName text PRIMARY KEY, 
             PurchasedDate date, 
             Amount integer,
             Location text)''')

data = [("selenium",datetime.date.today(),120,'Africa'),("Protractor",datetime.date.today(),45,'Africa'),('Appium',datetime.date.today(),99,'Asia'),('WebServices',datetime.date.today(),21,'Asia'),
        ("Jmeter",datetime.date.today(),76,'Asia')]
c.executemany("""INSERT INTO CustomerInfo(CourseName,PurchasedDate,Amount,Location) 
                    values(?, ?, ?, ?)""", data)

c.execute("UPDATE CustomerInfo SET Location = 'INK' WHERE CourseName = 'Jmeter'")
c.execute("SELECT * FROM CustomerInfo")
#row = c.fetchone()
rowAll = c.fetchall()
# Commit the changes and close the connection
conn.commit()
conn.close()
#print(row)
print(rowAll)
# file = open('resources\queries.txt', 'r')
# lines = file.readlines()
# for line in lines:
#     if line == '\n':
#         del line
#     else:
#         print(line)