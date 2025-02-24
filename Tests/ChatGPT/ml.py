import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder

def criar_base_dados():
    np.random.seed(42)
    clientes = ["Cliente A", "Cliente B", "Cliente C", "Cliente D"]
    carros = ["Sedan", "SUV", "Hatch", "Pickup"]
    cores = ["Preto", "Branco", "Vermelho", "Azul"]
    
    dados = []
    for _ in range(500):
        cliente = np.random.choice(clientes)
        mes = np.random.randint(1, 13)
        ano = np.random.randint(2023, 2025)
        carro = np.random.choice(carros)
        cor = np.random.choice(cores)
        quantidade = np.random.randint(1, 5)
        receita = quantidade * np.random.randint(30000, 120000)
        
        dados.append([cliente, ano, mes, carro, cor, quantidade, receita])
    
    df = pd.DataFrame(dados, columns=["Nome do Cliente", "Ano", "Mes", "Nome do Carro", "Cor do Carro", "Quantidade", "Receita"])
    return df

def treinar_modelo(df):
    le_cliente = LabelEncoder()
    le_carro = LabelEncoder()
    le_cor = LabelEncoder()
    
    df["Nome do Cliente"] = le_cliente.fit_transform(df["Nome do Cliente"])
    df["Nome do Carro"] = le_carro.fit_transform(df["Nome do Carro"])
    df["Cor do Carro"] = le_cor.fit_transform(df["Cor do Carro"])
    
    X = df.drop(columns=["Quantidade", "Receita"])
    y = df["Quantidade"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    modelo = RandomForestRegressor(n_estimators=100, random_state=42)
    modelo.fit(X_train, y_train)
    
    return modelo, le_cliente, le_carro, le_cor, X.columns

def prever_compra(modelo, le_cliente, le_carro, le_cor, colunas, cliente, carro, cor):
    try:
        cliente_cod = le_cliente.transform([cliente])[0]
        carro_cod = le_carro.transform([carro])[0]
        cor_cod = le_cor.transform([cor])[0]
        
        entrada = pd.DataFrame([[cliente_cod, 2025, 3, carro_cod, cor_cod]], columns=colunas)
        previsao = modelo.predict(entrada)
        return round(previsao[0])
    except ValueError:
        return None

def plotar_historico_cliente(df, cliente):
    df_cliente = df[df["Nome do Cliente"] == cliente]
    df_cliente = df_cliente.sort_values(by=["Ano", "Mes"])
    df_cliente["Tempo"] = df_cliente["Ano"].astype(str) + "-" + df_cliente["Mes"].astype(str)
    
    plt.figure(figsize=(10, 5))
    plt.plot(df_cliente["Tempo"], df_cliente["Quantidade"], marker="o", linestyle="-", label=f"{cliente}")
    plt.xlabel("Tempo (Ano-Mês)")
    plt.ylabel("Quantidade Faturada")
    plt.title(f"Histórico de Quantidade Faturada do Cliente {cliente}")
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()
    plt.show()

# Criar e treinar o modelo
df = criar_base_dados()
modelo, le_cliente, le_carro, le_cor, colunas = treinar_modelo(df)

# Exibir combinações disponíveis
print("Combinações disponíveis na base de dados:")
combinacoes_disponiveis = df[["Nome do Cliente", "Nome do Carro", "Cor do Carro"]].drop_duplicates()
print(combinacoes_disponiveis)

# Exemplo de entrada válida
exemplo_valido = combinacoes_disponiveis.sample(1).values[0]
cliente_exemplo, carro_exemplo, cor_exemplo = exemplo_valido
print(f"Exemplo válido: Cliente: {cliente_exemplo}, Carro: {carro_exemplo}, Cor: {cor_exemplo}")

# Input do usuário
cliente = input("Digite o nome do cliente (exemplo: Cliente A): ")
carro = input("Digite o modelo do carro (exemplo: SUV): ")
cor = input("Digite a cor do carro (exemplo: Preto): ")

# Fazer previsão
resultado = prever_compra(modelo, le_cliente, le_carro, le_cor, colunas, cliente, carro, cor)
if resultado is not None:
    print(f"Previsão de compra para {cliente}: {resultado} unidades do {carro} ({cor}) no próximo mês.")
    plotar_historico_cliente(df, cliente)
else:
    print("Erro: Cliente, carro ou cor não encontrados na base de dados. Verifique a entrada.")
