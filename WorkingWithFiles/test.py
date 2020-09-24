def filetolist(file):
    listoutput = list()
    with open(file) as fr:
        for line in fr:
            listoutput.append(int(line.strip()))
        return listoutput

primelist = filetolist("primenumbers.txt")
happylist = filetolist("happynumbers.txt")

print(primelist)
print(happylist)
overlaplist = [n for n in primelist if n in happylist]

print(overlaplist)
