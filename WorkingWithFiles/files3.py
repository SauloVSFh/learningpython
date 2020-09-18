#create a program to get information from big Files

#I want info from lines like this X-DSPAM-Confidence:    0.8475
#Number of lines and average of Spam Confidence

from statistics import mean
with open("files3.txt") as file:
#    count = 0
#    for line in file:
#        count += 1
#    print(count) #number of lines
    count1 = 0
    list=[]
    for line in file:
        if line.startswith("X-DSPAM-Confidence"):
            count1 += 1
            list.append(line)
    finallist=[]
    for i in list:
        n1 = i.find(":")
        n2 = i.find("n",n1)
        finallist.append(float(i[n1+2:n2]))
    print("the average of Spam confidence is:", mean(finallist))
