def duprem1(x):
	l=[]
	for i in x:
		if i not in l:
			l.append(i)
	return l

def duprem2(a):
	return list(set(a))

def duprem3(x):
	l=[i for i in x if i not in l]
	



