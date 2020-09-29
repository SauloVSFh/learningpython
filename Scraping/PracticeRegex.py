import re


def findmystring(string,mylist):
    with open("regexbase.txt") as fr:
        for line in fr:
            line = line.rstrip()
            x = re.findall(string,line)
            if len(x) != 1 : continue
            mylist.append(line)
        return mylist
        # for item in mylist:
        #     print(item)

#call the function and the name of list you want
#define what to find
stuff = list()
findmystring(string = "[\w\s]+\:\s\d+\.\d{4}", mylist = stuff)
# for item in stuff:
#     print(item)
count = 0
for item in stuff:
    if item.startswith("X-DSPAM-Confidence:"):
        count += 1
print (count)
