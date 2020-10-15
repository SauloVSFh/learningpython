import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy import stats
from scipy.stats import norm
from uncertainties import ufloat
from uncertainties import unumpy
from uncertainties import umath
from uncertainties.umath import *  # sin(), etc.
from scipy.interpolate import interp1d


'''

		#  Plot de barras de erro

df=pd.read_csv('Erro_medidas2.csv',skiprows=0,header=0)

x=np.arange(1,len(df.Measure)+1,1)

Sigmas=2

plt.figure('Dados e barras de erro',figsize=(9,5))
ax2=sns.scatterplot(x,df.Measure,s=60,color='royalblue',zorder=100)
plt.title(f'Barras de erro com {Sigmas} sigma')
#plt.xscale('log')
plt.errorbar(x,df.Measure,yerr=Sigmas*df.Err,color='dodgerblue', linestyle="None")
plt.xlabel('Amostra')
plt.ylabel('medida e erro')
#plt.grid()
plt.savefig('Barras de erro.png')


		# Covariância


x=np.random.normal(0,1,1000)
y1=np.random.normal(0,1,1000)
y2=0.2*x+np.random.rand(1000)
y3=x+np.random.rand(1000)
y4=-x+np.random.rand(1000)

covar1=np.round(np.cov(x,y1)[0,1],2)
covar2=np.round(np.cov(x,y2)[0,1],2)
covar3=np.round(np.cov(x,y3)[0,1],2)
covar4=np.round(np.cov(x,y4)[0,1],2)


a=sns.jointplot(x,y1,kind='reg')
a.fig.suptitle(f'Covar = {covar1}')
b=sns.jointplot(x,y2,kind='reg')
b.fig.suptitle(f'Covar = {covar2}')
c=sns.jointplot(x,y3,kind='reg')
c.fig.suptitle(f'Covar = {covar3}')
d=sns.jointplot(x,y4,kind='reg')
d.fig.suptitle(f'Covar = {covar4}')



		#II - Soma e subtração - erro propagado independente da medida

#Soma de uma constante e dado com erro
sigma=0.5
V=3
Const=3

X=np.random.normal(V,sigma,500)
Y=X+3
data={'Var_independente_com_erro':X,'Var_dependente':Y}
dXY=pd.DataFrame(data)


fig3=sns.jointplot('Var_independente_com_erro','Var_dependente',data=dXY,xlim = (0,15),ylim = (0,15), kind="reg")
fig3.fig.suptitle(f'{V}+-{sigma} + {Const}')
fig3.savefig('Soma_de_constante.png')


#multiplicação de uma constante e dado com erro


X=np.random.normal(V,sigma,1000)
Y=X*3
data={'Var_independente_com_erro':X,'Var_dependente':Y}
dXY=pd.DataFrame(data)


fig4=sns.jointplot('Var_independente_com_erro','Var_dependente',data=dXY,xlim = (0,15),ylim = (0,15), kind="reg")
fig4.fig.suptitle(f'{V}+-{sigma} * {Const}')
fig4.savefig('Multi_de_constante.png')



#Soma de duas variáveis com erro


x=np.linspace(0,50,50)
y1=10*np.random.rand(len(x))#(2+np.random.rand(len(x)))*x#
xe=np.ones(len(x))*1.6
ye=np.ones(len(x))*3.5

#Erro pela equação
Val=x[0]-y1[0]




plt.figure('Dados inventados',figsize=(13,7))
plt.title(f'X e Y totalmente correlacinonados')
ax=sns.scatterplot(x,y1,color='firebrick',s=60)
plt.errorbar(x,y1,xerr=Sigmas*xe,yerr=Sigmas*ye,color='tomato', linestyle="None")
plt.savefig('Dados_totalmente_correlacionados.png')

Xe = unumpy.uarray(x, xe)
Ye = unumpy.uarray(y1, ye)

#print(Xe[0],Ye[0])
Soma=Xe+Ye
Sub=Xe-Ye
#print(Soma)

Nominal=[]
Erro=[]





for i in Soma:
	Nominal.append(i.nominal_value) # ou .n
	Erro.append(i.std_dev) # ou .s

fig, (ax1,ax2)= plt.subplots (2,1,figsize=(9,7),sharex=False)

e1=sns.scatterplot(Nominal,np.zeros(len(Nominal)),Nominal,s=60,ax=ax1)
e1.set_title('Subtração dos erros')
e1.errorbar(Nominal,np.zeros(len(Nominal)),yerr=Sigmas*np.array(Erro), linestyle="None")
e1.set_ylabel('Erro propagado')




		#III - Multiplicação e divisão - erro propagado independente da medida


Multi=Xe*Ye

Nominal=[]
Erro=[]

for i in Multi:
	Nominal.append(i.nominal_value) # ou .n
	Erro.append(i.std_dev) # ou .s


e2=sns.scatterplot(Nominal,np.zeros(len(Nominal)),Nominal,s=60,ax=ax2)
e2.errorbar(Nominal,np.zeros(len(Nominal)),yerr=Sigmas*np.array(Erro), linestyle="None")
e2.set_title('Multiplicação dos erros')
e2.set_ylabel('Erro propagado')
plt.tight_layout()


		#IV - Outras funções


fig12, ((ax1,ax11),(ax2,ax12),(ax3,ax13))= plt.subplots (3,2,figsize=(12,7),sharex=False)

#log


Vec=[]
for i in Xe:
	if i.n!=0: # se o valor nominal não for zero
		l=umath.log10(i)
		Vec.append(l)

Nominal=[]
Erro=[]

for i in Vec:
	Nominal.append(i.nominal_value) # ou .n
	Erro.append(i.std_dev) # ou .s


Y=np.log10(Nominal)

e1=sns.lineplot(Nominal,Y,ax=ax1)
e1.set_title('Log10')

e11=sns.scatterplot(Nominal,np.zeros(len(Nominal)),s=60,ax=ax11)
e11.errorbar(Nominal,np.zeros(len(Nominal)),yerr=Sigmas*np.array(Erro), linestyle="None")
e11.set_xlabel('Valor nominal')
e11.set_ylabel('Erro propagado')



#x²

Vec=Xe**2

Nominal=[]
Erro=[]

for i in Vec:
	Nominal.append(i.nominal_value) # ou .n
	Erro.append(i.std_dev) # ou .s


Y=np.power(Nominal,2)

e2=sns.lineplot(Nominal,Y,color='firebrick',ax=ax2)
e2.set_title('Potência')

e12=sns.scatterplot(Nominal,np.zeros(len(Nominal)),color='firebrick',s=60,ax=ax12)
e12.errorbar(Nominal,np.zeros(len(Nominal)),yerr=Sigmas*np.array(Erro),color='firebrick', linestyle="None")
e12.set_xlabel('Valor nominal')
e12.set_ylabel('Erro propagado')



#sin

Vec=[]
for i in Xe:
	
	l=umath.sin(i)
	Vec.append(l)

Nominal=[]
Erro=[]

for i in Vec:
	Nominal.append(i.nominal_value) # ou .n
	Erro.append(i.std_dev) # ou .s


Y=np.sin(Nominal)

e3=sns.lineplot(Nominal,Y,color='olivedrab',ax=ax3)
e3.set_title('Sin')

e13=sns.scatterplot(Nominal,np.zeros(len(Nominal)),color='olivedrab',s=60,ax=ax13)
e13.errorbar(Nominal,np.zeros(len(Nominal)),yerr=Sigmas*np.array(Erro),color='olivedrab', linestyle="None")
e13.set_xlabel('Valor nominal')
e13.set_ylabel('Erro propagado')


fig12.tight_layout()



fig12.savefig('Outros.png')


'''
		#Aula 4d O módulo uncertanties

