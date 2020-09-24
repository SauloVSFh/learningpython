print("Choose an upper limit to your prime numbers sequence: ")
n = input()
try:
    n = int(n)
except:
    n = 1000
#function to get the list of prime numbers
def primegen(n):
    primes = [2]
    for i in range(3,n):
        isPrime = True
        for number in range(2,i):
            if i % number == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)
    return (primes)
    with open("primenumbers.txt",w+) as fw:
        for number in primes:
            fw.write(number, "\n") #ok
print(primegen(n))
#getting the happy numbers
print("Now choose an upper limit to your happy numbers sequence: ")
m = input()
try:
    m = int(m)
except:
    m = 1000
#function to calculate the square of each digit
def squarehappy(anynumber): #ok
#function to check if it's a happy number
def happygen(m): #the while loop doesn't break
    happy = [1]
    for i in range (2,(m+1)):
        possiblehappy = i
        isHappy = True
        while isHappy:
            it = squarehappy(i)
            if it == possiblehappy:
                isHappy = False
                break
            if it == 1:
                break
            if it != 1:
                i = squarehappy(i)
                continue
            if it < 1:
                break
        if isHappy:
            happy.append(possiblehappy)
    return happy
    #create a file
    with open("happynumbers.txt",w+) as fw:
        for number in happy:
            fw.write(number, "\n")
#bridge the two files
def filetolist(file):
    listoutput = list()
    with open(file) as fr:
        line = fr.readline()
        while line:
                listoutput.append(line.strip())
                line = fr.readline()
    return listoutput

primelist = filetolist("primenumbers.txt")
happylist = filetolist("happynumbers.txt")

overlaplist = [n for n in primelist if n in happylist]

print(overlaplist)
