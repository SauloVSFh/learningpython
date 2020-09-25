import xml.etree.ElementTree as ET

#later we'll see how to parse xml from the internet
# fr='''<person>
# <name>Chuck</name>
# <phone type="intl">
# +1 734 303 4456
# </phone>
# <email hide="yes" />
# </person>'''
#
# tree = ET.fromstring(fr)
# print("Name is: ", tree.find('name').text)
# print("Phone is: ", tree.find('phone').text.strip(), "and type is: ", tree.find('phone').get('type'))

input = '''
<stuff>
<users>
<user x="2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id>009</id>
<name>Brent</name>
</user>
</users>
</stuff>'''

tree = ET.fromstring(input)
users = tree.findall('users/user') # the trees work as directories!
for tag in users:
    print("name is: ", tag.find("name").text.rstrip(), ", user id is: ", tag.find('id').text.rstrip(), ", user attribute is: ", tag.get('x'))
