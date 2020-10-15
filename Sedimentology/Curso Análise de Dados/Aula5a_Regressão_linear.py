import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import pearsonr
from scipy.stats import linregress
from pylab import polyfit
from sklearn.metrics import r2_score

	#I- Mínimos quadrados

A=np.random.normal(20,5,15)
B=(A*2)+np.random.normal(3,4,15)

plt.figure('Mínimos quadrados')
sns.scatterplot(A,B).set_title('Mínimos quadrados')
m,b = polyfit(A, B, 1) 
y= (m*A)+b
plt.plot(A,y,'r')
plt.vlines(x=A,ymin=B,ymax=y,colors='b')
plt.savefig('MinQuad.png')

	#II- Coeficiente de correlação


A=np.random.normal(20,5,50)
B=(A*0.2)+np.random.normal(2,3,50)

sns.jointplot(A,B,kind='reg')
plt.text(5,60,f'r= {np.round(pearsonr(A,B)[0],3)}')
plt.savefig('Pearson_pos.png')

sns.jointplot(A,-B,kind='reg')
plt.text(25,-20,f'r= {np.round(pearsonr(A,-B)[0],3)}')
plt.savefig('Pearson_neg.png')

print('\nSaída pearsonr')
print(pearsonr(A,B))

	#III- As funções polifit e linregress

m,b = polyfit(A, B, 1) 
y= (m*A)+b #slope e intercept

print(m,b)

Slope, Intercept, rPearson, pValue, stderr = linregress(A,B)
print('\nSaída linregress')
print('Slope',Slope)
print('Intercept',Intercept)
print('rPearson',rPearson)
print('pValue',pValue)
print('stderr',stderr)

y= (Slope*A)+Intercept

plt.figure('Regressão')
sns.scatterplot(A,B).set_title('Regressão linear')
plt.text(12.5,65,f'r= {np.round(rPearson,3)}')
plt.plot(A,y,'r')
plt.savefig('RegLin.png')

	#IV- Coeficiente de determinação

print('\nSaída sklearn.metrics.r2_score\n',r2_score(B,y))


sns.jointplot(A,B,kind='reg')
plt.text(5,60,f'r= {np.round(pearsonr(A,B)[0],3)}\nR²= {np.round(r2_score(B,y),3)}')
plt.savefig('R2_score.png')

fig, (ax1,ax2) = plt.subplots(2,1,figsize=(6,8))
ax1=sns.distplot(B,ax=ax1)
ax1.set_xlim(0,75)
ax1.set_title(f'Variância de y_real\nvar= {np.round(np.var(B),2)}')
ax2=sns.distplot((B-y)+np.mean(B),ax=ax2)
ax2.set_xlim(0,75)
ax2.set_title(f'Variância dos resíduos,\n var= {np.round(np.var(B-y),2)}')
plt.tight_layout()
plt.savefig('R2_variances.png')


sns.jointplot(A,B,kind='reg')
plt.vlines(x=A,ymin=B,ymax=y,colors='r')
plt.savefig('R2.png')

sns.jointplot(A,B-y,kind='reg')
plt.vlines(x=A,ymin=B-y,ymax=0,colors='r')
plt.savefig('R2_resid.png')

	#V- Interpretação

Slp=[3,1,0.2]
A=np.random.normal(20,5,50)
Disp=np.random.normal(2,3,50)+10
B1=(A*Slp[0])+Disp
Slope1, Intercept1, rPearson1, pValue1, stderr1 = linregress(A,B1)
y1= (Slope1*A)+Intercept1

B2=(A*Slp[1])+Disp
Slope2, Intercept2, rPearson2, pValue2, stderr2 = linregress(A,B2)
y2= (Slope2*A)+Intercept2

B3=(A*Slp[2])+Disp
Slope3, Intercept3, rPearson3, pValue3, stderr3 = linregress(A,B3)
y3= (Slope3*A)+Intercept3

fig2, (ax1,ax2,ax3)=plt.subplots(1,3,figsize=(12,4))

ax1=sns.scatterplot(A,B1,ax=ax1)
ax1.set_title(f'Regressão linear com Slope= {Slp[0]}')
ax1.set_xlim(0,90)
ax1.set_ylim(0,120)
ax1.text(5,100,f'r= {np.round(rPearson1,3)}\nR²= {np.round(r2_score(B1,y1),3)}')
ax1.plot(A,y1,'r')

ax2=sns.scatterplot(A,B2,ax=ax2)
ax2.set_title(f'Regressão linear com Slope= {Slp[1]}')
ax2.set_xlim(0,45)
ax2.set_ylim(0,60)
ax2.text(5,45,f'r= {np.round(rPearson2,3)}\nR²= {np.round(r2_score(B2,y2),3)}')
ax2.plot(A,y2,'r')


ax3=sns.scatterplot(A,B3,ax=ax3)
ax3.set_title(f'Regressão linear com Slope= {Slp[2]}')
ax3.set_xlim(0,45)
ax3.set_ylim(0,60)
ax3.text(5,40,f'r= {np.round(rPearson3,3)}\nR²= {np.round(r2_score(B3,y3),3)}')
ax3.plot(A,y3,'r')
plt.tight_layout()

plt.savefig('RegLin_interp.png')

#plt.show()
