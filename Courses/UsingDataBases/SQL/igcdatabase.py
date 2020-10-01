from bs4 import BeautifulSoup
import requests
import sqlite3

con = sqlite3.connect("IGcContacts.sqlite3")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS GMGContacts")
cur.execute("CREATE TABLE GMGContacts (Name, Email, Phone, Type)")

r = requests.get("http://igc.usp.br/gmg/corpo-docente-gmg/").text
soup = BeautifulSoup(r,'lxml')

tables = soup.find_all('table', attrs={'wp-block-table'})
for table in tables:
    tbodies = soup.find_all('tbody')
    tbody = tbodies[0]
    for tr in tbody:
        td = tr.find_all('td')
        cur.execute("INSERT INTO GMGContacts (Name, Email, Phone, Type) VALUES (?,?,?,?)", (td[0].text, td[1].text, td[2].text, 'Docente'))
    con.commit()
    tbody = tbodies[1]
    for tr in tbody:
        td = tr.find_all('td')
        cur.execute("INSERT INTO GMGContacts (Name, Email, Phone, Type) VALUES (?,?,?,?)", (td[0].text, td[1].text, td[2].text, 'Permissionário'))
    con.commit()


print('Info...')

cur.execute("SELECT Name, Email, Phone, Type FROM GMGContacts")
for row in cur:
    print(row)
