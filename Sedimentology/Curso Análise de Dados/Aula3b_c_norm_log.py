import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy 
from scipy import stats
from scipy.stats import norm
from scipy.stats import lognorm
from scipy.stats import pareto
from scipy.stats import gamma
from scipy.stats import beta
from scipy.stats import vonmises
from matplotlib.ticker import FuncFormatter, MultipleLocator
from scipy.stats import kurtosis, skew
from scipy.interpolate import interp1d



dataSeixos=pd.read_csv('Seixos_Rejeito.csv',skiprows=0,header=None) # lista simples de tamanhos de seixos

data1=pd.read_csv('Dados1.csv',skiprows=0,header=None) #


df=pd.read_csv('Data_Perm_Por.csv',skiprows=0,header=0)

dfOSL=pd.read_csv('Exemplo_OSL.csv',skiprows=0,header=0)



#Entendendo um KDE

x = np.array([2,5,6,8])
bandwidth = 1.06 * x.std() * x.size ** (-1 / 5.)
support = np.linspace(-4, 13, 200)

plt.figure('KDE')
sns.rugplot(x, color=".2", linewidth=3);
sns.kdeplot(x,bw=bandwidth,shade=True,color='olivedrab').set_title('Fundamento do KDE')



kernels = []
for x_i in x:

    kernel = stats.norm(x_i, bandwidth).pdf(support)/4
    kernels.append(kernel)
    plt.plot(support, kernel, color="r")



plt.figure('Histo diâmetros seixos (cm)')
sns.distplot(dataSeixos,bins=30,kde=True).set_title('Dataseixos')




#histogramas não lidam bem com NaN entao  tira o NaN com .notnull
z=df.Por_Population[df.Por_Population.notnull()]

plt.figure('Kurtosis e skewness')
ax=sns.distplot(z, bins=15, kde=True);#sem os notanumber (notnull) para evitar erro
plt.ylabel("Frequency")
ax.text(30,0.05,'excess_kurtosis:\n'+str(np.round(kurtosis(z),3))+'\nskewness:\n'+str(np.round(skew(z),3)))

mu,sigma = norm.fit(z)
xn= np.linspace(-5,50,100)
pdf = norm.pdf(xn, mu,sigma)

ax.plot(xn, pdf, 'r--',label="norm fit")
plt.legend()


#ax.set_xscale("log")
fig = ax.get_figure()
'''
'''

	#Não parecer normal pode ser efeito do tamanho da amostra:

x = np.random.normal(mu, sigma, 15)   # valores aleatórios e mdistribuição normal com média e sigma iguais ao de cima

plt.figure(222)
ax2=sns.distplot(x, bins=15, kde=True)
ax2.text(30,0.05,'excess_kurtosis:\n'+str(np.round(kurtosis(x),3))+'\nskewness:\n'+str(np.round(skew(x),3)))

mu,sigma = norm.fit(x)
xn= np.linspace(-5,50,100)
pdf = norm.pdf(xn, mu,sigma)
ax2.plot(xn, pdf, 'r--',label="norm fit")
ax2.legend()

#print( 'excesso de kurtosis (distribuição normal = 0): ', kurtosis(x) )
#print( 'skewness (distribuição normal = 0): ', skew(x) ,'\n')


	#provando a dependência da tamanho da amostra:

Sample_Size = np.logspace(1,4,30)

plt.figure('Sample_Size')
sns.rugplot(Sample_Size).set_title('Sample sizes')


Repeat=300 # numeros de amostras aleatórias de cada tamanho
Kurtosis=[]
Skewness=[]
SSs=[]


count=0

while count<len(Sample_Size):
	
	Krts=[]
	Skws=[]
	SS=[]
	count2=0

	while count2<Repeat:

		x = np.random.normal(mu, sigma, np.int(Sample_Size[count]))
		K = kurtosis(x)
		Krts= np.append(Krts,K)
		S= skew(x) 
		Skws= np.append(Skws,S)
		SS=np.append(SS,Sample_Size[count])
		count2+=1
		print(count,count2)

	Kurtosis=np.append(Kurtosis,Krts)
	Skewness=np.append(Skewness,Skws)
	SSs=np.append(SSs,SS)

	count+=1



plt.figure('Tamanho da amostra e kurtosis',figsize=(10,7))
sns.lineplot(SSs,Kurtosis,ci=99,label="ci=99%")
plt.title("Excesso de kurtosis por tamanho da amostra")
#plt.savefig('Kurt.png')

