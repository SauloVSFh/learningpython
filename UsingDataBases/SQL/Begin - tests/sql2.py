import re, sqlite3

connect = sqlite3.connect('emails.sqlite')
cur = connect.cursor()

cur.execute("DROP TABLE IF EXISTS Maillist")
cur.execute("CREATE TABLE Maillist(Name,Email)")

def miningwords(word):
    stuff = list()
    emailsdict = dict()
    with open("regexbase.txt") as fr:
        for line in fr:
            line = line.rstrip()
            mail = re.findall(word,line)
            if len(mail) != 1 : continue
            x = mail[0].find('@')
            name = mail[0][0:(x)]
            emailsdict[name] = mail[0]
    return emailsdict

mail = miningwords("([\w\.]+@[\w\.]+)")
for k,v in mail.items():
    cur.execute("INSERT INTO Maillist (Name,Email) Values (?,?)", (k,v))
    connect.commit()

print('Names:')
cur.execute("SELECT Name, Email FROM Maillist")
for row in cur:
    print(row)
