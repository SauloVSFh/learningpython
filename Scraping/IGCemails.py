import re

with open("igc.txt",'r') as fr:
    for line in fr:
        line = line.rstrip()
        names = re.findall("(.*) \S+@\S+",line)
        emails = re.findall("\S+@\S+",line)
        numbers = re.findall('\S+-\S+',line)
    print(emails)    
    #for i in range(len(emails)):
        #print (emails[i], numbers [i], names [i])
