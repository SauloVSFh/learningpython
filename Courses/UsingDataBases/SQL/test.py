import sqlite3

conn = sqlite3.connect("OWNdatabase.sqlite3")
cur = conn.cursor()

cur.execute("SELECT * FROM Cities WHERE Name = ? LIMIT 1", ('Sampa',))
cur.execute('UPDATE Cities SET Name = ? WHERE Name = ?', ("São Paulo", "Sampa"))
conn.commit()
conn.close()
