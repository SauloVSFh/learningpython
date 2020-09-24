import requests
from bs4 import BeautifulSoup

baseurl = "https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(baseurl) #response object called page that can be read through python
soup = BeautifulSoup(r.text, 'lxml')

all_p_cn_text_body = soup.select("div.grid--item body body__container article__body grid-layout__content > p")
for elem in all_p_cn_text_body:
    print(elem.text)
