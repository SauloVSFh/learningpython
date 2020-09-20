def countnames():
    with open ("readfromfile1.txt") as base:
        namesdict = {} #dictionaries are the best option when you need to understand and element by a number.
        for line in base:
            line = line.strip()
            if line in namesdict:
                namesdict[line] += 1
            else:
                namesdict[line] = 1
        return namesdict

print(countnames())

def countnames2():
    with open ("readfromfile1.txt") as base:
        namesdict2 = {} #dictionaries are the best option when you need to understand and element by a number.
        for line in base:
            name = line.strip()
            namesdict2[name] = namesdict2.get(name,0) + 1 #the get method gets the key assigned to name and adds one. If there's no name in the dic, the default is set 0
        return namesdict2

print(countnames2())    
