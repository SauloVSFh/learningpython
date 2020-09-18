import random
x = random.randint(1,9)
count = 0


while True:

    guess = int(input("Please, pick one random number 1 and 9, including the both of them: "))
    dif = x - guess
    
    count += 1
    if dif==0:
        print("You've guessed the number, and it took you ",count," tries!")
        break		
    elif dif>0:
        print("Too low!")
        if str(input("Do you want to play again: y or n?")) == "y":
            continue
        else:
            print("game over! You tried ",count," times!")
            break
    elif dif<0:
        print("Too high!")
        if str(input("Do you want to play again: y or n?")) == "y":
            continue
        else:
            print("game over! You tried ",count," times!")
            break
   
