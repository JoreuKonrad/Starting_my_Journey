
"""Para finalizar o projeto com sucesso, você precisará colocar em prática seus conhecimentos 
sobre a fase de teste, mais especificamento sobre o Teste TDD. Você foi destinado a testar 
duas classes programadas em Python, uma classe para o cadastro produtos automotivos e 
outra classe para cadastrar clientes. Além de desenvolver as DUAS classes, você precisará 
mostrar que as classes irão retornar com sucesso os dados, ou seja, colar o código identado e 
com comentários. Porm fim, colocar a imagem do terminar sendo executado sem erros com 
os dados correto das classes testadas. """


class Produto:
    lista_produtos = []  # lista para armazenar os produtos cadastrados

    def __init__(self, codigo, descricao, marca, tipo): # iniciação dos dados produtos. Estoque começa com 0
        self.codigo = codigo
        self.descricao = descricao
        self.marca = marca
        self.tipo = tipo
        self.estoque = 0  

    def apresentar(self): #display de dados
        print(f"Código: {self.codigo}")
        print(f"Descrição: {self.descricao}")
        print(f"Marca: {self.marca}")
        print(f"Tipo: {self.tipo}")
        print(f"Estoque: {self.estoque}")

    @classmethod
    def cadastrar(cls, codigo, descricao, marca, tipo):

        if any(produto.codigo == codigo for produto in cls.lista_produtos): # check se existe o codigo
            print(f"O código {codigo} já está cadastrado. Tente outro.")
            return None

        novo_produto = cls(codigo, descricao, marca, tipo)
        cls.lista_produtos.append(novo_produto)
        print(f"Produto '{descricao}' cadastrado com sucesso!")
        return novo_produto

    def ajustar_estoque(self, quantidade): # movimentação de estoque
        # Ajusta o estoque com base na quantidade
        if self.estoque + quantidade < 0:
            print("Erro: Estoque não pode ser negativo!")
        else:
            self.estoque += quantidade
            print(f"Estoque ajustado. Novo estoque: {self.estoque}")

    @classmethod
    def listar_produtos(cls): # função para listar todos os produtos cadastrados e os estoques
        if not cls.lista_produtos:
            print("Nenhum produto cadastrado.")
        else:
            print("Lista de produtos cadastrados:")
            for produto in cls.lista_produtos:
                produto.apresentar()
                print("-" * 20)

class Cliente:
    lista_clientes = []  # Lista para armazenar os clientes cadastrados

    def __init__(self, cpf, nome, email): # iniciação dos dados cadastrados
        self.cpf = cpf
        self.nome = nome
        self.email = email

    def apresentar(self): #apresenta os dados do usuario
        print(f"CPF: {self.cpf}")
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")

    @classmethod
    def cadastrar(cls, cpf, nome, email): 
        if any(cliente.cpf == cpf for cliente in cls.lista_clientes): # não cadastra se o cpf já existir
            print(f"O CPF {cpf} já está cadastrado. Tente outro.")
            return None

        novo_cliente = cls(cpf, nome, email) # cadastro valido
        cls.lista_clientes.append(novo_cliente)
        print(f"Cliente '{nome}' cadastrado com sucesso!")
        return novo_cliente

    @classmethod
    def listar_clientes(cls): # listar todos os clientes
        if not cls.lista_clientes:
            print("Nenhum cliente cadastrado.")
        else:
            print("Lista de clientes cadastrados:")
            for cliente in cls.lista_clientes:
                cliente.apresentar()
                print("-" * 20)


produto1 = Produto.cadastrar(881002,
                             'Oleo Motor Shell Helix Hx8 5w-30 API SP ILSAC GF-6A Sintetico',
                             'Shell',
                             'Oléo Sintético')



cliente1 = Cliente.cadastrar('111.222.333-55',
                             'Tobby',
                             'tobby@email.com')

print('\n')
produto1.apresentar()
print('\n---')
cliente1.apresentar()