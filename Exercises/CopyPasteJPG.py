import os

os.chdir("D:\Pictures-videos")
with open("niver.png",'rb') as rbf:
	os.chdir("D:\Programing\Python")
	with open("nivercopy.jpg", 'wb') as wbf:
		chunk = 4096
		rbf1 = rbf.read(chunk)
		while len(rbf1)>0:
			wbf.write(rbf1)
			rbf1 = rbf.read(chunk)
			
		
