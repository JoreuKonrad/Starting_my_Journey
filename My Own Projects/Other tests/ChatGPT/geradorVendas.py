import pandas as pd

# Carregar os dados
file_path = "C:/Users/joreu/OneDrive/Documents/Sewe/VENDA.txt"
df = pd.read_csv(file_path, sep="\t")

# Converter a coluna de data para formato datetime
df["Periodo.Data"] = pd.to_datetime(df["Periodo.Data"], format="%d-%m-%Y")

# Adicionar coluna de ano-mês
df["AnoMes"] = df["Periodo.Data"].dt.to_period("M")

# Calcular a média de registros por cliente por mês
media_registros = df.groupby(["Cliente", "AnoMes"]).size().groupby("Cliente").mean()

# Definir os novos meses para projeção (adicionando mais 6 meses)
novos_meses = pd.date_range(start=df["Periodo.Data"].max(), periods=17, freq="M")[1:].to_period("M")

# Criar novos registros baseados na média de registros por cliente
novos_dados = []
for cliente, media in media_registros.items():
    media = int(round(media))  # Arredondar para número inteiro de registros
    for mes in novos_meses:
        # Pegar registros reais do cliente e replicar
        registros_cliente = df[df["Cliente"] == cliente].sample(n=media, replace=True)
        registros_cliente = registros_cliente.copy()
        registros_cliente["AnoMes"] = mes
        registros_cliente["Periodo.Data"] = registros_cliente["AnoMes"].dt.to_timestamp()
        novos_dados.append(registros_cliente)

# Concatenar os dados originais com os novos
df_expandido = pd.concat([df] + novos_dados, ignore_index=True)

# Remover a coluna AnoMes
df_expandido.drop(columns=["AnoMes"], inplace=True)

# Salvar o novo arquivo
new_file_path = "C:/Users/joreu/OneDrive/Documents/Sewe/VENDA_EXPANDIDA_2.xlsx"
df_expandido.to_excel(new_file_path, index=False)


