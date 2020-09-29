import re

string = 'https://[\w\?\&/]+'
stuff = list()
with open("regexbase.txt") as fr:
    for line in fr:
        line = line.rstrip()
        x = re.findall(string,line)
        if len(x) != 1 : continue
        toprint = (x[0])
        stuff.append(toprint)

print (toprint)
