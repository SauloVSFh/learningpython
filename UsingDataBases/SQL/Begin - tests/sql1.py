import sqlite3

connect = sqlite3.connect('Country.sqlite') #connecting to something that whether exists or will be created
cur = connect.cursor() #cursor function is similar to the open or the read function

#sql commands come in form of strings by means of the execute function
#Execute is the function to pass in SQL commands
cur.execute ("DROP TABLE IF EXISTS States") #It deletes the table States so it can be created again
cur.execute ("CREATE TABLE States (Name, Population)")

connect.close()
