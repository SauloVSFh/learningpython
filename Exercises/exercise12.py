#Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and makes a new list 
#of only the first and last elements of the given list. For practice, write this code inside a function.

import random

def ls(list):
	list= range(1,9)
	c = [list[0],list[(len(list)-1)]]
	print(c)

ls(list)