import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import seaborn as sns
import scipy.stats
from scipy.stats import pearsonr
from scipy.stats import linregress
from pylab import polyfit
from sklearn.metrics import r2_score
from uncertainties import ufloat
from uncertainties import unumpy
from uncertainties import umath
from scipy.optimize import curve_fit
from scipy.odr import Model, Data, RealData, ODR
from sklearn.metrics import r2_score
from scipy.stats import multivariate_normal as mvn
from sklearn.covariance import empirical_covariance
from sklearn.metrics import mean_squared_error as MSE
import plotly.express as px #para os interativos


		#Regressão com erros na variável dependente

X=np.array([5,20,30,40,50,65])
Y=np.array([18,20,30,40,50,52])
Yerr=np.array([7,3,3,4,2,7])


plt.figure(1)
plt.errorbar(X,Y,yerr=Yerr,fmt='none')
plt.plot(X,Y,'bo')
plt.title("Regressão com erro em Y")
plt.xlabel('Variável independente')
plt.ylabel('Variável dependente')

def linf(x,a,b):

	return((a*x)+b)


popt, pcov = curve_fit(linf,X,Y)

y_reg = (popt[0]*X) + popt[1]

plt.figure(1)
plt.plot(X,y_reg,'g', label='Sem erro')
plt.legend()



popt2, pcov2 = curve_fit(linf,X,Y,sigma=Yerr)

y_reg2 = (popt2[0]*X) + popt2[1]

plt.figure(1)
plt.plot(X,y_reg2,'r', label='Considerando os erros')
plt.legend()
plt.savefig('5c_Erro_em_Y.png')

X= np.random.normal(20,5,50)
Y=X+np.random.normal(0,2,50)
Yerr=[1]*50


popt2, pcov2 = curve_fit(linf,X,Y,sigma=Yerr)

y_reg2 = (popt2[0]*X) + popt2[1]

plt.figure()
sns.jointplot(X,Y,kind='reg')
plt.errorbar(X,Y,yerr=Yerr,fmt='none')
plt.text(7,35,f'R²= {np.round(r2_score(Y,y_reg2),2)}')
plt.legend()
plt.savefig('5c_Variância_não_explicada1.png')



		#Variância não explicada

df=pd.read_csv('Formações.csv')


plt.figure(2)
sns.scatterplot(df.Medida1,df.Medida2)

fig2 = px.scatter(df, x='Medida1', y='Medida2', hover_name="Amostra",color='Unidade')#))
fig2.update_traces(marker=dict(size=10,line=dict(width=2,color='DarkSlateGrey')),selector=dict(mode='markers'))

popt,pcov = curve_fit(linf,df.Medida1,df.Medida2)
y_reg= (popt[0]*df.Medida1)+popt[1]
plt.plot(df.Medida1,y_reg,'r')

plt.text(5,60,f'R²= {np.round(r2_score(df.Medida2,y_reg),2)}')

fig2.show()


fig3 = px.scatter(df, x='Medida1', y='Medida2', hover_name="Amostra", animation_frame='Unidade',range_x=[-10,110], range_y=[-15,100])#, animation_group='Unidade', color=AE, size=por, hover_name=Grain, log_x=True, size_max=55)#))
fig3.update_traces(marker=dict(size=10,line=dict(width=2,color='DarkSlateGrey')),selector=dict(mode='markers'))

fig3.show()





Forms=np.array(df.Unidade)

Forms[df.Unidade=='Formação1']=1
Forms[df.Unidade=='Formação2']=2
Forms[df.Unidade=='Formação3']=3
Forms[df.Unidade=='Formação4']=4
Forms[df.Unidade=='Formação5']=5
Forms[df.Unidade=='Formação6']=6
Forms[df.Unidade=='Formação7']=7

df.insert(np.shape(df)[1],"Forms",Forms)


x=df.Medida1
z=df.Medida2
y=df.Forms


		#figuras 2d
idx=np.arange(0,len(x)-1,1)
idx=np.random.choice(idx,15)

x1=np.copy(x[idx])
z1=np.copy(z[idx])
print(x1)




