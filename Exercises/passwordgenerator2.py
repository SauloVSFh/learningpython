#Password generator

import random
import string


n = int(input("Enter how many charactors you want in youw password: "))
s = int(input("From 1 to 3, enter the strengh you want of your password: "))
while s<0 or s>3:
	print("Enter a number from 1 to 3")
	
list = ["abacaxi","caramelo","morango","chocolate","macarrão"]

if s == 1:
	pn = random.sample(list,1)
	for i in pn:
		pw = pn[0:n]
	print("Your password is: :", pw)
elif s == 2:
	pn = random.sample(list,2)
	pn2 = pn[0] + pn[1]
	for i in pn2:
		pw = pn2[0:n]
	print("Your password is: :", pw)
else:
	base = string.printable
	pn = random.sample(base,n)
	pw = "".join(pn)
	print("Your password is: :", pw)

	

	
	
