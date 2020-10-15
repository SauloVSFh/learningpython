import urllib.request, urllib.parse, urllib.error #alternative to get
from bs4 import BeautifulSoup
import re


hand = urllib.request.urlopen('http://igc.usp.br/gsa/corpo-docente-gsa/').read() #http response
soup = BeautifulSoup(hand, 'html.parser')
mylist = list()
for tr in soup.find_all('tr'):
    mylist = [td.text.strip() for td in soup.find_all("td")]

with open("igcinfo.txt",'w+') as wf:
    for item in mylist:
        wf.write("%s\n" %item)

#still having problems with regex functions. Can't track the names on it
with open("igcinfo.txt",'r') as wf:
    data = wf.read().split()
    mail = [line for line in data if len(re.findall("\S+@\S+", line)) > 0]
    numbers = list()
    names = list()
    for line in data:
        if re.search("\S+@\S+", line) : pass
        if re.search("[0-9]+-+[0-9]+", line) :
            numbers.append(line)
        if re.search('[a-zA-Z]+',line):
            names.append(line)



        if data2 not in mail:
            if data2 not in numbers:
                names.append(data2)
print(names)

for i in range(len(numbers)):
    print(mail[i], " ", numbers[i])
