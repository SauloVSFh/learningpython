#parsing strings
#Retrieve "uct.ac.za"
data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
word = data.split()
mail=word[1]
piece = mail.split("@")
print(piece[1])
