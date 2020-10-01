import re, sqlite3

connect = sqlite3.connect('emails.sqlite')
cur = connect.cursor()

cur.execute("DROP TABLE IF EXISTS Countmail")
cur.execute("CREATE TABLE Countmail(Name,Email)")

def miningwords(word):
    countdict = dict()
    mails = list()
    with open("regexbase.txt") as fr:
        for line in fr:
            line = line.rstrip()
            mail = re.findall(word,line)
            if len(mail) != 1 : continue
            mails.append(mail[0])
        for mail in mails:
            countdict[mail] = countdict.get(mail,0) + 1
    return countdict

mail = miningwords("([\w\.]+@[\w\.]+)")
for k,v in mail.items():
    cur.execute("INSERT INTO Countmail (Name,Email) Values (?,?)", (k,v))
    connect.commit()

print('Names:')
cur.execute("SELECT Name, Email FROM Countmail")
for row in cur:
    print(row)


# for k,v in emailsdict.items():
#     output = f'INSERT INTO Users(name,email) VALUES("{k}","{v}")'
#     print(output)
