#Web scraping
import requests
from bs4 import BeautifulSoup

baseurl = "https://www.nytimes.com/"
r = requests.get(baseurl) #response object called page that can be read through python
soup = BeautifulSoup(r.text, 'lxml') #it returns all the text we need to recode the page
# The website use differents h2 class, so the first step would be getting every h2 class in the first place to map how we can acess it
#h2 class= 'css-189ztlo e1voiwpg1' h2 class= 'css-1vvhd4r e1voiwgp0' h2 class= 'css-14byr0y e1voiwgp0'

#for heading in soup.find_all(class_= 'css-1vvhd4r e1voiwgp0'): # soup find all returns a list of information.
    #headlines = heading.span.text.replace("n/", " ").strip() #the dots narrow the variable of interest within the idented information
    #after I use the string methods to replace the empty line by spaces and strip the excessive spaces
    #print(headlines)

headslist = soup.find_all('h2') #no need to use class in here. I'm just looking for the headlines
heads = []
for i in headslist:
    heads.append(i.text.rstrip("\n").strip())
print(type(heads))

#to write this into a txt:
with open("NYheadlines.txt",'w+') as txt:
    for i in heads:
        txt.write(i+'\n')
with open('NYheadlines.txt','r') as txt1:
    for line in txt1:
        print (line)






#print (soup.prettify()) #print soup the html file is not idented. prettify does that .

#match = soup.title()

#match1 = soup.title.text #it prints the text within the tags only
#print (match1)

#match = soup.div # it prints the first div tag as whole

#better parser is soup.find()
#match = soup.find('span', class_='balancedHeadline') # it allows to insert class in the function. This line gets the first div class = footer
