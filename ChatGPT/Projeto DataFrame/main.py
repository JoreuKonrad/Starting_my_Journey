import pandas as pd

class ManipuladorDataFrame:
    def __init__(self, dados):
        self.df = pd.DataFrame(dados)

    def adicionar_coluna(self, nome_coluna, dados):
        self.df[nome_coluna] = dados

    def remover_coluna(self, nome_coluna):
        self.df.drop(columns=[nome_coluna], inplace=True)

    def obter_resumo(self):
        return self.df.describe()

    def filtrar_linhas(self, condicao):
        return self.df.query(condicao)

    def atualizar_valor(self, linha, coluna, novo_valor):
        self.df.at[linha, coluna] = novo_valor

# Exemplo de uso
if __name__ == "__main__":
    dados = {
        'Produto': ['Produto A', 'Produto B', 'Produto C'],
        'Cliente': ['Cliente 1', 'Cliente 2', 'Cliente 3'],
        'Quantidade': [10, 20, 30],
        'Receita': [1000, 2000, 3000],
        'Data': ['2023-01-01', '2023-01-02', '2023-01-03']
    }

    manipulador_df = ManipuladorDataFrame(dados)
    print("DataFrame Inicial:")
    print(manipulador_df.df)

    manipulador_df.adicionar_coluna('Desconto', [100, 200, 300])
    print("\nDataFrame após adicionar coluna Desconto:")
    print(manipulador_df.df)

    manipulador_df.remover_coluna('Desconto')
    print("\nDataFrame após remover coluna Desconto:")
    print(manipulador_df.df)

    print("\nResumo do DataFrame:")
    print(manipulador_df.obter_resumo())

    filtered_df = manipulador_df.filtrar_linhas('Quantidade > 15')
    print("\nDataFrame filtrado (Quantidade > 15):")
    print(filtered_df)

    manipulador_df.atualizar_valor(1, 'Quantidade', 25)
    print("\nDataFrame após atualizar valor na linha 1, coluna 'Quantidade':")
    print(manipulador_df.df)