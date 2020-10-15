import pandas as pd
from pandas import DataFrame
import numpy as np
from numpy import append
import matplotlib.pyplot as plt
import seaborn as sns


	#TIPOS DE VARIÁVEIS	

H= 'nada'
#print('Tipo de variável',type(H))



	#ESTRUTURAS DE DADOS

ExemploList = [2,3,5,9,2,1]
#print(ExemploList)

ExemploArray = np.array(ExemploList)
#print(ExemploArray)

A=ExemploList * 2
#print(A)

B=ExemploArray * 2
#print(B)




Exemplo2List = [ExemploList,[3,5,4,6,8,7]] # Array com duas linhas, 2 x 6, não dá pra usar append uma nova linha, o número de dimensões já tem que existir
#print(Exemplo2List)

#adicionar uma linha
Exemplo2List = append(Exemplo2List,[[5,4,16,8,7,1],],axis=0) # o adicionado tem que ter o mesmo número de dimensões
#print(Exemplo2List)


#adicionar uma coluna
Exemplo2List = np.append(Exemplo2List,[[10],[23],[50]],axis=1)
#print(Exemplo2List)



	#ÍNDICES

#print(B)
C=B[1:-1]
#print(C)
C2=B[1:]
#print(C2)

Z=np.array([[2,4,5],[3,2,5],[7,9,8],[1,1,1]])

Z2= Z[1,-1]
#print(Z2)

Z3= Z[:-1,1:]
#print(Z3)

	#DATAFRAMES NO PANDAS

data_teste=pd.read_csv('Dados1.csv',skiprows=0,header=0)
#print(data_teste)

#Se o arquivo não tem nome de coluna
dataSeixos=pd.read_csv('Seixos_Rejeito.csv',skiprows=0,header=None)
#print(dataSeixos)
dataSeixos.columns=["Diâmetro"] #é útil dar nome à cada coluna
#print(dataSeixos)
primeiros=['Granito']*100
últimos=['Quartzo_veio']*105
IV=primeiros+últimos
dataSeixos.index=[IV] 
#print(dataSeixos)

C=dataSeixos.Diâmetro * 2
#print(C)

#inserindo uma coluna no dataframe
dataSeixos.insert(1,"Vezes2",C)#1= posição (segunda coluna), "Vezes2" = nome da coluna, C=array que vira a coluna nova

#print(dataSeixos)


	#ALGUNS TRUQUES ÚTEIS

#print(data_teste)

#print(data_teste.Fácies.unique()) #para listar as classes que existem na coluna facies

#print(data_teste.groupby('Fácies').size()) # para saber quantos tem de cada classe com base em uma coluna

#print("Fácies_Aa= \n",data_teste.Fácies[data_teste.Fácies!="Aa"])

	#ÍNDICES NO DATAFRAME

#print("Algumas fácies \n",data_teste.Rumo[:4])

#print(data_teste.Espessura[data_teste.Fácies=="Afl"])

print(data_teste.loc[0][0]) #[linha][coluna], índice pode ser número ou nome da coluna entre ''




#Fim da primeira Aula!



