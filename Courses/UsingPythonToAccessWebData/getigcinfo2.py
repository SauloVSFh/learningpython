#that's my program to scrape a internet-based table and create a txt file to be imported as csv.

import requests
from bs4 import BeautifulSoup

r = requests.get("http://igc.usp.br/gsa/corpo-docente-gsa/")
soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find_all('table')
tbody0 = table[0].find('tbody') #There is no way to parse in find_all elements. It is a list of lists. Need to slice the list.
tbody2 = table[2].find('tbody')

info = list()
for tr in tbody0.find_all('tr'): #first get into the table rows because if I go straigh to the cell it won't work
    name = tr.find_all('td')[0].text.strip() #find_all returns a bs4 element that's actually a list
    mail = tr.find_all('td')[1].text.strip()
    phone = tr.find_all('td')[2].text.strip()
    link = tr.find_all('td')[3].find('a').get('href') #get method always work to search with html
    info.append((name, mail, phone, link))
for tr in tbody2.find_all('tr'): #first get into the table rows because if I go straigh to the cell it won't work
    name = tr.find_all('td')[0].text.strip() #find_all returns a bs4 element that's actually a list
    mail = tr.find_all('td')[1].text.strip()
    phone = tr.find_all('td')[2].text.strip()
    link = tr.find_all('td')[3].find('a').get('href') #get method always work to search with html
    info.append((name, mail, phone, link))

igcinfo = tuple(info)

with open("igcinfo.txt",'w+') as fw:
    for item in igcinfo:
        for var in item:
            fw.write(var + ";")
        fw.write("\n")
