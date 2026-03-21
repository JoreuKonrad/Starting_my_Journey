import pandas as pd

# Criar um DataFrame de exemplo
data = {
    'Categoria': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Data': ['2023-01-01', '2023-01-01', '2023-01-02', '2023-01-02', '2023-01-03', '2023-01-03'],
    'Valor': [10, 20, 15, 25, 12, 18],
    'Filtro': ['X', 'Y', 'X', 'Y', 'X', 'Y']
}

df = pd.DataFrame(data)

# Leia o arquivo Excel
nome_arquivo_entrada = 'dados.xlsx'
df.to_excel(nome_arquivo_entrada, index=False)

# Especifique as colunas para a tabela dinâmica
indice = 'Categoria'
colunas = 'Data'
valores = 'Valor'
filtros = 'Filtro'

# Crie uma tabela dinâmica
tabela_dinamica = pd.pivot_table(df, values=valores, index=[indice], columns=[colunas], aggfunc='sum', fill_value=0)

# Adicione filtros à tabela dinâmica
tabela_dinamica_com_filtros = pd.pivot_table(df, values=valores, index=[indice], columns=[colunas], aggfunc='sum', fill_value=0,
                                             margins=True, margins_name='Total', dropna=False)

# Salve a tabela dinâmica com filtros em um novo arquivo Excel
nome_arquivo_saida_com_filtros = 'tabela_dinamica_com_filtros.xlsx'
tabela_dinamica_com_filtros.to_excel(nome_arquivo_saida_com_filtros)

print(f"Tabela dinâmica com filtros criada e salva em {nome_arquivo_saida_com_filtros}")
