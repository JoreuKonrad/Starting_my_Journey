from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('https://www.incepa.com.br/serie/arbol/produto/lm-arbol-canela-ac-20x120-r-7mm')
bs = BeautifulSoup(html.read(), 'html.parser')
print(bs.body)