plt.figure('Tamanho da amostra e skewness',figsize=(10,7))
sns.lineplot(SSs,Skewness,ci=99,label="ci=99%")
plt.title("Skewness por tamanho da amostra")
#plt.savefig('Skew.png')

	


	# DISTRIBUIÇÃO LOGNORMAL


	#Porosidade todas granulações

Phi=df.Por_Population[df.Por_Population.notnull()]
plt.figure('Phi todas granulações')
ax=sns.distplot(Phi, bins=20, kde=True).set_title('Phi todas granulações');#sem os notanumber (notnull) para evitar erro
plt.text(35,0.045,'excess_kurtosis:\n'+str(np.round(kurtosis(Phi),3))+'\nskewness:\n'+str(np.round(skew(Phi),3))+'\nN= '+str(len(Phi)))
plt.ylabel("Frequency")
#ax.set_xscale("log")
mu,sigma = norm.fit(Phi)
x= np.linspace(0,50,150)
pdf = norm.pdf(x, mu,sigma)
plt.plot(x, pdf, 'r--',label="norm fit")
plt.legend()

	#Permeabilidade de arenitos finos

DF= df.Perm_Population[df.Perm_Population.notnull()]
DF=DF[df.Grainsize=='F']
plt.figure('k de AF',figsize=(11,5))
sns.distplot(DF[DF<10000], bins=100,kde=False).set_title('k de AF') # density=True para normalizar (área soma 1)
plt.text(2000,200,'excess_kurtosis:\n'+str(np.round(kurtosis(DF),3))+'\nskewness:\n'+str(np.round(skew(DF),3))+'\nN= '+str(len(DF)))


#ver se é lognormal (Permeabilidade de arenitos finos)

dataplot = np.log10(DF[DF!=0]) #!= para diferente de, evitando o log de zero

dataplot=dataplot[dataplot.notnull()] #para tirar os NaN

plt.figure('Log k de Af')
ax2=sns.distplot(dataplot, bins=100,kde=True).set_title('Log k de Af') 
plt.text(4.5,0.4,'excess_kurtosis:\n'+str(np.round(kurtosis(dataplot),3))+'\nskewness:\n'+str(np.round(skew(dataplot),3))+'\nN:\n'+str(len(dataplot)))


mu,sigma = norm.fit(dataplot)
xn= np.linspace(0,6,100)
pdf = norm.pdf(xn, mu,sigma)
plt.plot(xn, pdf, 'r--',label="norm fit")
plt.legend()


# ou tratar direto como log normal


xn= np.linspace(0,10000,500)
shape, loc, scale =lognorm.fit(DF[DF!=0])


pdf = lognorm.pdf(xn, shape, loc, scale) #pode tratar como três parâmetros ou só como dois



plt.figure('Lognorm PDF')
plt.title('Lognorm PDF')
xn= np.linspace(0,10000,500)
sns.distplot(DF[DF<10000], bins=100,kde=True).set_title('k de AF') # density=True para normalizar (área soma 1)
ax2=sns.lineplot(xn, pdf, color=(0.9,0.2,0.1))
#ax2.fill_between(xn, pdf, color='olivedrab', alpha=0.2)

'''
# Se há números negativos na população o gráfico fica distorcido, pois todos plotam entre 0 e 1
mu=3
sigma=0.2


xn= np.linspace(0,35,500)
pdf = lognorm.pdf(xn, s=sigma, scale=np.exp(mu)) 

plt.figure('Lognorm PDF 2')
plt.title(f'Lognorm PDF 2,  mu={ np.log(1)},  sigma={1}')
ax=sns.lineplot(xn, pdf, color=(0.9,0.2,0.1))
ax.fill_between(xn, pdf, color='olivedrab', alpha=0.2)

'''



		#Permeabilidade de todas as granulações

DF= df.Perm_Population[df.Perm_Population.notnull()]
plt.figure('k todas as granulações',figsize=(11,5))
sns.distplot(DF[DF<10000], bins=100,kde=False).set_title('k todas as granulações') # density=True para normalizar (área soma 1)
plt.text(2000,300,'excess_kurtosis:\n'+str(np.round(kurtosis(DF),3))+'\nskewness:\n'+str(np.round(skew(DF),3))+'\nN= '+str(len(DF)))


#ver se é lognormal 

dataplot = np.log10(DF[DF!=0]) #!= para diferente de, evitando o log de zero

dataplot=dataplot[dataplot.notnull()] #para tirar os NaN



