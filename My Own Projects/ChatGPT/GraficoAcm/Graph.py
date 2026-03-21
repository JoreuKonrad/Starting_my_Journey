import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from pandas.tseries.offsets import BDay

# Criar um DataFrame de exemplo
data = {'Data': ['2023-11-01', '2023-11-05', '2023-11-10', '2023-12-02', '2023-12-08'],
        'Faturamento': [100, 150, 200, 120, 180],
        'Volume_Faturado': [50, 70, 90, 60, 80]}

df = pd.DataFrame(data)
df['Data'] = pd.to_datetime(df['Data'])
df = df.sort_values(by='Data')

# Adicionar uma coluna com o mês e o ano
df['Mes'] = df['Data'].dt.month
df['Ano'] = df['Data'].dt.year

# Filtrar os dados para o mês atual e o anterior
data_atual = datetime.now()
df_mes_atual = df[(df['Mes'] == data_atual.month) & (df['Ano'] == data_atual.year)]
df_mes_anterior = df[(df['Mes'] == data_atual.month - 1) & (df['Ano'] == data_atual.year)]

# Calcular o valor acumulado apenas nos dias úteis
df_mes_atual['Data_Uteis'] = df_mes_atual['Data'] + pd.to_timedelta(np.arange(len(df_mes_atual)), 'D')
df_mes_atual['Faturamento_Acumulado'] = df_mes_atual['Faturamento'].cumsum()
df_mes_atual = df_mes_atual.set_index('Data_Uteis').asfreq(BDay())

df_mes_anterior['Data_Uteis'] = df_mes_anterior['Data'] + pd.to_timedelta(np.arange(len(df_mes_anterior)), 'D')
df_mes_anterior['Faturamento_Acumulado'] = df_mes_anterior['Faturamento'].cumsum()
df_mes_anterior = df_mes_anterior.set_index('Data_Uteis').asfreq(BDay())

# Criar o gráfico de linhas
plt.plot(df_mes_atual.index, df_mes_atual['Faturamento_Acumulado'], label='Mês Atual', marker='o')
plt.plot(df_mes_anterior.index, df_mes_anterior['Faturamento_Acumulado'], label='Mês Anterior', marker='o')

# Adicionar mais uma linha de exemplo
plt.plot(df_mes_atual.index, df_mes_atual['Volume_Faturado'].cumsum(), label='Volume Faturado', marker='o', linestyle='--')

# Adicionar rótulos e título ao gráfico
plt.xlabel('Data')
plt.ylabel('Faturamento Acumulado / Volume Faturado Acumulado')
plt.title('Faturamento e Volume Faturado Acumulado do Mês Atual e Anterior (Dias Úteis)')
plt.legend()

# Exibir o gráfico
plt.show()
