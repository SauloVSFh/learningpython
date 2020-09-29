import re

string = "(https?://[^\)$]\S+)"
stuff = list()
with open("regexbase.txt") as fr:
    for line in fr:
        line = line.rstrip()
        x = re.findall(string,line)
        if len(x) != 1 : continue
        stuff.append(x[0])


for item in stuff:
    print(item)
