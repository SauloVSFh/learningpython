import random

n = int(input("Enter how many charactors you want in youw password: "))
s = int(input("From 1 to 3, enter the strengh you want of your password: "))
while s<0 or s>3:
	print("Enter a number from 1 to 3")
	
list = ["abacaxi","caramelo","morango","chocolate","macarrão"]

if s == 1:
	pn = random.sample(list,1)
	for i in pn:
		pw = pn[0:n]
	print("Your password is: ",pw)
elif s == 2:
	pn = "".join(random.sample(list,2))
	for i in pn:
		pw = pn[0:n]
	print("Your password is: ",pw)
else:
	numbers = []
	for i in range(9):
		numbers.append(i)
	#list of characters
	char = []
	alpha = "a"
	for i in range(0,26):
		char.append(alpha)
		alpha = chr(ord(alpha)+1)
	#list of Uppercase
	CHAR = []
	alpha = "A"
	for i in range(0,26): #strings sre unicodes. Which means that any str is represented by a 4-byte number
		CHAR.append(alpha)
		alpha = chr(ord(alpha)+1)
	#list of special chr
	special = ["!","@","#","$","%","¨","&","*"]
	#password generator
	final = char + CHAR + special + numbers
	final2=[]
	for i in range(0,n):
		guide = random.randint(0,len(final)-1)
		final2.append(final[guide])		
	pw = ''.join(final2)
	print("Your password is: ",pw)
	
#https://pynative.com/python-generate-random-string/
		
	

