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
from scipy.odr import Model, Data, RealData, ODR
from scipy.stats import pearsonr
from scipy.stats import multivariate_normal as mvn
from sklearn.covariance import empirical_covariance
from sklearn.metrics import mean_squared_error as MSE
import scipy.stats

# minhas funções para estatística

		# O desvio padrão dos resíduos

def SDR(x,y,popt,ddof=1): # desvio padrão dos resíduos

		
	y_pred = (popt[0]*x) + popt[1]
	Res=[]
	cont=0

	while cont< len(y_pred):
		res= (y_pred[cont] - y[cont])**2
		Res.append(res)
		cont+=1

	return(np.sqrt(np.sum(Res)/(len(y)-ddof)))


	#Função para obteção dos parâmetros de erro da regressão


def uReg (x,y,reg_type='OLSq',xerr=0.0,Dxerr=0.0,yerr=0.0,conf_int=.90,title='Regressão'): # type 'OLSq (pode ter erro em y - vetor yerr), 'ODR' (regressão ortogonal - precisa de vetor xerr e float Dxerr (incerteza estimada do erro em x em %)), 'MM' (correção pelo método dos momentos - precisa de float xerr e float Dxerr e, %) e não paramétrica 'Theil'precisa do conf_int e retorna [medslope, medintercept, lo_slope, up_slope,conf_int,R2]

	def f(p, x):
		
		return (p[0] * x) + p[1]

	def linf(x,a,b):
		
		return ((a*x)+b)


		# O desvio padrão  dos resíduos



	def SDR(x,y,popt,ddof=1): # desvio padrão dos resíduos

		
		y_pred = (popt[0]*x) + popt[1]
		Res=[]
		cont=0

		while cont< len(y_pred):
			res= (y_pred[cont] - y[cont])**2
			Res.append(res)
			cont+=1

		return(np.sqrt(np.sum(Res)/(len(y)-ddof)))



	def orthoregress(x, y,xerr,yerr):
				
		linreg = linregress(x, y)
		mod = Model(f)
		
		dat = RealData(x, y,sx=xerr,sy=yerr)
		
		od = ODR(dat, mod, beta0=linreg[0:2])
		out = od.run()
		return list(out.beta)


	#rodando

	if np.size(yerr)==1:

		if yerr==0:

			popt, pcov = curve_fit(linf,x,y)

	else:
		popt, pcov = curve_fit(linf,x,y,sigma=yerr)

	#caso de reg_type ser "OLSq"

	uSlope= ufloat(popt[0],(pcov[0,0]**0.5))
	uIntercept = ufloat(popt[1],(pcov[1,1]**0.5))
	uResid = ufloat(0.0,SDR(x,y,popt))

	y_pred= (x *uSlope.n)+uIntercept.n
	R2= np.round(r2_score(y,y_pred),2)


	if reg_type=='MM':

		Max_slope=popt[0]+(pcov[0,0]**0.5)
		Min_slope=popt[0]-(pcov[0,0]**0.5)
		Int_max= popt[1]+(pcov[1,1]**0.5)
		Int_min= popt[1]-(pcov[1,1]**0.5)

		null_x = (Int_max-popt[1])/(popt[0]-Min_slope)

		uXvar=ufloat(np.var(x),0.0)
		uXerr=ufloat(xerr,(Dxerr*xerr))
			
		uSlopeMM= uSlope*uXvar/(uXvar-(uXerr**2)) # correção pelo método dos momentos, considerando erros
		null_point= [null_x,(uSlope*null_x+uIntercept)] #on a correção não afeta o y
		uInterceptMM = -((uSlopeMM*null_point[0])-null_point[1])# propação da incerteza do erro

		poptMM=[uSlopeMM.n,uInterceptMM.n]
		uResidMM= ufloat(0.0,SDR(x,y,poptMM))

		uSlope=uSlopeMM
		uIntercept=uInterceptMM
		uResid=uResidMM

		y_pred= (x *uSlope.n)+uIntercept.n
		R2= np.round(r2_score(y,y_pred),2)




	if reg_type=='ODR':


		SlopeODR, InterceptODR = orthoregress(x, y,xerr,yerr) # regressão ortogonal
		SlopeODR_min, InterceptODR_min = orthoregress(x, y,xerr-(Dxerr*xerr),yerr) # estimando o erro
		SlopeODR_max, InterceptODR_max = orthoregress(x, y,xerr+(Dxerr*xerr),yerr) # estimando o erro

		SlopeODR_err=max(np.abs(SlopeODR-SlopeODR_min),np.abs(SlopeODR-SlopeODR_max))
		InterceptODR_err=max(np.abs(InterceptODR-InterceptODR_min),np.abs(InterceptODR-InterceptODR_max))

		poptODR=[SlopeODR,InterceptODR]
		uResidODR= ufloat(0.0,SDR(x,y,poptODR))

		uSlope=ufloat(SlopeODR,SlopeODR_err)
		uIntercept=ufloat(InterceptODR,InterceptODR_err)
		uResid=uResidODR

		y_pred= (x *SlopeODR)+InterceptODR
		R2= np.round(r2_score(y,y_pred),2)

	uParams = [uSlope,uIntercept,uResid,R2]

	if reg_type=='Theil':

		medslope, medintercept, lo_slope, up_slope= scipy.stats.theilslopes(y, x, conf_int)
		y_pred= (x *medslope)+medintercept
		R2= np.round(r2_score(y,y_pred),2)
	
		uParams = [medslope, medintercept, lo_slope, up_slope,conf_int,R2]



	#Plot

	def pearsonr_meu(x,y):

		return(np.cov(x,y)[0,1]/(np.cov(x,y)[0,0]*np.cov(x,y)[1,1]))


	pos_text_y=min(y)+(max(y)-min(y))*0.6
	if pearsonr_meu(x,y)>0:
		pos_text_x=min(x)+(max(x)-min(x))*0.1
	else:
		pos_text_x=min(x)+(max(x)-min(x))*0.8

	plt.figure(title)
	plt.title(title+' '+reg_type)
	plt.plot(x,y,'ko',alpha=0.4)	
	plt.plot(x,y_pred,color='firebrick')
	if reg_type=='Theil':
		plt.text(pos_text_x,pos_text_y,f'R²= {R2}\nSlope= {np.round(medslope,2)}\nIntercept= {np.round(medintercept,2)}\nSlope_max={np.round(up_slope,2)}  Slope_min={np.round(lo_slope,2)}\nconfidence interval= {conf_int}')
	else:
		plt.text(pos_text_x,pos_text_y,f'R²= {R2}\nSDR= {np.round(uResid.s,3)}\nSlope= {uSlope}\nIntercept= {uIntercept}')

	plt.savefig(title+'.png')




	return (uParams)