def scatt_r2(x,y,title,marker='ko',linecolor='firebrick'):

	def pearsonr_meu(x,y):

		return(np.cov(x,y)[0,1]/(np.cov(x,y)[0,0]*np.cov(x,y)[1,1]))

	def linf(x,a,b):

		return((a*x)+b)


	popt, pcov = curve_fit(linf,x,y)
	y_reg=(popt[0]*x)+popt[1]
	R2= np.round(r2_score(y,y_reg),2)
	pos_text_y=min(y)+(max(y)-min(y))*0.9
	if pearsonr_meu(x,y)>0:
		pos_text_x=min(x)+(max(x)-min(x))*0.1
	else:
		pos_text_x=min(x)+(max(x)-min(x))*0.8
	plt.figure(title)
	plt.title(title)
	plt.plot(x,y,marker)	
	plt.plot(x,y_reg,color=linecolor)
	plt.text(pos_text_x,pos_text_y,f'R²= {R2}')
	plt.savefig(title+'.png')


scatt_r2(x1,z1,'Com_Outliers')

#descobrindo os outliers

def outliers_resid(x,y,interquartis): #retorna a posição dos  outliers considerando quantos interquartis para considerar outlier

	popt, pcov = curve_fit(linf,x,y)
	y_reg=(popt[0]*x)+popt[1]

	Resids=[]
	cont=0

	while cont<len(y):

		res=np.absolute(y_reg[cont]-y[cont])
		Resids= np.append(Resids,res)
		cont+=1


	Outliers=[]
	cont=0

	while cont< len(Resids):

		if Resids[cont]>interquartis*scipy.stats.iqr(Resids): #distância interquartis
			out=cont
			Outliers=np.append(Outliers,cont)


		cont+=1
	
	return(np.round(Outliers).astype(int))

out=outliers_resid(x1,z1,1.5)
print(out)
	
plt.figure('Com_Outliers')
plt.plot(x1[out],z1[out],'ro')
plt.savefig('Com_Outliers.png')

mask = np.ones(x1.size, dtype=bool)
mask[out]=False
x2=x1[mask] #onde não é out
z2=z1[mask] 

scatt_r2(x2,z2,'Sem_OUtliers')


#Duas variáveis

fig_2d, (ax1,ax2) = plt.subplots(1,2,figsize=(13,5))
popt, pcov = curve_fit(linf,x,z)
z_reg=(popt[0]*x)+popt[1]

ax1=sns.scatterplot(x,z,color='firebrick',ax=ax1)
ax1.plot(x,z_reg,color='b')
ax1.set_title(f'R²= {np.round(r2_score(z,z_reg),2)}')

popt, pcov = curve_fit(linf,y,z)
z_reg=(popt[0]*y)+popt[1]

ax2=sns.scatterplot(y,z,color='firebrick',ax=ax2)
ax2.plot(y,z_reg,color='b')
ax2.set_title(f'R²= {np.round(r2_score(z,z_reg),2)}')


plt.savefig('5c_duas_independentes.png')



		#figure 3d

 
# Creating figure 
fig = plt.figure(figsize = (8, 8)) 
ax = plt.axes(projection ="3d") 
    
# Add x, y gridlines  
ax.grid(b = True, color ='grey',  
        linestyle ='-.', linewidth = 0.3,  
        alpha = 0.2)  
  
  

  
# Creating plot 
sctt = ax.scatter3D(x, y, z, 
                    alpha = 0.8,
                    marker ='^') 
  
plt.title("Explicando a variância em Y") 
ax.set_xlabel('X-axis', fontweight ='bold')  
ax.set_ylabel('Y-axis', fontweight ='bold')  
ax.set_zlabel('Z-axis', fontweight ='bold') 

plt.show()

		#Considerando os erros na variável independente

Erro_x=5

X=[5,20,30,40,50,65]
Xerr=[Erro_x]*len(X)
Y=[18,20,30,40,50,52]
Yerr=[3,3,3,3,3,3]

uX=unumpy.uarray(X,Xerr)
uY=unumpy.uarray(Y,Yerr)

