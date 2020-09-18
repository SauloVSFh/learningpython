w = input(str("Please, type a phrase you want that I'll reverse it backwards: "))

def rev(w):
	l = w.split( )
	l1 = []
	for i in l:
		l1.insert(0,i)
	print(" ".join(l1))
	
rev(w)
	
#without using split

x = str(input("Please enter a phrase you want to reverse: "))

def wr (x):
	l = x.split(" ")
	i = len(l) - 1
	z=[]
	while i >= 0:
		z.append(l[i])
		i += (-1)
	print(z)
	
wr(x)