plt.figure('Log k todas as granulações')
ax=sns.distplot(dataplot[dataplot.notnull()], bins=100, kde=True).set_title('Log k todas as granulações')  #sem os notanumber (notnull) para evitar erro
mu,sigma = norm.fit(dataplot[dataplot.notnull()])
xn= np.linspace(0,6,100)
pdf = norm.pdf(xn, mu,sigma)
plt.plot(xn, pdf, 'r--',label="norm fit")
plt.text(4.5,0.4,'excess_kurtosis:\n'+str(np.round(kurtosis(dataplot),3))+'\nskewness:\n'+str(np.round(skew(dataplot),3))+'\nN:\n'+str(len(DF)))
plt.legend()
plt.ylabel("Frequency")





# BOXPLOT E VIOLIN PLOT

plt.figure(8)
ax=sns.boxplot(dataSeixos)
plt.ylabel("Frequency")
plt.title("Diametro Seixos Caverna")



plt.figure(61)
ax2=sns.violinplot(dataSeixos)
plt.ylabel("Frequency")
plt.title("Diametro Seixos Caverna")



plt.figure(5)
ax3=sns.violinplot(df.Por_Population[df.Por_Population.notnull()])
plt.ylabel("Frequency")



				#Fim parte b

		#PARTE C OUTRAS DISTRIBUIÇÕES




N=500
xn= np.linspace(0,50,N)
xc= np.linspace(0,100,100)


#Pareto

alpha=[1.16]
loc=0
scale=1

for i in alpha:

	pdf = pareto.pdf(xn,i, loc)

	plt.figure('Pareto PDF')
	plt.title('Pareto PDF')
	ax=sns.lineplot(xn, pdf, color='k')
	ax.fill_between(xn, pdf, color='olivedrab', alpha=0.2)




cdf= pareto.cdf(xc,alpha[0], loc,scale)

plt.figure('Pareto CDF')
plt.title('Pareto CDF')
ax=sns.lineplot(xc, cdf, color='red')
ax.fill_between(xc, cdf, color="firebrick", alpha=0.3)



#Gamma (com a = é uma exponencial)
a=[1,3,5]


for i in a:

	pdf = gamma.pdf(xn,i, loc,scale)


	plt.figure('Gama PDF')
	plt.title('Gama PDF')
	ax=sns.lineplot(xn, pdf, color=(0.9,0.2,0.1))
	ax.fill_between(xn, pdf, color='olivedrab', alpha=0.2)



cdf= gamma.cdf(xc,a[-1], loc,scale)

plt.figure('Gama CDF')
plt.title('Gama CDF')
ax=sns.lineplot(xc, cdf, color='r')
ax.fill_between(xc, cdf, color='firebrick', alpha=0.3)

#Beta
xb=np.linspace(0,1,100)

a, b = 4, 20

pdf = beta.pdf(xb,a,b)

plt.figure('Beta PDF')
plt.title('Beta PDF')
ax=sns.lineplot(xb, pdf, color=(0.9,0.2,0.1))
ax.fill_between(xb, pdf, color='olivedrab', alpha=0.2)

a, b = 15, 20

pdf = beta.pdf(xb,a,b)
ax=sns.lineplot(xb, pdf, color=(0.9,0.2,0.1))
ax.fill_between(xb, pdf, color='olivedrab', alpha=0.2)


a, b = 50, 5
pdf = beta.pdf(xb,a,b)
ax=sns.lineplot(xb, pdf, color=(0.9,0.2,0.1))
ax.fill_between(xb, pdf, color='olivedrab', alpha=0.2)
#print(stats.sem(Sample))

#vonmises

xv=np.linspace(0,2*np.pi,100)

kappa, loc = 1.5, 1.9*np.pi

pdf = vonmises.pdf(xv,kappa,loc)

plt.figure('Von_Mises PDF')
plt.title('Von_Mises PDF')
ax=sns.lineplot(xv, pdf, color=(0.9,0.2,0.1))

ax.fill_between(xv, pdf, color='olivedrab', alpha=0.2)
ax.xaxis.set_major_formatter(FuncFormatter(
   lambda val,pos: '{:.0g}$\pi$'.format(val/np.pi) if val !=0 else '0'
))
ax.xaxis.set_major_locator(MultipleLocator(base=np.pi))
plt.show()


#Distribuição Multimodal

print(dfOSL)

#Criando as pdfs de cada ponto

cont=0
All_pdfs=[]


dfOSL=dfOSL#.loc[:15][:]
while cont<len(dfOSL.Idade):

	x_new = np.random.normal(dfOSL.Idade[cont], dfOSL.Two_sig[cont]/2, 200)
	All_pdfs=np.append(All_pdfs,x_new)

	cont+=1

plt.figure(1003)
sns.distplot(All_pdfs,bins=30,kde=True)

plt.show()
