with open("countword.txt") as f:
    f2 = f.read()
    wordin = f2.split()
    words = [i for i in wordin if i.isalnum()]

    count = dict()
    for word in words:
        count[word] = count.get(word,0) + 1

#print(count)

#print (count.keys()) #it returns only the keys

#print(count.values()) #to return the values

#print (count.items()) #now we get a list of tupples back

# print with two iteration variables. Easier to check data in dictionaries

#for k,v in count.items(): #only possible transforming it into a list of tupples
    #print (k,v)

#the biggest value within the dictionary
bigword = 0
bigcount = 0
for k,v in count.items():
    if v > bigcount: #it considers the whole domain
        bigcount = v
        bigword = k
print(bigcount, bigword)
#smart way of adressing the same issue. Sort by value. Can use the size of the return list as a variable
countreverse = list()
for k,v in count.items(): #not possible to loop straight through dictionaries
    countreverse.append((v,k))
countreverse = sorted(countreverse, reverse=True)
for i in countreverse[:10]:
    print(i)
#Using lists of comprehension - one line of code
print(sorted([(v,k) for k,v in count.items()], reverse=True)[:10])
