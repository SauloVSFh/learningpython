#extract the days of the week out of the mail text in files3.txt

with open("files3.txt") as mail:
    for line in mail:
        if not line.startswith("From") : continue
        pieces = line.split()
        if len(pieces) < 3 : continue
        print(pieces[2])
