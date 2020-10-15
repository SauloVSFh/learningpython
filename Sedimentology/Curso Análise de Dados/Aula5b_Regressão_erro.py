import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from scipy.stats import linregress
from pylab import polyfit
from sklearn.metrics import r2_score
from uncertainties import ufloat
from uncertainties import unumpy
from uncertainties import umath
from scipy.optimize import curve_fit
from scipy.stats import pearsonr
from sklearn.metrics import r2_score
from scipy.stats import multivariate_normal as mvn
from sklearn.covariance import empirical_covariance


		#O erro da taxa entre dois valores

A=ufloat(16000,500)
B=ufloat(14000,500)
C=ufloat(12000,500)
D=ufloat(10000,500)

E=10 #m
Esp=E
#Como na aula de erro da taxa:


Dif=A-B
#print('Dif',Dif)
TaxaSed= E/(A-B)
TaxaGraf=(A-B)/E
#print('Taxa',TaxaSed)

#print(A, A.n, A.s)

Txmax=(TaxaGraf.n+TaxaGraf.s)
Txmin=(TaxaGraf.n-TaxaGraf.s)

#print(Txmin)


InterceptMax=B.n-((Txmax*Esp)+B.n-A.n)/2
InterceptMin=B.n-((Txmin*Esp)+B.n-A.n)/2

retaMax=[InterceptMax,InterceptMax+(Txmax*Esp)]
retaMin=[InterceptMin,InterceptMin+(Txmin*Esp)]


#retaMax=[B.n,B.n+(Txmax*A.n)]
#retaMin=[B.n,B.n+(Txmin*A.n)]

plt.figure('taxa Sed')
plt.plot([0,Esp],[B.n,A.n],'ro')
plt.errorbar([0,Esp],[B.n,A.n],yerr=[B.s,A.s],zorder=10)
plt.errorbar([0,Esp],[B.n,A.n],zorder=11)
plt.plot([0,Esp],retaMax,'w--')
plt.plot([0,Esp],retaMin,'w--')


plt.fill_between([0,Esp], retaMax, retaMin, color='tomato',alpha=0.2,label='erro taxa')
plt.title(f'Simulação taxa sedimentação\ntaxa={TaxaSed} m/mil anos')
plt.xlabel('distância estratigráfica (m)')
plt.ylabel('idade (mil anos)')
plt.legend(loc='upper left')

plt.savefig('Erro_taxa.png')

	#Mais pontos menos erro

As=[A]*50
Adata=np.random.normal(A.n,A.s,50)
Bs=[B]*50
Bdata=np.append(Adata,np.random.normal(B.n,B.s,50))
Cs=[C]*50
Cdata=np.append(Bdata,np.random.normal(C.n,C.s,50))
Ds=[D]*50	 	
Ddata=np.append(Cdata,np.random.normal(D.n,D.s,50))

Ids=As+Bs+Cs+Ds



Data={'Ids':Ids,'Values':Ddata}
df=pd.DataFrame(Data)

plt.figure(3)
ax1=sns.boxplot(x=df.Ids,y=df.Values)
ax1.set_xlabel('')
plt.savefig('Boxplots.png')

def linf(x,a,b):

	return((a*x)+b)


		#Covariância e PDF 2d

n=20
A=np.random.normal(20,5,n)
B=(A*1)+np.random.normal(0,5,n)
Slope, Intercept, rPearson, pValue, stderr = linregress(A,B)



#calculando a covariância pela fórmula:
def covar_minha(A,B,ddof=0):

	
	Ps=[]
	cont=0	

	while cont<len(A):

		P= (A[cont]- np.mean(A)) * (B[cont] - np.mean(B))
		Ps= np.append(Ps,P)
		cont+=1

	return(np.sum(Ps)/(len(A)-ddof))


print('\nCovar_formula_Amostra', covar_minha(A,B))
print('Var A_amostra',np.var(A))
print('Var B_Amostra',np.var(B))

M=np.vstack((A,B)) #empilha na vertical e transpoe para duas colunas
M=np.transpose(M)

Cov2=empirical_covariance(M) #estimativa da covariância da população

print('Matriz com empirical covariance\n',Cov2)

Amean=np.mean(A)
Bmean=np.mean(B)


print('\nCovar_formula_População', covar_minha(A,B,ddof=1))
print('Var A_População',np.var(A,ddof=1))
print('Var B_População',np.var(B,ddof=1))

print('Matriz com np.cov\n',np.cov(A,B))




