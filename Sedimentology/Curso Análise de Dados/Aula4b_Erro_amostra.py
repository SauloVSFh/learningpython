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
from uncertainties.umath import *  # sin(), etc.
from scipy.interpolate import interp1d




		# I  - Medidas de variabilidade

Amostra=[2,3,7,9,1.2,5.4,8,9.6]
Amostra2=[2,3,7,9,1.2,5.4,8,40]


med=np.mean(Amostra)

fig, (ax1,ax2)=plt.subplots(2,1,figsize=(7,6))
ax1.vlines(x=med,ymin=-0.1,ymax=0.1,color='firebrick',linewidth=3,zorder=1)
ax1.vlines(x=Amostra,ymin=-0.05,ymax=0.05,color='b',linewidth=1,zorder=1)
ax1.axhline(y=0,xmin=0,xmax=max(Amostra),color='k',linewidth=1,zorder=1)
#para esconder os eixos
frame1=plt.gca()
frame1.axes.get_yaxis().set_visible(False)
ax1.set_title(f'Variância {np.round(np.var(Amostra),1)}, desvio padrão {np.round(np.std(Amostra),1)}')

ax2.vlines(x=med,ymin=-0.1,ymax=0.1,color='firebrick',linewidth=3,zorder=1)
ax2.vlines(x=Amostra2,ymin=-0.05,ymax=0.05,color='b',linewidth=1,zorder=1)
ax2.axhline(y=0,xmin=0,xmax=max(Amostra2),color='k',linewidth=1,zorder=1)
#para esconder os eixos
frame2=plt.gca()
frame2.axes.get_yaxis().set_visible(False)
ax2.set_title(f'Variância {np.round(np.var(Amostra2),1)}, desvio padrão {np.round(np.std(Amostra2),1)}')
plt.tight_layout()


plt.savefig('Desvio Padrão.png')


		#II- O desvio padrão da amostra não é o erro da amostra.


A =  [ 3.3 , 3.5 , 3.2 , 3.4, 5.7 , 0.1,7.9,1.2,2.3]
B = [2,3,2,3,2,1,3,2,3,2,2,3,3]

'''
a=A
print(a)
print(np.std(a))
print(stats.sem(a))
print(stats.sem(a)*(len(a)**0.5),np.std(a,ddof=1))
'''

		#III - Entendendo a variância de subamostras


#criando subamostras

mu= 0
std= 20
n=100

x= np.linspace(-70,70,100)
pdf= norm.pdf(x, mu,std)

cont=0
samples=10
means1, means2, means3 =[], [], []
stds1, stds2, stds3 =[], [], []
sample_size1 = 1
sample_size2 = 5
sample_size3 = 50

while cont<samples:

	sample1= np.random.normal(mu,std,sample_size1)
	m1 = np.mean(sample1)
	s1 = np.std(sample1)
	means1=np.append(means1,m1)
	stds1 =np.append(stds1,s1)

	sample2= np.random.normal(mu,std,sample_size2)
	m2 = np.mean(sample2)
	s2 = np.std(sample2)
	means2=np.append(means2,m2)
	stds12 =np.append(stds2,s2)

	sample3= np.random.normal(mu,std,sample_size3)
	m3 = np.mean(sample3)
	s3 = np.std(sample3)
	means3=np.append(means3,m3)
	stds3 =np.append(stds3,s3)

	cont+=1

Fig2=plt.figure(2)
ax2=sns.lineplot(x, pdf, color='red')
ax2.fill_between(x, pdf, color="tomato", alpha=0.7)
#sns.scatterplot(means1,np.zeros(len(means1)),s=90,alpha=0.6,zorder=10)
sns.rugplot(means1)
plt.plot([mu,0],[mu,0.01],color='firebrick',linewidth=3,zorder=1)
plt.text(40,0.0175,'N= '+str(sample_size1),size=12)
plt.title("Erro Padrão da Média")

Fig21=plt.figure(21)
ax2=sns.lineplot(x, pdf, color='red')
ax2.fill_between(x, pdf, color="tomato", alpha=0.7)
#sns.scatterplot(means2,np.zeros(len(means2)),s=90,alpha=0.6,zorder=10)
sns.rugplot(means2)
plt.plot([mu,0],[mu,0.01],color='firebrick',linewidth=3,zorder=1)
plt.text(40,0.0175,'N= '+str(sample_size2),size=12)
plt.title("Erro Padrão da Média")

