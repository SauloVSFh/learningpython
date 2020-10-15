import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px #exportar interativo
# import random

indep = 100*(np.random.rand(100))
dep = (0.5*indep)+(15*np.random.rand(100)) #random array of 100 elements
print(type(indep))
data = {"Medida1": indep, "Medida2": dep} #dictionary to submit the random array
df = pd.DataFrame(data) #transform dict into df
print(type(df))

# plt.figure("Scatter1", edgecolor='blue', facecolor=...)
# sns.scatterplot(df.Medida1, df.Medida2)

                        #Criando um lineplot simples
x=np.linspace(0,100,51)
y= 3*(x**0.5)
# plt.figure("Line plot")
# sns.lineplot(x,y,color='red',marker='o').set(xlabel='inventado',ylabel='adaptado')
# plt.savefig('myfirstsavedplot.png')

                        #Crindo subplots
# x = np.linspace(0, 2*np.pi, 400)
# y = np.sin(x**2)

# Create just a figure and only one subplot
# fig, ax = plt.subplots()
# ax.plot(x, y)
# ax.set_title('Simple plot')

# Create two subplots and unpack the output array immediately
# f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex=True)
# ax1.plot(x, y)
# ax1.set_title('Sharing Y axis') #it works for matplotlib to use the array as the first argument of the function
# ax2.scatter(x, y,marker='.')
# ax2.fill_between(x,y,color='green',alpha=0.5)
# sns.regplot(x,y,ax=ax3).set_title("Regression") #sns you need to pass it in as an attribute
# sns.scatterplot(y,x,ax=ax4).set_title("Plot Invertido")

                        #SNS might be used inside matplotlib figures
#This is other way to create figures. syntax is the figure, tuples of tuples that will become the areas in which program will plot
# fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(10, 7), sharex=True, squeeze=False)
# sns.scatterplot(df.Medida1,df.Medida2,ax=ax1).set_title('Scatter 1')
# sns.regplot(df.Medida1,df.Medida2,ax=ax2).set_title('Regression')
# sns.lineplot(x,y,marker='o',color='firebrick',ax=ax3).set_title('Lineplot_markers') #ax is a parameter within the function
# sns.lineplot(x,y,ax=ax4).set_title('Lineplot')
# ax4.fill_between(x,y,color='red',alpha=1)

                        #barplots
Data = {'Classes':  ["A","A","B","B","E","Z","J","K"],'Dados': [102.45,23,48.2,90,74,115,78,90],"Tipo": ["II","I","II","I","I","I","I","I"]}
#Há dois valores para a classe A e dois para a B. Por padrão, os valores são plotados com IC
dfB = pd.DataFrame(Data)

f, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(5,5),squeeze=True)
sns.barplot(dfB.Classes,dfB.Dados,ax=ax1).set_title("Com intervalo de confiança")
sns.barplot(dfB.Classes,dfB.Dados,ax=ax2,ci=False).set_title("Sem intervalo de confiança $\sigma$")
sns.barplot(dfB.Classes,dfB.Dados,ax=ax3,palette="cubehelix_r",ci=False).set_title("outra paleta de cores") #_r no final inverte a paleta
sns.barplot(dfB.Classes,dfB.Dados,ax=ax4,hue=dfB.Tipo).set_title("Categorizando")
f.tight_layout(pad=1.0) #aumentar o espaçamento entre os gráficos
plt.show()

#https://www.youtube.com/watch?v=VWIUnU4PEq0&list=PLvPlYlEGKfUE7oakvSuheexM8Zq95ztkx&index=4
