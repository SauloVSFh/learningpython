x = str(input("Please enter a phrase you want to reverse: "))
print(str.capitalize(x))

def wr (x):
	l = x.split(" ") #l is a list composed by words. Therefore no longer a str sequence. 
	i = len(l) - 1
	z=[]
	while i >= 0:
		z.append(l[i])
		i += (-1)
	print(" ".join(z))
	
wr(x)