Fig22=plt.figure(22)
ax2=sns.lineplot(x, pdf, color='red')
ax2.fill_between(x, pdf, color="tomato", alpha=0.7)
#sns.scatterplot(means3,np.zeros(len(means3)),s=90,alpha=0.6,zorder=10)
sns.rugplot(means3)
plt.plot([mu,0],[mu,0.01],color='firebrick',linewidth=3,zorder=1)
plt.text(40,0.0175,'N= '+str(sample_size3),size=12)
plt.title("Erro Padrão da Média")


		#IV - Simulação numérica e estimativa pela equação


mu=0
sigma=1
points=10
Sample_Size = np.logspace(0.5,2,points)

plt.figure('Sample_Size')
sns.rugplot(Sample_Size).set_title('Sample sizes')


Repeat=100 # números de amostras aleatórias de cada tamanho
Sig_am=[]
Resid=[]
MeansTot=[]
SSs=[]

Sig_med=[]
SEM_med=[]
SEM_ests=[]


count=0

while count<len(Sample_Size):
	
	Sigs=[]
	resids=[]
	SS=[]
	Means=[]
	count2=0
	SEM_est=[]

	
	while count2<Repeat:

		x = np.random.normal(mu, sigma, np.int(Sample_Size[count]))
		Sig = np.std(x)
		Sigs= np.append(Sigs,Sig)
		sem_est = Sig*(1/(Sample_Size[count]-1)**0.5)
		SEM_est.append(sem_est)
		mean=np.mean(x)
		R= np.abs(np.mean(x)-mu) 
		resids= np.append(resids,R)
		SS=np.append(SS,Sample_Size[count])
		Means.append(mean)
		count2+=1
		print(count,count2)
		

	Sig_am=np.append(Sig_am,Sigs)
	Resid=np.append(Resid,resids)
	SSs=np.append(SSs,SS)
	SEM_ests=np.append(SEM_ests,SEM_est)

	Sig_med=np.append(Sig_med,np.mean(Sigs))
	SEM_med=np.append(SEM_med,np.std(Means))
	MeansTot.append(np.mean(Means))
	

	count+=1

	#Sigma_estimado
DP_pop=sigma

plt.figure('Tamanho da amostra e desvio padrão da amostra',figsize=(10,7))
sns.lineplot(SSs,Sig_am,ci=99,label="Sigma amostra ci=99%")
plt.title("desvio padrão da amostra por tamanho da amostra")
#Comparando com a estimativa pela equação
DP_pop_est=Sig_med*(Sample_Size/(Sample_Size-1))**0.5
#print(Sig_med*(Sample_Size/(Sample_Size-1))**0.5)
plt.plot(Sample_Size,DP_pop_est,'r--',label='Sigma_população estimado')
#plt.plot(Sample_Size,(DP_pop-DP_pop_est)/DP_pop_est,'g--',label='Diferença em %')
plt.legend()
plt.savefig('SD_am_vs_Sample_Size.png')


	#SEM
plt.figure('Tamanho da amostra e SEM',figsize=(10,7))
plt.plot(Sample_Size,SEM_med,label="SEM solução numérica")
sns.lineplot(SSs,SEM_ests,ci=99.9,label="SEM estimado de\n cada amostra, ci=99.9%")
plt.title(f"Erro padrão por tamanho da amostra\n{Repeat} iterações")
#Comparando com a estimativa pela equação
SEM = Sig_med*(1/(Sample_Size-1)**0.5)
plt.plot(Sample_Size,SEM,'r--',label="SEM pela equação")
plt.legend()
plt.savefig('SEM and Sample_Size.png')
# Como a superestimação do erro é sempre menor que 26%, essa variação some no arredondamento (o erro é expresso com os mesmos algarismos significativos da medida)



		# V- aumentando o o número de análises

#SigmaA, SigmaP e EPM variando com n

n=2

SAs,SPs, EPMs, Ns = [],[],[],[]
AM1, AM2, AM3 = [],[],[]
semAM1, semAM2, semAM3 = [],[],[]
spAM1,spAM2,spAM3 =  [],[],[]
nMax=200
nStep=1
STDsample = 20 

