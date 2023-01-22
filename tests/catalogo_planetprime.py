from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import pandas as pd
import time


url = 'https://www.planetprime.com.br/fones-de-ouvido'

html = urlopen(url)
bsObj = BeautifulSoup(html.read(), "lxml")

lista_links_produtos = bsObj.find_all('a',{'class':'info-product'})


lista_vazia = []
df_links_produtos = pd.DataFrame(lista_vazia,columns=['Links'])
df_produtos = pd.DataFrame(lista_vazia,columns=['Nome','Preco','Parcelas','Marca','Codigo'])
    

for link_produto in lista_links_produtos:
    link_produto = link_produto['href']
    df_links_produtos.loc[len(df_links_produtos)] = [link_produto]
    

for endereco_produto in df_links_produtos['Links']:
    
    print('Aguarde...')
    time.sleep(4)
    print('Acessando o site...')
    #Acessando o site e extraindo o html
    html = urlopen(endereco_produto)
    bsObj = BeautifulSoup(html.read(), "lxml")
    
    nome_produto = bsObj.find('h1',{'class':'product-name'}).get_text(' ',strip=True)
    preco_produto = bsObj.find('span',{'data-app':'product.price'}).get_text(' ',strip=True)
    
    div_infos_preco = bsObj.find('div',{'id':'produto_preco'})
    parcelamento_produto = div_infos_preco.find('strong').get_text(' ',strip=True)

    codigo_produto = bsObj.find('span',{'class':'ref'}).get_text(' ',strip=True).replace('(Cód.: ','').replace(')','')

    td_infos_produto = bsObj.find_all('td')
    x = 0
    for td_info in td_infos_produto:
    
        td_info = str(td_info)
    
        if td_info == '<td>Marca</td>':
            marca_produto = td_infos_produto[x+1].get_text()       
        x += 1
    
    
    
    df_produtos.loc[len(df_produtos)] = [nome_produto,preco_produto,parcelamento_produto,marca_produto,codigo_produto]
    print('Produto '+ nome_produto +' registrado!\n')
    
df_produtos.to_excel('C:/Users/Samsung/Desktop/projetos/Produtos_planetprime.xlsx')
print('Concluido!')