m,b = polyfit(X, Y, 1) 
xreg=np.array([0,max(X)])
yreg= (m*xreg)+b



cont=0
Xnew=[]
Ynew=[]

while cont< len(X):

	i= mvn.rvs(mean=[X[cont],Y[cont]], cov=[[Xerr[cont],0],[0,Yerr[cont]]],size=100) #os erros têm covariancia=0
	Xnew=np.append(Xnew,i[:,0])
	Ynew=np.append(Ynew,i[:,1])
	cont+=1




fig2, (ax1,ax2)= plt.subplots(1,2,figsize=(10,3))
ax1=sns.scatterplot(X,Y,ax=ax1)
ax1.errorbar(x=X,y=Y,xerr=Xerr,yerr=Yerr,ls='none')
ax1.plot(xreg,yreg,'r')
ax1.set_xlim(-20,85)
ax1.set_title(f'Sem erro em x, slope= {np.round(m,2)}')

m2,b2 = polyfit(Xnew, Ynew, 1) 
xreg2=np.array([0,max(X)])
yreg2= (m2*xreg)+b2
ax2=sns.scatterplot(Xnew,Ynew,alpha=0.1,ax=ax2)
ax2.plot(xreg2,yreg2,'r')
ax2.set_xlim(-20,85)
ax2.set_title(f'Com erro em x=30, slope= {np.round(m2,2)}')

plt.savefig('5c_Atenuação do slope.png')


def MM_corr_slope(X,Ex,OLS_slope): #vetor x, erro em x, slope do Ordinary Least Squares

	return (OLS_slope*np.var(X)/(np.var(X)-Ex**2))


fig21, (ax1,ax2)= plt.subplots(1,2,figsize=(10,3))

m2,b2 = polyfit(Xnew, Ynew, 1) 
xreg2=np.array([0,max(X)])
yreg2= (m2*xreg)+b2
ax1=sns.scatterplot(Xnew,Ynew,alpha=0.1,ax=ax1)
ax1.plot(xreg2,yreg2,'r')

m3=MM_corr_slope(X,Erro_x,m2)
yreg3= (m3*xreg)+b2 #corrigido por método dos momentos
ax2=sns.scatterplot(Xnew,Ynew,alpha=0.1,ax=ax2)
ax2.plot(xreg2,yreg3,color='purple')


ax1.set_xlim(-20,85)
ax2.set_xlim(-20,85)
ax1.set_title(f'OLS, slope= {np.round(m2,2)}')
ax2.set_title(f'Corrigido por MM, slope= {np.round(m3,2)}')

plt.savefig('5c_Metodo_momentos.png')




		#Regressão ortogonal (mínimos quadrados totais)



def orthoregress(x, y,xerr,yerr):
	"""Por cortesia de http://blog.rtwilson.com/orthogonal-distance-regression-in-python/
	Perform an Orthogonal Distance Regression on the given data,
	using the same interface as the standard scipy.stats.linregress function.
	Arguments:
	x: x data
	y: y data
	Returns:
	[m, c, nan, nan, nan]
	Uses standard ordinary least squares to estimate the starting parameters
	then uses the scipy.odr interface to the ODRPACK Fortran code to do the
	orthogonal distance calculations.
	"""
	linreg = linregress(x, y)
	mod = Model(f)
	if xerr==0:

		dat = RealData(x, y)
	else:
		dat = RealData(x, y,sx=xerr,sy=yerr)

	od = ODR(dat, mod, beta0=linreg[0:2])
	out = od.run()
	return list(out.beta)

def f(p, x):
	#Basic linear regression 'model' for use with ODR
	return (p[0] * x) + p[1]

OrthoSlope,OrthoInterc = orthoregress(X,Y,Xerr,Yerr)


fig21, (ax1,ax2,ax3)= plt.subplots(1,3,figsize=(14,4))

p1=sns.scatterplot(Xnew,Ynew,alpha=0.1,ax=ax1)
p1.plot(xreg2,yreg2,'r')
p1.set_xlim(-20,85)
p1.set_title(f'OLS, slope= {np.round(m2,2)}')

