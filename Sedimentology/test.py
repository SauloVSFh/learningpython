import pandas as pd

filename = "Curso Análise de Dados/Exemplo_C14.csv"
file = pd.read_csv(filename,index_col=None)
df = file.loc[file.Amostra == 'A38']
print(df)
# print(file.groupby("Amostra").count())
