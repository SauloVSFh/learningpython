import re

stuff = list()
def miningfloats(number):

    with open("regexbase.txt") as fr:
        for line in fr:
            line = line.rstrip()
            x = re.findall(number,line)
            if len(x) != 1 : continue
            spamconfidence = float(x[0])
            stuff.append(spamconfidence)
    return stuff
#regex does not function twice within the same with statement
def miningwords(word):
    stuff = list()
    with open("regexbase.txt") as fr:
        for line in fr:
            line = line.rstrip()
            x = re.findall(word,line)
            if len(x) != 1 : continue
            stuff.append(x[0])
    return stuff

author = miningwords("^Author: (.+)")
spam = miningfloats('X-DSPAM-Confidence: ([0-9.]+)')
mydict = dict()
for i in range(len(author)):
        mydict[author[i]] = (spam[i])

print ("The Spam confidence from the lowest to the highest is:\n", sorted([(v,k) for k,v in mydict.items()],))
