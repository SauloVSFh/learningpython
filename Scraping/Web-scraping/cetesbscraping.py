import requests
from bs4 import BeautifulSoup


url = 'https://cetesb.sp.gov.br/areas-contaminadas/relacao-de-areas-contaminadas/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

table = soup.find('table').find('tr')
links = table.find_all('a')
infodict = dict()
for elem in links:
    link = elem.get("href")
    name = elem.text
    infodict[name] = link

print(infodict)

# I still lack the ability to parse thrugh pdf. Check that in the future
# import io
# import PyPDF2 as pp

# response = requests.get(infodict["– Áreas em processo de remediação"])
# with io.BytesIO(response.content) as f:
#     pdf = pp.PdfFileReader(f)
#     print (pdf.numPages)
