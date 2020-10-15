import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = 'Curso Análise de Dados/Seixos_Rejeito.csv'
file1 = 'Curso Análise de Dados/Dados1.csv'
data = pd.read_csv(file, header=None)
data_teste = pd.read_csv(file1,header=0)
data.columns = ['diametro']
novacoluna = ['granito']*100 + ['basalto']*105
data.index=(novacoluna)
outracoluna = data.diametro * 2
data.insert(1,"x2",outracoluna) #insert data at columns
plt.figure("hello")
sns.scatterplot(data_teste.Espessura,data_teste.Rumo)
plt.show()


                        #truque úteis

# print(data_teste.Fácies.unique()) #it prints only once the values of you select
# print(data_teste.groupby("Fácies").size()) #Vai além do unique e fala quantos elementos de cada há
# print(data_teste)
# print(data_teste.Fácies[data_teste.Fácies == 'Aa'].size()) #quantas fácies Aa há
# print(data_teste.Espessura[data_teste.Fácies == "Aa"])
                        #possível usar índices

# print(data_teste[:4])
# print(data_teste.loc[:4]['Fácies']) #linha e depois coluna


                        #Select column without NaN
# filename = "Curso Análise de Dados/Erro_medidas.csv"
# file = pd.read_csv(filename,index_col=None)
# print(file)
# for col in file.columns.values:
#     df = file.loc[file[col].notnull(), [col]]
#     if len(df) != len(file[col]) : continue
#     print(df)

                        #Select rows without NaN
# df=file.dropna()
# print(df)
