import requests
from bs4 import BeautifulSoup
import re

baseurl = "http://igc.usp.br/gsa/corpo-docente-gsa/"
site = requests.get(baseurl)
f = site.read()

print(f)

#for email in re.findall(".+@.+",soup):
#    print (email)
