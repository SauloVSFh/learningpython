import pandas as pd
from pandas import DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
from scipy import stats

		#I- Erros aleatório e sistemático

Amostra=np.array([3,5,7,9,3.2,5.4,8,9.6])*2
Amostra2=Amostra-5.1


true=np.mean(Amostra)-0.2

fig, (ax1,ax2)=plt.subplots(2,1,figsize=(9,6))
ax1.vlines(x=true,ymin=-0.1,ymax=0.1,color='firebrick',linewidth=3,zorder=1,label="valor real")
ax1.vlines(x=np.mean(Amostra),ymin=-0.05,ymax=0.05,color='r',linewidth=3,zorder=1,label="valor estimado")
ax1.vlines(x=Amostra,ymin=-0.05,ymax=0.05,color='b',linewidth=1,zorder=1,label="medidas")
ax1.axhline(y=0,xmin=0,xmax=max(Amostra),color='k',linewidth=1,zorder=1)
ax1.set_xlim(0,20)
#para esconder os eixos
frame1=plt.gca()
frame1.axes.get_yaxis().set_visible(False)
ax1.set_title('Erro aleatório')
ax1.legend(loc='upper left')

ax2.vlines(x=true,ymin=-0.1,ymax=0.1,color='firebrick',linewidth=3,zorder=1)
ax2.vlines(x=np.mean(Amostra2),ymin=-0.05,ymax=0.05,color='r',linewidth=3,zorder=1,label="valor estimado")
ax2.vlines(x=Amostra2,ymin=-0.05,ymax=0.05,color='b',linewidth=1,zorder=1)
ax2.axhline(y=0,xmin=0,xmax=max(Amostra2),color='k',linewidth=1,zorder=1)
#para esconder os eixos
frame2=plt.gca()
frame2.axes.get_yaxis().set_visible(False)
ax2.set_title('Erros aleatório e sistemático')
ax2.set_xlim(0,20)

plt.tight_layout()


plt.savefig('Sistemático e aleatórios.png')

print(Amostra)
print(Amostra2)
print(np.mean(Amostra))
print(np.std(Amostra))


		# II  - Medidas de variabilidade

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


plt.show()

