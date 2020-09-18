#https://www.practicepython.org/solution/2014/04/02/08-rock-paper-scissors-solutions.html
#2 forms of making this: traditional if statements or by using dictionaries
p1=input("P1, choose between rock, paper and scissors?")
p2=input("P2, please choose between rock, paper and scissors?")


#checking inputs
check=["rock","paper","scissors"]
if p1 in check:
    print("P1 has chosen: " + p1)
else:
    p1=input("Type it again, P1: rock, paper os scissors?")
if p2 in check:
    print("P2 has chosen: " + p2)
else:
    p2=input("Type it again, p2: rock, paper os scissors?")  

#function           
def game(p1,p2):
    if p1==p2:
        print("it's a tie")
    elif p1 == "rock":
		if p2 == "paper":
			print("P2 has won")
		else:
			print ("P1 has won")
	elif p1 == "paper":
		if p2 == "rock":
			print("P1 has won")
		else:
			print ("P2 has won")
	elif p1== "scissors":
		if p2 == "rock"
			print ("p2 has won")
	sys.exit()
	
print(game(p1,p2))




#Other way of doing the same exercise:

print("Please, choose between rock, scissors and paper. Do not use caps lock")

#It means that while the idented expressions are true, the while will keep on looping

while True:

	dict = {"rock":1,"scissors":2,"paper":3}
	check=["rock","paper","scissors"]
	pa=str(input("Player a: "))
	pb=str(input("Player b: "))

#checking inputs
	if pa in check:
		print("P1 has chosen: " + pa)
	else:
		pa=input("Type it again, P1: rock, paper os scissors?")
	if pb in check:
		print("P2 has chosen: " + pb)
	else:
		pb=input("Type it again, p2: rock, paper os scissors?")  
        
#dictionaries
	a = dict[pa]
	b = dict[pb]
	dif = a - b 


#conditionals
	if dif in [-1,2]:
		print("Player a has won!")
		if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
			continue
		else:
			print("game over!")
		break
	elif dif in [1,-2]:
		print("Player b has won!")
		if str(input('Do you want to play another game, yes or no?\n')) == 'yes':
			continue
		else:
			print("game over!")
	else:
		print("It's a tie!")
		continue
	sys.exit()

	