#Descobrindo a matriz de covariância (estimada) e as médias
Cov=np.cov(A,B)
Amean=np.mean(A)
Bmean=np.mean(B)

rv=mvn(mean=[Amean,Bmean], cov=Cov) #função para gerar o plot pdf2d
Dist = mvn.rvs(mean=[Amean,Bmean], cov=Cov,size=150) #criando dados aleatórios na distribuição
x=Dist[:,0]
y=Dist[:,1]


fig, (ax1,ax2,ax3) = plt.subplots(1,3,figsize=(13,4))
ax1= sns.scatterplot(A,B,ax=ax1)
ax1.set_title(f'Dados originais\n{np.round(Cov2,2)}')
ax1.set_xlim(0,40)
ax1.set_ylim(0,40)

#grade para os contornos

xg, yg = np.mgrid[0:40:1, 0:40:1]
pos = np.dstack((xg, yg)) # concatena o segundo como profundidade (3a dimensão)
ax2= sns.scatterplot(x,y,ax=ax2,zorder=10)
ax2.contourf(xg, yg, rv.pdf(pos),10, cmap='YlOrBr') #contourf para fill e contour para lines
ax2.set_title(f'Pdf 2d\n{np.round(Cov,2)}')
ax2.set_xlim(0,40)
ax2.set_ylim(0,40)



ax3= sns.scatterplot(x,y,ax=ax3,zorder=10)
ax3.set_title(f'Dados sorteados\n{np.round(empirical_covariance(Dist),2)}')
ax3.set_xlim(0,40)
ax3.set_ylim(0,40)


plt.tight_layout()
plt.savefig('Cov_pdf_2d.png')




		#Entendendo erros no slope e no intercept - Montecarlo

A=np.random.normal(20,5,50)
B=(A*2)+np.random.normal(0,4,50)

M=np.vstack((A,B)) #empilha na vertical e transpoe para duas colunas
M=np.transpose(M)

Slop, Interc, rPearson, pValue, stderr = linregress(A,B)
y= (Slop*A)+Interc



#criando uma distribuição de muitos dados com mesmas médias e matriz de covariâncias

covariancia=np.cov(A,B)
meanA=np.mean(A)
meanB=np.mean(B)
varA=np.var(A)
varB=np.var(B)
size=20000
Population = mvn.rvs(mean=[meanA,meanB], cov=covariancia,size=size)


fig, (ax1,ax2) = plt.subplots(1,2,figsize=(13,6))
ax1= sns.scatterplot(A,B,ax=ax1)
ax1.set_title(f'Dados originais\n{np.round(empirical_covariance(M),2)}')
ax1.set_xlim(0,40)
ax1.set_ylim(0,80)
ax1.text(5,60,f'N= {len(A)}')
ax2= sns.scatterplot(Population[:,0],Population[:,1],ax=ax2,zorder=10)
ax2.set_title(f'Estimativa da população\n{np.round(empirical_covariance(Population),2)}')
ax2.set_xlim(0,40)
ax2.set_ylim(0,80)
ax2.text(5,60,f'N= {len(Population[:,0])}')
plt.tight_layout()
plt.savefig('Population.png')

#Criando vários cenários por sorteio, para diferentes tamanhos de amostra
sig_y=[4]
#sig_y=[2,2.5,3,4,6]
cont0=0
Iteractions=10 #2000

fig11, (ax1,ax2) = plt.subplots(1,2,figsize=(10,6))
fig11.suptitle(f'Montecarlo simulation, {Iteractions} runs\npopulation covariance= {np.round(covariancia,2)}')

