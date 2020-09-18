#parsing strings
#Retrieve "uct.ac.za"
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
n=data.find("@")
n1=data.find(" ",n)
st=data[n+1:n1]
print("what you're lookinf for is this email: ", st)
