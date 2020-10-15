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
from sklearn.metrics import r2_score
from scipy.stats import multivariate_normal as mvn
from sklearn.covariance import empirical_covariance
from sklearn.metrics import mean_squared_error as MSE
from scipy.stats import theilslopes
from GeoSed_stat_funcs import uReg, SDR, scatt_r2,linreg_err_propag
import scipy.stats



x=np.random.normal(20,5,50)
y=x+np.random.normal(0,2,50)

#xerr=np.random.rand(50)*.05
#yerr=np.random.rand(50)*.05

xerr=np.empty(50)+0.8
yerr=np.empty(50)+0.2

	#usando a função criada para obter os parâmetros de vários tipos de regressão

uParams= uReg(x,y)
#uParamsMM= uReg(x,y,reg_type='MM',xerr=2.,Dxerr=.5)
#uParamsODR= uReg(x,y,reg_type='ODR',xerr=xerr,Dxerr=.5,yerr=yerr,plot_title="Reg")
#uParamsODR= uReg(x,y,reg_type='Theil',conf_int=0.95,plot_title="Reg")


		##Erro slope, erro intercepto e  ponto nulo

def linf(x,a,b):
		
	return ((a*x)+b)


popt, pcov = curve_fit(linf,x,y)

uSlope=ufloat(popt[0],pcov[0,0]**0.5)
print('Slope',uSlope)

uIntercept=ufloat(popt[1],pcov[1,1]**0.5)
print('Intercepto',uIntercept)

null_point= [np.mean(x),np.mean(y)] # aqui X e erro têm distribuições normais então o ponto nulo equivale às médias
Intercept_meu = -((popt[0]*null_point[0])-null_point[1])



Max_slope=popt[0]+(pcov[0,0]**0.5)
Min_slope=popt[0]-(pcov[0,0]**0.5)

Intercept_max = -((Max_slope*null_point[0])-null_point[1])
Intercept_min = -((Min_slope*null_point[0])-null_point[1])


plt.figure(1)
sns.jointplot(x,y,kind='reg')
plt.plot()
plt.savefig('5d_jointplot.png')

print(f'Max, Min Slopes {np.round(Max_slope,2),np.round(Min_slope,2)}')

print(f'Intercept, max, min {np.round(Intercept_meu,2)}, {np.round(Intercept_min,2)}, {np.round(Intercept_max,2)}')


# Em um caso mais geral, o ponto nulo pode ser encontrado como a igualdade das retas
Int_max= popt[1]+(pcov[1,1]**0.5)
Int_min= popt[1]-(pcov[1,1]**0.5)

null_x1 = (Int_max-popt[1])/(popt[0]-Min_slope)
null_x2 = (Int_min-popt[1])/(popt[0]-Max_slope)

print(f'ponto nulo {null_x1} {null_x2}')


'''

		#Propagando o erro de xdata na regressão

# O erro do slope é zero em np.mean(x) e não em x=0!

My_x= np.random.normal(20,6,150)
My_x_err=np.ones(150)*1.5 #np.random.rand(50)*0.1
uMydata=unumpy.uarray(My_x,My_x_err)



	#usando a função criada para propagação

sigmas=2. # para o plot de barras de erro

uDepend , null_x= linreg_err_propag(uMydata,uParams,SDR='no',title='Sem SDR')

scatt_r2(unumpy.nominal_values(uMydata),unumpy.nominal_values(uDepend),yerr=unumpy.std_devs(uDepend)*sigmas,title='SDR=no, err_x =1.5, err_y 2 sig')



uDepend , null_x= linreg_err_propag(uMydata,uParams,SDR='yes',title='Com SDR')

scatt_r2(unumpy.nominal_values(uMydata),unumpy.nominal_values(uDepend),yerr=unumpy.std_devs(uDepend)*sigmas,title='SDR=yes, err_x =1.5, err_y 2 sig')

print(f'Null x {null_x}')




	# Se os resíduos não têm distribuição normal	

# Resíduos em lognormal
x=(np.random.rand(150)-0.5)*20
y=x+np.random.lognormal(0,1.5,150)

scatt_r2(x,y,title='Non-normal_resid')



# Regressão não paramétrica
#Theil sen reg o y vem antes!


s, i ,n,n,n = linregress(x, y)

medslope, medintercept, lo_slope, up_slope= theilslopes(y, x, 0.90) #  low e up_slope = Lower e upper  bound of the confidence interval on medslope.

xplot=np.linspace(min(x),max(x),100)

yOLSq= (s*xplot) +i
yTheil= (medslope*xplot)+medintercept
yTup= (up_slope*xplot)+medintercept
yTol= (lo_slope*xplot)+medintercept

plt.figure('Regressão não paramétrica')
plt.title('Regressão não paramétrica')
plt.plot(x,y,'ko',alpha=0.3)
plt.plot(xplot,yOLSq,color='blue',label='OSLq')
plt.plot(xplot,yTheil,color='red',label='Theil')
plt.plot(xplot,yTup,'r--')
plt.plot(xplot,yTol,'r--')
plt.legend()

uReg(x,y,reg_type='Theil',conf_int=0.95,plot_title="Regressão tipo")

'''


plt.show()
