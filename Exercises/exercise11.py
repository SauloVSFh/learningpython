n = int(input("Please, enter a number and we'll tell you if it's prime: "))

def function(n):
	if n == 1:
		print("You've chosen 1.")
	else:
		a = range(2,n)
		b=[]
		[b.append(i) for i in a if n%i==0]
		if len(b) > 0:
			print("The number you've chosen isn't prime and the list of divisors is: ",b,".")
		else:
			print("You've picked a prime number!")
		
function(n)

	