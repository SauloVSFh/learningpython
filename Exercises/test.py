x = 'X-DSPAM-Confidence:0.8475'
begin = x.find(":")
print(begin)	
y = float(x[begin+1:])
print(y)