while cont0<len(sig_y):

	A=np.random.normal(20,5,50)
	B=(A*2)+np.random.normal(0,sig_y[cont0],50)
	Slop, Interc, rPearson, pValue, stderr = linregress(A,B)
	y_pred= (Slop*A)+Interc
	
	R2= r2_score(B,y_pred)

	M=np.vstack((A,B)) #empilha na vertical e transpoe para duas colunas
	M=np.transpose(M)


	SampleSizes=np.logspace(1,2.5,40).astype(int)

	cont=0

	Slopes_sigma=[]
	Slopes_means=[]
	Intercepts_sigma=[]
	Intercepts_means=[]



	while cont<len(SampleSizes):


		Slps=[]
		Ints=[]

		cont2=0

		while	cont2 <Iteractions:

			Sample= mvn.rvs(mean=[meanA,meanB], cov=np.cov(A,B),size=SampleSizes[cont]) # criando amostras de tamanho 'n' extraída da distribuição estimada da população
			popt, pcov =curve_fit(linf,Sample[:,0],Sample[:,1]) #ajustando a reta
			Slope=popt[0]
			Intercept=popt[1]
			Sample_cov=empirical_covariance(Sample)[0,1]
			Slps=np.append(Slps,Slope)
			Ints=np.append(Ints, Intercept)


			print(cont0,cont,cont2)
			cont2+=1	


		Slopes_sigma=np.append(Slopes_sigma,np.std(Slps))
		Slopes_means=np.append(Slopes_means,np.mean(Slps))
		Intercepts_sigma=np.append(Intercepts_sigma,np.std(Ints))
		Intercepts_means=np.append(Intercepts_means,np.mean(Ints))


		
		
		cont+=1


	ax1.plot(SampleSizes,Slopes_sigma/Slopes_means,label=f'{np.round(R2,2)}')
	ax1.set_title('Sample size and slope error')
	ax1.set_xlabel('Sample Size')
	ax1.set_ylabel('Slope error %')
	ax1.legend().set_title('R² original sample')
	ax2.plot(SampleSizes,Intercepts_sigma)
	ax2.set_title('Sample size and intercept error')
	ax2.set_xlabel('Sample Size')
	ax2.set_ylabel('Intercept error')
	ax2.legend()
	fig11.tight_layout()



	cont0+=1


plt.savefig('1_Montecarlo.png')


#função numérica para definir erro amostral do slope e do intercept

def LinRegErr(A,B,iteractions=50): #retorna os erros do slope e do intercept

	n=len(A)
	meanA=np.mean(A)
	meanB=np.mean(B)
	Iteractions=iteractions

	cont=0

	Slps=[]
	Ints=[]
	Covs=[]


	while	cont <Iteractions:

		Sample= mvn.rvs(mean=[meanA,meanB], cov=np.cov(A,B),size=n) # criando amostras de tamanho 'n' extraída da distribuição estimada da população
		popt, pcov =curve_fit(linf,Sample[:,0],Sample[:,1]) #ajustando a reta
		Slope=popt[0]
		Intercept=popt[1]
		Sample_cov=empirical_covariance(Sample)[0,1]
		Slps=np.append(Slps,Slope)
		Ints=np.append(Ints, Intercept)
		Covs=np.append(Covs,Sample_cov)

		print(cont)
		cont+=1	

	return(np.std(Slps),np.std(Ints),np.mean(Sample_cov))	


		#scipy.optimize.curve_fit

def func(x,a,b):

	return (a * x) + b

popt, pcov = curve_fit(func,A,B)

print('popt',popt)
print('\npcov',pcov)

Slope=ufloat(popt[0],pcov[0,0]**0.5)
Intercept=ufloat(popt[1],pcov[1,1]**0.5)

Slp_err_num, Inter_err_num, Mean_cov  = LinRegErr(A,B)

print('\nSlope',Slope)
print('Slope Err optimize',pcov[0,0]**0.5)
print('Slope Err num',Slp_err_num)

print('\nIntercept',Intercept)
print('Inter err optimize',pcov[1,1]**0.5)
print('Inter err num',Inter_err_num)

print('\nCovariância da amostra:',np.cov(A,B)[0,1])
print('Covariância média de amostras de mesmo n: ', Mean_cov)
M=np.empty([len(A),2])
M[:,0]=A
M[:,1]=B
print('Empirical covariance: ', empirical_covariance(M))

plt.figure(23)
ax1=sns.jointplot(A,B,kind='reg')
plt.text(10,70,f'r= {np.round(rPearson,3)}\nR²= {np.round(r2_score(B,y),3)}')
plt.xticks([])
Data=[[Slp_err_num,Inter_err_num],[pcov[0,0]**0.5,pcov[1,1]**0.5]]
plt.table(cellText=Data, rowLabels=('Montecarlo','curve_fit'), colLabels=('Slope err','Intecept err'), loc="bottom")
plt.tight_layout()
plt.savefig('1_Erros_Montecarlo.png')


ax2=sns.jointplot(A,B,kind='reg')
plt.text(10,70,f'r= {np.round(rPearson,3)}\nR²= {np.round(r2_score(B,y),3)}')
plt.text(23,20,f'Slope= {Slope}\nIntercept= {Intercept}')
plt.savefig('1_Erro_slope2.png')

'''
#plt.show()




