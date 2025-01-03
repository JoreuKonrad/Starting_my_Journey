from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "lxml")
        title = bsObj.body.h2
    except AttributeError as e:
        return None
    return title


title = getTitle("https://www.biancogres.com.br/produto/botanic")
if title == None:
    print("Title could not be found")
else:
    print(title)
    
    