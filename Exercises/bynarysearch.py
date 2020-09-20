import random

num = int(input("Please, enter a number from 1 to 10 and we'll check if it's on the list."))

def bynarysearch(num):
    numbers = sorted(random.sample(range(1,10),5))
    if num in numbers:
        return True
    else:
        return False

print(bynarysearch(num))
