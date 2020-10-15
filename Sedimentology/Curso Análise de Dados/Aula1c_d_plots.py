import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px #para os interativos




	#CRIANDO DADOS CORRELACIONADOS

indep=100*(np.random.rand(100))


dep=(0.5*indep)+(15*np.random.rand(100))


Data = {'Medida1':  indep,'Medida2':  dep}
df=pd.DataFrame(Data)



print(df)


plt.figure('scatter1',figsize=(7,5))
sns.scatterplot(df.Medida1,df.Medida2)

plt.show()





	#CRIANDO DADOS PARA UM LINEPLOT - DUAS VARIÁVEIS CONTÍNUAS
	
		#Alterações depois da plotagem

x=np.linspace(0,100,50) # array com 50 números de 0 a 100 com espaçamento constante
y= 3*(x**0.5)

plt.figure('Lineplot')
sns.lineplot(x,y,marker='o',color='firebrick')
plt.title('Lineplot simples')
#plt.title("Exemplo de lineplot")
plt.savefig('Lineplot.png')

	#Criando subplots

fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2, 2, figsize=(10, 7), sharex=True)
sns.scatterplot(df.Medida1,df.Medida2,ax=ax1).set_title('Scatter 1')
sns.regplot(df.Medida1,df.Medida2,ax=ax2).set_title('Regression')
sns.lineplot(x,y,marker='o',color='firebrick',ax=ax3).set_title('Lineplot_markers')
sns.lineplot(x,y,ax=ax4)
ax4.set_title('Lineplot')
ax4.fill_between(x,y,color='olivedrab',alpha=0.2)






	#CRIANDO DADOS PARA UM BARPLOT VARÍAVEL CATEGÓRICA E VARIÁVEL DISCRETA OU CONTÍNUA

Data = {'Classes':  ["A","A","B","B","E","Z","J","K"],'Dados': [102.45,23,48.2,90,74,115,78,90],"Tipo": ["II","I","II","I","I","I","I","I"]}
dfB=pd.DataFrame(Data)

#variando paleta e hue
plt.figure(3)
ax=sns.barplot(dfB.Classes,dfB.Dados,hue=dfB.Tipo,palette="cubehelix_r",ci=None).set_title("Dados por Classe")# hue=dfB.Tipo,, ci=None #para reverter é só por "_r" no fim do nome. outros exemplos "BrBG", "PuOr", "YlGn", "cubehelix"
plt.savefig('Barplot.png')




#Variáveis independente e dependente contínuas


indep=100*(np.random.rand(100))
dep=(0.5*indep)+(15*np.random.rand(100))
Data = {'Medida1':  indep,'Medida2':  dep}
df=pd.DataFrame(Data)

plt.figure('Scatter_contour')
sns.scatterplot(df.Medida1,df.Medida2,s=60,color='red',alpha=1.0) #s é o marker size, alpha é a tansparência
sns.kdeplot(df.Medida1,df.Medida2, cmap="Greys", shade=False, shade_lowest=False)


plt.figure('Scatter_shades')
sns.kdeplot(df.Medida1,df.Medida2, cmap="Reds", shade=True, shade_lowest=True,cbar=True,zorder=2) #cbar ára a legenda dos contornos
sns.scatterplot(df.Medida1,df.Medida2,s=60,color='black',alpha=1.0,zorder=10) #s é o marker size, alpha é a tansparência
plt.savefig('Scatterplot.png')



	#CRIANDO DADOS CORRELACIONADOS POR UNIDADE

Amostra=np.linspace(1,350,350)

x=100*(np.random.rand(350))


z1=(0.5*x[:30])+(20*np.random.rand(30)-15)
z2=(0.5*x[30:70])+(23*np.random.rand(40)-10)
z3=(0.5*x[70:140])+(25*np.random.rand(70)-5)
z4=(0.5*x[140:170])+(25*np.random.rand(30))
z5=(0.5*x[170:220])+(23*np.random.rand(50)+5)
z6=(0.5*x[220:300])+(12*np.random.rand(80)+10)
z7=(0.5*x[300:350])+(15*np.random.rand(50)+15)

dep=np.array(list(z1)+list(z2)+list(z3)+list(z4)+list(z5)+list(z6)+list(z7))
indep=x

Fm=["Formação1"]*30+["Formação2"]*40+["Formação3"]*70+["Formação4"]*30+["Formação5"]*50+["Formação6"]*80+["Formação7"]*50


Data = {'Amostra': Amostra,'Unidade':  Fm,'Medida1':  indep,'Medida2':  dep}
df2=pd.DataFrame(Data)

print(df2)


#utilizando o hue por unidade
plt.figure('Scatter_unidades',figsize=(9,5))
ax=sns.scatterplot(df2.Medida1,df2.Medida2,hue=df2.Unidade)
#ax.set_yscale("log")


#Variável independente categórica e variável dependente discreta (count)


plt.figure(5,figsize=(11,5))
sns.countplot(df2.Unidade,label="Count",palette="PuOr").set_title("Contagem por unidade")
plt.savefig('Countplot.png')



plt.figure(51,figsize=(11,5))
sns.kdeplot(df2.Medida1,df2.Medida2, cmap="Greys", shade=True, shade_lowest=True)
sns.scatterplot(df2.Medida1,df2.Medida2,s=60,hue=df2.Unidade,alpha=1.0) #s é o marker size, alpha é a tansparência


	#PLOTLY EXPRESS


fig1 = px.scatter(df2, x="Medida1", y="Medida2", color="Unidade", hover_name="Amostra")

fig1.show()


fig2 = px.scatter(df2, x='Medida1', y='Medida2', hover_name="Amostra",color='Unidade')#))
fig2.update_traces(marker=dict(size=10,line=dict(width=2,color='DarkSlateGrey')),selector=dict(mode='markers'))


fig2.show()



fig3 = px.scatter(df2, x='Medida1', y='Medida2', hover_name="Amostra", animation_frame='Unidade',range_x=[-10,110], range_y=[-15,100])#, animation_group='Unidade', color=AE, size=por, hover_name=Grain, log_x=True, size_max=55)#))
fig3.update_traces(marker=dict(size=10,line=dict(width=2,color='DarkSlateGrey')),selector=dict(mode='markers'))

fig3.show()




plt.show()
