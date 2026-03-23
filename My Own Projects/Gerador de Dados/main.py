#Gerador de dados. Crie tabelas de dimensões como dim_cliente, dim_produto, dim_tempo e uma tabela de fatos como fato_vendas. Popule essas tabelas com dados fictícios para simular um ambiente de data warehouse. Use bibliotecas como Faker para gerar dados realistas. Por fim gere csv de cada dataframe
import pandas as pd
from faker import Faker
fake = Faker()
# Gerar dados para dim_cliente
clientes = []
for _ in range(100):
    cliente = {
        'cliente_id': fake.unique.random_int(min=1, max=1000),
        'nome': fake.name(),
        'email': fake.email(),
        'telefone': fake.phone_number(),
        'endereco': fake.address()
    }
    clientes.append(cliente)


