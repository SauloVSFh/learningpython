import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy import stats
from scipy.stats import norm
from scipy.stats import lognorm
from scipy.stats import kurtosis, skew
from scipy.interpolate import interp1d

import random


#Um dado de seis faces
Dado=[1,2,3,4,5,6]

Dist=[]
DistSum=[]
Sum5=[]
#Sum15=[]

cont=0

while cont<10000:
	Dist=np.append(Dist,random.choice(Dado))
	DistSum=np.append(DistSum,random.choice(Dado)+random.choice(Dado))
	Sum5=np.append(Sum5,random.choice(Dado)+random.choice(Dado)+random.choice(Dado)+random.choice(Dado)+random.choice(Dado))

	cont+=1

Fig1=plt.figure(1)
ax0=sns.distplot(Dist,bins=20,kde=False)
plt.title('100.000 lances de um dado')

Fig2=plt.figure(2)
ax=sns.distplot(DistSum,bins=20,norm_hist=True,kde=False)
plt.title('100.000 lances, soma de dois dados')

Fig3=plt.figure(3)
ax2=sns.distplot(Sum5,bins=26,norm_hist=True,kde=False)
plt.title('100.000 lances, soma de cinco dados')




# DESCRIÇÃO DOS DADOS

dfSum5=pd.DataFrame(Sum5)
print(dfSum5.describe())


# obtendo a pdf dos dados

mu,sigma = norm.fit(Sum5)
xn= np.linspace(0,35,100)
pdf = norm.pdf(xn, mu,sigma)
ax2.plot(xn, pdf, 'r--',label="norm fit")
plt.legend()





#Plotando a CDF
cdf = norm.cdf(xn, mu,sigma)

Fig5=plt.figure(5)
plt.hist(Sum5, bins=25,density=True, cumulative=True,color='darkseagreen') #density=True para normalizar
ax23=sns.lineplot(xn, cdf, color='red',label="norm fit")
ax23.legend()
plt.title("Histograma cumulativo e CDF")

#Percentis e Desvio Padrão
#1 sigma 68,3 centrais
#2 sigma 95,5 centrais
#3 sigma 99,7 centrais



S1=68.3
S2=95.5
S3=99.7
a=(100-S1)/2
b=(100-S2)/2
c=(100-S3)/2

#calculando a porcentagem entre + e - 1sigma na CDF
A1 = np.interp(mu-sigma,xn,cdf)
B1= np.interp(mu+sigma,xn,cdf)
print("Probabilidade entre +1 sigma e -1 sigma: ",B1-A1)


A2 = np.interp(mu-2*sigma,xn,cdf)
B2= np.interp(mu+2*sigma,xn,cdf)
print("Probabilidade entre +2 sigma e -2 sigma: ",B2-A2)


A3 = np.interp(mu-3*sigma,xn,cdf)
B3= np.interp(mu+3*sigma,xn,cdf)
print("Probabilidade entre +3 sigma e -3 sigma: ",B3-A3)

# Curva gaussiana e desvio padrão

Fig4=plt.figure(4)
ax3=sns.lineplot(xn, pdf, color='blue')
ax3.fill_between(xn, pdf, color="cadetblue", alpha=0.3)

plt.plot([mu-sigma,mu-sigma],[0,0.11],color='saddlebrown',linestyle='--')
plt.plot([mu+sigma,mu+sigma],[0,0.11],color='saddlebrown',linestyle='--')
plt.plot([mu-2*sigma,mu-2*sigma],[0,0.11],color='crimson',linestyle='--')
plt.plot([mu+2*sigma,mu+2*sigma],[0,0.11],color='crimson',linestyle='--')
plt.plot([mu-3*sigma,mu-3*sigma],[0,0.11],color='tomato',linestyle='--')
plt.plot([mu+3*sigma,mu+3*sigma],[0,0.11],color='tomato',linestyle='--')
plt.title('Gaussiana e desvio padrão')

#CDF e desvio padrão

Fig6=plt.figure(6)
ax4=sns.lineplot(xn, cdf, color='blue')
ax4.fill_between(xn, cdf, color="olivedrab", alpha=0.3)

plt.plot([mu-sigma,mu-sigma],[0,1],color='saddlebrown',linestyle='--')
plt.plot([mu+sigma,mu+sigma],[0,1],color='saddlebrown',linestyle='--')
plt.plot([mu-2*sigma,mu-2*sigma],[0,1],color='crimson',linestyle='--')
plt.plot([mu+2*sigma,mu+2*sigma],[0,1],color='crimson',linestyle='--')
plt.plot([mu-3*sigma,mu-3*sigma],[0,1],color='tomato',linestyle='--')
plt.plot([mu+3*sigma,mu+3*sigma],[0,1],color='tomato',linestyle='--')
plt.title('CDF e desvio padrão')


Fig1.savefig("1_dado.png")

Fig2.savefig("2_dados.png")

Fig3.savefig("5_dados.png")

Fig4.savefig("Gaussiana_std.png")

Fig5.savefig("CDF.png")

Fig6.savefig("CDF_std.png")


#plt.show()


	
	
