import requests
r = requests.get ('https://xkcd.com/353/')
#print (r)  # <Response [200]>
#print (dir(r)) #it shows the  attributes and methods within the response object
#print(help(r)) #detailed explanation of each function within the library requests

#to get the information in unicodes, in other words, texts:
print(r.text)
