#Fibonacci numbers	

n=int(input("How many Fibonacci numbers would you like to appreciate? "))

def fibo(n):
	if n == 0:
		print("It seems you don't want a Fibonacci sequence.")
	elif n == 1:
		l=[1]
		print("The Fibonacci sequence is equal to: ", l,".")
	elif n == 2:
		l=[1,1]
		print("The Fibonacci sequence is equal to: ", l,".")
	elif n > 2:
		i=1
		l = [1,1]
		while i < (n-1): #sums till the last but one
			l.append(l[i]+l[i-1])
			i += 1
		print("Your list of Fibonacci numbers is: ",l,"!")
fibo(n)	

