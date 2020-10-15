import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy

#Operadores:

#print(10**3) # + - * / ()

#print(10//3)# divisão interira

#print(26 % 7)# resto da divisão



#funções

data=np.round(np.random.rand(10)*100,1)

#print(data)

data=data.astype('int')

print(data)


# Muitas operações podem ser feitas com índices

dataB=np.copy(data)
dataB[dataB>30]= dataB[dataB>30]*2 #comparativos: ==  !=   <   >   <=   >=    
print(dataB,'\n')



#Loops para operações mais complexas

dataC=np.copy(data)

print('\nFor loop:')

A=0

for i in dataC:

	A= A+ (i**2+34)/10
	print('i=',i,',A=',A)

A=0
cont=0
As=[]

#Ou, de forma equivalente:

print('\nWhile loop:')

while cont < len(dataC):
	
	A= A+ (dataC[cont]**2+34)/10
	As=np.append(As,A)
	print('dataC[cont]=',dataC[cont],',A=',A)
	cont+=1

print(As)


#condicionais

print('\nIf:')
for i in dataC:

	if i >30: # outros comparativos: ==  !=   >   <=   >=   
		A= A+ (i**2+34)/10
		print('i=',i,',A=',A)

	elif i<15:
		
		print('<15')

	else:

		print('não')


print('\nIf_and_:')
for i in dataC:

	if i>30 and i<70: #outros operadores lógicos: or  not
		A= A+ (i**2+34)/10
		print('i=',i,',A=',A)

	else:

		print('não')


#definindo uma função

def My_func(vect,b,c): #array,integer,integer
	
	X=[]
	for i in vect:
		x=(i**b)/c
		X=np.append(X,x)
	return(X)

k= My_func(data,2,4)

print("\nk ",k)
	

#várias funções podem ser salvas em um arquivo .py e carregadas como um módulo de funções no início.

#pode-se estrutura o código em funções e usar funções em loops tb. Fica tudo mais fácil em códigos grandes.



