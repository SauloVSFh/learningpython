import re

stuff = list()
spam = list()
fr = open("regexbase.txt")
for line in fr:
    line = line.rstrip()
    x = re.findall("^Author: (.+)",line)
    if len(x) != 1 : continue
    stuff.append(x)
print(stuff)

for line in fr:
    line = line.rstrip()
    x = re.findall("X-DSPAM-Confidence: ([0-9.]+)",line)
    if len(x) != 1 : continue
    spamconfidence = float(x[0])
    spam.append(spamconfidence)
