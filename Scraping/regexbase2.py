import re

string = "\(?(https?://[^\)$]\S+)\)?"
# string = "(https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|www\.[a-zA-Z0-9][a-zA-Z0-9-]+[a-zA-Z0-9]\.[^\s]{2,}|https?:\/\/(?:www\.|(?!www))[a-zA-Z0-9]+\.[^\s]{2,}|www\.[a-zA-Z0-9]+\.[^\s]{2,})"

stuff = list()
with open("regexbase.txt") as fr:
    for line in fr:
        line = line.rstrip()
        x = re.findall(string,line)
        if len(x) != 1 : continue
        if x[0].startswith('https://collab'):
            y = re.findall('(https://[\w\.\/]+)',x[0])
            stuff.append(y[0])
        else :  stuff.append(x[0])

for item in stuff:
    print(item)
