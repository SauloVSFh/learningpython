import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

var_url = urllib.request.urlopen('https://blogs.oracle.com/oraclepartners/database-7/rss')
xmldoc = read(var_url)


for item in xmldoc.find('channel/item'):
    title = item.find('title').text
    date = item.find('pubDate').text
    link = item.find('link').text

    print(title)
    print(date)
    print(link)
