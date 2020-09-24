
with open("countword.txt") as f:
    f2 = f.read()
    wordin = f2.split()
    words = [i for i in wordin if i.isalnum()]
    count = dict()
    for word in words:
        count[word] = count.get(word,0) + 1
#count is a dictionary
countreverse = list()
for k,v in count.items(): #not possible to loop straight through dictionaries
    countreverse.append((v,k))
countreverse = sorted(countreverse, reverse=True)
for i in countreverse[:10]:
    print(i)