#plot de scatter com r2


def scatt_r2(x,y,xerr=None,yerr=None,title='Reg',marker='ko',linecolor='firebrick'):

	if xerr=='none':
		xerr = np.zeros(len(x))

	if yerr=='none':
		yerr = np.zeros(len(x))
		
	
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
	plt.plot(x,y,marker,alpha=0.4,zorder=10)
	plt.errorbar(x,y,yerr,xerr,fmt='none',zorder=1)	
	plt.plot(x,y_reg,color=linecolor)
	plt.text(pos_text_x,pos_text_y,f'R²= {R2}')
	plt.savefig(title+'.png')


	res=y-y_reg

	figRes, (ax1,ax2) = plt.subplots(1,2)
	ax1=sns.distplot(res,bins=10,ax=ax1)
	ax1.set_title('Resíduos')
	ax2=sns.distplot(np.log(res[res>0]),bins=10,ax=ax2)
	ax2.set_title('Log Resíduos')
	plt.savefig('Distribuição dos resíduos.png')



def linreg_err_propag(uXdata,uParams,SDR='yes',title='Propagação_de_erro'): # uXdata seus dados em formato uarray SDR='yes' para considerar o erro dos resíduos

	
	uSlope=uParams[0]
	uIntercept=uParams[1]
	uResids=uParams[2]

	#calculando o erro propagado do slope considerando o np.mean(x) como x0 
	X_n=unumpy.nominal_values(uXdata)
	X_e=unumpy.std_devs(uXdata)


	#definindo o ponto nulo
	Max_slope=uSlope.n+uSlope.s
	Min_slope=uSlope.n-uSlope.s

	Int_max= uIntercept.n+uIntercept.s
	Int_min= uIntercept.n-uIntercept.s

	null_x = (Int_max-uIntercept.n)/(uSlope.n-Min_slope)



	cont=0
	Y_errs=[]
	Ys=[]

	while cont< len(X_n): #propagando o erro considerando o Xmed como x0 

		y_i=(uSlope.n*(X_n[cont]))+uIntercept.n		
		Ys=np.append(Ys,y_i)

		y_e= np.abs(uSlope.n*(X_n[cont]-null_x))*np.sqrt((X_e[cont]/X_n[cont])**2+(uSlope.s/uSlope.n)**2)
		Y_errs=np.append(Y_errs,y_e)

		cont+=1

	uY=unumpy.uarray(Ys,Y_errs) #criando o uArray com o erro slope propagado

	if SDR=='yes':
		uY=uY+uResids # propagando a soma dos uResid

	#Plot

	def linf(x,a,b):
		
		return ((a*x)+b)

	def pearsonr_meu(x,y):

		return(np.cov(x,y)[0,1]/(np.cov(x,y)[0,0]*np.cov(x,y)[1,1]))


	popt, pcov = curve_fit(linf,X_n,Ys)
	y_reg=(popt[0]*X_n)+popt[1]
	pos_text_y=min(Ys)+(max(Ys)-min(Ys))*0.8
	if pearsonr_meu(X_n,Ys)>0:
		pos_text_x=min(X_n)+(max(X_n)-min(X_n))*0.1
	else:
		pos_text_x=min(X_n)+(max(X_n)-min(X_n))*0.8
	plt.figure(title)
	plt.title(title)
	plt.errorbar(X_n,y_reg,yerr=unumpy.std_devs(uY),color='orangered',fmt='none',zorder=1)	
	plt.plot(X_n,y_reg,color='darkblue',zorder=10)
	if SDR=='yes':
		plt.text(pos_text_x,pos_text_y,f'SDR= {np.round(uResids.s,3)}\nSlope= {uSlope}\nIntercept= {uIntercept}\nAverage input x err= {np.round(np.mean(X_e),2)}')
	else:
		plt.text(pos_text_x,pos_text_y,f'Slope= {uSlope}\nIntercept= {uIntercept}\nAverage input x err= {np.round(np.mean(X_e),2)}')
	plt.savefig(title+'.png')


	


	return(uY,null_x)




