import random
import string

number = random.randint(1000,9999)
num = list(str(number))
print(num)

count = 0

while True:
    oi = input("Try a 4 digit number or type exit to leave: ")
    inp = list(str(oi))
    if oi == 'exit':
        print("Game over. Your number of attempts is: ", count)
        break
    count += 1
    if num == inp:
        print("You've made it! Game over. Your number of attempts is: ", count)
        break
    cow = 0
    bull = 0
    for i in range(len(num)):
        if num[i] == inp[i]:
            cow += 1
        else:
            if inp[i] in num:
                bull += 1
    print("You've got: ", cow ,"cows, and ", bull ,"bulls")
    continue