while n <nMax:

	sa= STDsample
	SAs= np.append(SAs,sa)
	sp= ((n/(n-1))**0.5) *sa
	SPs= np.append(SPs,sp)
	EPM = sp/(n**0.5)
	EPMs= np.append(EPMs,EPM)
	Ns= np.append(Ns,n)
	RdmSample= np.random.normal(0,20,3)
	AM1=np.append(AM1,RdmSample[0])
	AM2=np.append(AM2,RdmSample[1])
	AM3=np.append(AM3,RdmSample[2])
	semAM1= np.append(semAM1,stats.sem(AM1))
	semAM2= np.append(semAM2,stats.sem(AM2))
	semAM3= np.append(semAM3,stats.sem(AM3))
	spAM1= np.append(spAM1,stats.sem(AM1)*(n**0.5))
	spAM2= np.append(spAM2,stats.sem(AM2)*(n**0.5))
	spAM3= np.append(spAM3,stats.sem(AM3)*(n**0.5))
	n+= nStep


Fig3=plt.figure(3)
ax=sns.lineplot(Ns,SAs, color='red',label="Desvio Padrão da Amostra")
ax=sns.lineplot(Ns,SPs, color='firebrick',label="Estimativa do DP da população")
plt.title("Variação da estimativas do sigma da população\n com o tamanho da amostra para desvio\n padrão da amostra constante")


Fig4=plt.figure(4)
ax=sns.lineplot(Ns,EPMs, color='cadetblue',label="Erro padrão da Média para DP constante=20")
ax=sns.lineplot(Ns,semAM1, color='olive',linestyle='dashed',label="EPM da amostra aleatória 1")
ax=sns.lineplot(Ns,semAM2, color='firebrick',linestyle='dashed',label="EPM da amostra aleatória 2")
#ax=sns.lineplot(Ns,semAM3, color='orange',linestyle='dashed',label="Média da amostra aleatória 3")
plt.title("Variação do Erro Padrão da Média com DP constante\n e do EPM de amostra aleatória com aumento do N" )

Fig41=plt.figure(41)
ax=sns.lineplot(Ns,SAs, color='cadetblue',label="Desvio Padrão Real da População")
ax=sns.lineplot(Ns,spAM1, color='olive',linestyle='dashed',label="DPP da amostra aleatória 1")
ax=sns.lineplot(Ns,spAM2, color='firebrick',linestyle='dashed',label="DPP da amostra aleatória 2")
#ax=sns.lineplot(Ns,semAM3, color='orange',linestyle='dashed',label="DPP da amostra aleatória 3")
plt.title("Variação do DPP\n de amostra aleatória com aumento do N" )


plt.legend()


		# VI - Exercício calcular erro amostral

df=pd.read_csv('Erro_medidas.csv',skiprows=0,header=0)

cont=0
Ns=[]
Means=[]
Erros=[]
Estim_sig=[] #estimativa do desvio padrão da população 
Coef_var=[]

Rows, Columns = np.shape(df)
#print(np.shape(df))

cont=0

while cont<Columns:

	data=df.iloc[:,cont]
	data=data[data.notnull()]
	n=len(data)	
	mu=np.mean(data)
	sem=stats.sem(data)
	cv=sem/mu
	sig_est=np.std(data,ddof=1)

	Ns.append(n)
	Means.append(mu)
	Erros.append(sem)
	Estim_sig.append(sig_est)
	Coef_var.append(cv)

	cont+=1
	

data2={'Amostra':df.columns, 'N':Ns, 'Measure': Means, 'Err':Erros,'Coef_Variac':Coef_var, 'Est_sig_pop':Estim_sig}
df2=pd.DataFrame(data2)
print(df2)

#A_e = unumpy.uarray(df2.Measure, df2.Err)
#print(A_e[0])

df2.Err[df2.Err.isnull()]=max(df2.Est_sig_pop)
print(df2.Err)

'''
# Reescrevendo as funções para entender:



def func_sum_x2(A): # A é o array ou lista
	total=0
	for i in range(0,len(A)):
	 total+=A[i]**2
	return(total)

def func_Sig_m(A):

	desvios = []

	for i in range(0,len(A)):

		desv = A[i] - np.mean(A)
		desvios = np.append(desvios,desv)
		print(desvios)

	Sum_di2 = func_sum_x2(desvios)
	print(Sum_di2)


	s= (Sum_di2/len(A))**0.5  # desvio padrão da amostra


	Sig = s * ((len(A)/(len(A)-1))**0.5) #estimativa do desvio da população


	Sig_m = Sig/ (len(A)**0.5) # estimativa do erro da média de uma amostra com relação à média da população

	Mean = np.mean(A)

	return(s, Sig, Sig_m,Mean)

s, Sig, Sig_m, Mean = func_Sig_m(Amostrinha)

print("s, Sig, Sig_m",s, Sig, Sig_m)

print("stats.sem",stats.sem(Amostrinha))


'''
#plt.show()

