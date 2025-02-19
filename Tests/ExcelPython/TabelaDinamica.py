import openpyxl
from openpyxl.utils.dataframe import dataframe_to_rows
import pandas as pd

# Criar um workbook e adicionar uma planilha
wb = openpyxl.Workbook()
ws_fato = wb.active
ws_fato.title = "Fato"

# Criar a tabela de Fato (exemplo)
dados_fato = {
    "ID_Venda": [1, 2, 3],
    "ID_Produto": [101, 102, 103],
    "Quantidade": [10, 15, 5],
    "Preço": [100, 200, 150],
    "Custo": [60, 120, 90]
}
df_fato = pd.DataFrame(dados_fato)

# Adicionar dados da tabela de Fato
for r in dataframe_to_rows(df_fato, index=False, header=True):
    ws_fato.append(r)

# Criar uma segunda planilha para a dimensão
ws_dimensao = wb.create_sheet(title="Dimensão")

# Criar a tabela de Dimensão (exemplo)
dados_dimensao = {
    "ID_Produto": [101, 102, 103],
    "Nome_Produto": ["Produto A", "Produto B", "Produto C"],
    "Categoria": ["Categoria 1", "Categoria 2", "Categoria 1"]
}
df_dimensao = pd.DataFrame(dados_dimensao)

# Adicionar dados da tabela de Dimensão
for r in dataframe_to_rows(df_dimensao, index=False, header=True):
    ws_dimensao.append(r)

# Salvar a planilha
wb.save("planilha_com_modelo_dinamico.xlsx")

print("Planilha criada com sucesso!")
