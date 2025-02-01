import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Gerando dados fictícios
np.random.seed(42)
n_samples = 500

clientes = np.random.choice(['Cliente A', 'Cliente B', 'Cliente C'], size=n_samples)
produtos = np.random.choice(['Produto X', 'Produto Y', 'Produto Z'], size=n_samples)
preco = np.random.uniform(10, 100, size=n_samples)
quantidade = np.random.randint(1, 50, size=n_samples)

# Criando um DataFrame
df = pd.DataFrame({'Cliente': clientes, 'Produto': produtos, 'Preço': preco, 'Quantidade': quantidade})

# Criando uma variável de preço logaritmo
df['log_preco'] = np.log(df['Preço'])
df['log_qtd'] = np.log(df['Quantidade'])

# Criando um modelo de regressão para cada cliente-produto
elasticidades = []

for (cliente, produto), grupo in df.groupby(['Cliente', 'Produto']):
    if len(grupo) > 5:  # Apenas grupos com dados suficientes
        X = grupo[['log_preco']]
        y = grupo['log_qtd']
        modelo = LinearRegression()
        modelo.fit(X, y)
        elasticidade = modelo.coef_[0]
        elasticidades.append({'Cliente': cliente, 'Produto': produto, 'Elasticidade': elasticidade})

# Criando DataFrame com elasticidades
elasticidade_df = pd.DataFrame(elasticidades)
print(elasticidade_df)

# Visualizando os resultados
plt.figure(figsize=(10, 5))
sns.barplot(data=elasticidade_df, x='Produto', y='Elasticidade', hue='Cliente')
plt.axhline(0, color='black', linestyle='--')
plt.title('Elasticidade Preço da Demanda por Cliente e Produto')
plt.ylabel('Elasticidade Preço')
plt.xlabel('Produto')
plt.legend(title='Cliente')
plt.show()
