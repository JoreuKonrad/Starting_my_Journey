import pandas as pd

# Criar dois DataFrames
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Nome': ['Alice', 'Bob', 'Charlie']})
df2 = pd.DataFrame({'ID': [2, 3, 4,2], 'Idade': [25, 30, 35,40]})

# Realizar o merge com base na coluna 'ID'
df_merged = pd.merge(df1, df2, on='ID')

# Exibir o DataFrame resultante
print(df_merged)



