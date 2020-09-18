#Exercise 5 and 10
 a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
 c = []
 
 for i in a:
	for j in b:
		if i == j:
			list(set(c))

#second way

for i in a:
	for j in b:
		if == j:
			c=list(dict.fromkeys(c))
print(c)

#third way
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=[i for i in a for j in b if i==j]
[d.append(x) for x in c if x not in d]
print(d)

#fourth way
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
c=list(set(i for i in a if i in b))
print(c)