p2=sns.scatterplot(Xnew,Ynew,alpha=0.1,ax=ax2)
p2.plot(xreg2,yreg3,color='purple')
p2.set_xlim(-20,85)
p2.set_title(f'Corrigido MM, slope= {np.round(m3,2)}')


yOrtho= (OrthoSlope*xreg)+OrthoInterc
p3=sns.scatterplot(Xnew,Ynew,alpha=0.1,ax=ax3)
p3.plot(xreg,yOrtho,'firebrick')
p3.set_xlim(-20,85)
p3.set_title(f'Regressão ortogonal, slope= {np.round(OrthoSlope,2)}')
plt.tight_layout()
plt.savefig('5c_Orthoreg.png')


#Sensibilidade à incerteza do erro em x

sigma_x=10
sigma_resid=sigma_x/3
x=np.random.normal(10,sigma_x,150)
y=x+np.random.normal(0,sigma_resid,150)
x_err=np.linspace(0.1,7,70)
y_err=[4]*len(x)

popt, pcov = curve_fit(linf,x,y)

y_reg = (popt[0]*x) + popt[1]




OLS_slope=popt[0]
OLS_slps=np.empty(len(x_err))+popt[0]

Slope_ortho=[]
Interc_ortho=[]

for i in x_err:
	newS, newI =orthoregress(x,y,i,y_err[0])
	Slope_ortho=np.append(Slope_ortho,newS)
	Interc_ortho=np.append(Interc_ortho,newI)

print(newS)

Slope_MM=[]

for i in x_err:
	new=MM_corr_slope(x,i,OLS_slope)
	Slope_MM=np.append(Slope_MM,new)




figSens, (p1,p2)=plt.subplots(2,1,figsize=(6,11))
p1.plot(x_err/np.std(x),Slope_MM,color='tomato',label='MM-corrected')
p1.plot(x_err/np.std(x),Slope_ortho,color='olivedrab',label='OR')
p1.set_xlabel('sampe ste/sample std in independent variable')
p1.set_ylabel('Regression slope')
p1.legend()
p1.set_title("Regression sensibility to error in x")
p2=sns.scatterplot(x,y,ax=p2)
p2.plot(x,y_reg)
p2.text(min(x)+0.1*(max(x)-min(x)),min(y)+0.8*(max(y)-min(y)),f'R²= {np.round(r2_score(y,y_reg),2)}')
plt.tight_layout()

plt.savefig('5c_Slope_e_x_err.png')






covariancia=0.85
size=20000
Population = mvn.rvs(mean=[0,0], cov=[[1,covariancia],[covariancia,1]],size=size)
Indexes=np.linspace(0,20000-1,20000-1).astype(int)

SlopePop, InterceptPop, rPearsonPop, pValuePop, stderrPop = linregress(Population[:,0],Population[:,1])

def linf(x,a,b):

	return((a*x)+b)

popt, pcov =curve_fit(linf,Population[:,0],Population[:,1])
slope = popt[0]
intercept = popt[1]
slope_err=pcov[0,0]**0.5
intercept_err=pcov[1,1]**0.5
uSlope=ufloat(slope,slope_err)
uInter=ufloat(intercept,intercept_err)

#E a regressão ortogonal
ORTslope, ORTinterc = orthoregress(Population[:,0],Population[:,1],0,0)# 0 para os erros de cada ponto

plt.figure('JointPop')
ax1=sns.jointplot(Population[:,0],Population[:,1],kind='reg',joint_kws = {'scatter_kws':dict(alpha=0.01),'line_kws':{'color':'orange'}})
plt.plot(Population[:,0],(ORTslope*Population[:,0])+ORTinterc,'firebrick',label=f'Orthoregress\nslope= {np.round(ORTslope,2)}')
ax1.fig.suptitle(f'Population parameters, n={size}')
plt.text(-4,4,f'X_sigma=1\nY_sigma=1\nCov={covariancia}')
plt.text(1,-3,f'slope= {uSlope}\ninterc= {uInter}')
plt.tight_layout()
plt.legend(loc='upper right')
plt.savefig('5c_Joint_Population.png')




plt.show()