df=pd.read_csv('Erro_medidas2.csv',skiprows=0,header=0)

#print(df)

Value=df.Measure[0]
Erro=df.Err[0]

Value2=df.Measure[1]
Erro2=df.Err[1]

Ve=ufloat(Value,Erro)
Ve2=ufloat(Value2,Erro2)

#print('Ufloat ',Ve,Ve2)

#print('Soma',Ve2+Ve)
#print('Div',Ve2/Ve)


UArr = unumpy.uarray(df.Measure,df.Err)

print(UArr**2)
#print(UArr) # ele mostra o float inteiro

#print(UArr[2]) # mostra apenas os algarismos significativos


#Avaliando a propagação de erro - taxa de sedimentação

IdadeA = 32.013
ErroA = 0.530
IdadeB = 25.130
ErroB = 0.780

Esp = 2.0 #distância estatigráfica (m), sem erro significativo
ErroEsp= 0.10 #imprecisão de 10 cm na medida da espessura



A= ufloat(IdadeA,ErroA)
B= ufloat(IdadeB,ErroB)
E=ufloat(Esp,ErroEsp)
#print(A,B,E)


Dif=A-B
#print('Dif',Dif)
TaxaSed= E/(A-B)
TaxaGraf=(A-B)/E
#print('Taxa',TaxaSed)

#print(A, A.n, A.s)

Txmax=(TaxaGraf.n+TaxaGraf.s)
Txmin=(TaxaGraf.n-TaxaGraf.s)

#print(Txmin)


InterceptMax=IdadeB-((Txmax*Esp)+IdadeB-IdadeA)/2
InterceptMin=IdadeB-((Txmin*Esp)+IdadeB-IdadeA)/2

retaMax=[InterceptMax,InterceptMax+(Txmax*Esp)]
retaMin=[InterceptMin,InterceptMin+(Txmin*Esp)]


#retaMax=[IdadeB,IdadeB+(Txmax*IdadeA)]
#retaMin=[IdadeB,IdadeB+(Txmin*IdadeA)]

plt.figure('taxa Sed')
plt.plot([0,Esp],[IdadeB,IdadeA],'ro')
plt.errorbar([0,Esp],[IdadeB,IdadeA],yerr=[ErroB,ErroA],zorder=10)
plt.errorbar([0,Esp],[IdadeB,IdadeA],zorder=11)
plt.plot([0,Esp],retaMax,'w--')
plt.plot([0,Esp],retaMin,'w--')


plt.fill_between([0,Esp], retaMax, retaMin, color='tomato',alpha=0.2,label='erro taxa')
plt.title(f'Simulação taxa sedimentação\ntaxa={TaxaSed} m/mil anos')
plt.xlabel('distância estratigráfica (m)')
plt.ylabel('idade (mil anos)')
plt.legend(loc='upper left')

plt.savefig('Erro_taxa.png')

Zeta=(UArr[0]**UArr[1])/(unumpy.log10(UArr[2]-unumpy.log10(UArr[3])))
print(Zeta)

#plt.show()