def scatt_nonlin(x,y,yerr=0.0,func_type='exp',p0=None,grau=1,title='Reg',marker='bo',linecolor='firebrick'):

	
	def pearsonr_meu(x,y):

		return(np.cov(x,y)[0,1]/(np.cov(x,y)[0,0]*np.cov(x,y)[1,1]))

	#exp
	def func(x, a, b, c):
		return a * np.exp(b * x) + c
	xplot=np.linspace(min(x),max(x),len(x))


	popt, pcov = curve_fit(func,x,y,p0=p0)
	equação = f'{np.round(popt[0],2)}*exp({np.round(popt[1],2)}*x)+({np.round(popt[2],2)})'

	#power
	if func_type=='power':

		def func(x, a, b, c):
			return a * np.power(x,b) + c

		popt, pcov = curve_fit(func,x,y,p0=p0)
		equação = f'{np.round(popt[0],2)}*(x**{np.round(popt[1],2)})+({np.round(popt[2],2)})'

	
	#log
	elif func_type=='log':

		def func(x, a, b, c):
			return a * np.log(x) + c
		xplot=np.logpace(log(min(x)),log(max(x)),100)
		popt, pcov = curve_fit(func,x,y,p0=p0)
		equação = f'{np.round(popt[0],2)}*log({np.round(popt[1],2)}*x)+({np.round(popt[2],2)})'


	#sin
	elif func_type=='sin':

		def func(x, a, b, c):
			return a * np.sin(b*x) + c
		popt, pcov = curve_fit(func,x,y,p0=p0)
		equação = f'{np.round(popt[0],2)}*sin({np.round(popt[1],2)}*x)+({np.round(popt[2],2)})'


	#considerando o erro em y
	if np.size(yerr)==1:

		if yerr==0:

			popt, pcov = curve_fit(func,x,y,p0=p0)

	else:
		popt, pcov = curve_fit(func,x,y,p0=p0,sigma=yerr)

	

	y_reg= func(x, *popt)
	R2= np.round(r2_score(y,y_reg),2)

	pos_text_y=min(y)+(max(y)-min(y))*0.7
	if pearsonr_meu(x,y)>0:
		pos_text_x=min(x)+(max(x)-min(x))*0.1
	else:
		pos_text_x=min(x)+(max(x)-min(x))*0.6

	plt.figure(title)
	plt.title(title)
	plt.plot(x,y,marker,alpha=0.4,zorder=10)
	plt.plot(xplot,func(xplot, *popt),color=linecolor,zorder=10)
	plt.errorbar(x,y,yerr,fmt='none',zorder=1)	
	plt.text(pos_text_x,pos_text_y,equação+f'\nR²= {R2}')
	plt.savefig(title+'.png')

	res=y-y_reg

	figRes, (ax1,ax2) = plt.subplots(1,2)
	ax1=sns.distplot(res,bins=10,ax=ax1)
	ax1.set_title('Resíduos')
	ax2=sns.distplot(np.log(res[res>0]),bins=10,ax=ax2)
	ax2.set_title('Log Resíduos')
	plt.savefig('Distribuição dos resíduos NL.png')





