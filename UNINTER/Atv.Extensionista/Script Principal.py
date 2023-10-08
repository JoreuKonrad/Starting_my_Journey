import pandas as pd
from bs4 import BeautifulSoup
import time
from random import randint
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

url= 'http://mtr.ima.sc.gov.br/'
options = webdriver.ChromeOptions()
#options.add_argument("--headless=new")

driver = webdriver.Chrome(ChromeDriverManager().install())#,executable_path="C:/ChromeDriver/chromedriver.exe")
driver.get(url)


usuario = driver.find_element(By.ID,'txtCnpj').click()
usuario = driver.find_element(By.ID,'txtCnpj')
usuario.send_keys('*******') #Login 
senha = driver.find_element(By.ID,'txtSenha').click()
senha = driver.find_element(By.ID,'txtSenha')
senha.send_keys('********') # Senha

time.sleep(5)
buttom = driver.find_element(By.ID,'btEntrar').click()

time.sleep(5)
buttomQuit = driver.find_element(By.XPATH,'/html/body/div[9]/div[1]/button').click()

time.sleep(1)
elementHover = driver.find_element(By.ID,'menu1')
hover = ActionChains(driver).move_to_element(elementHover)
hover.perform()

time.sleep(1)
driver.find_element(By.ID,'menu6').click()

time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="relatorioMtr"]/table/tbody/tr[1]/td[2]/img').click()

#Escolhendo Mês
time.sleep(1)
data = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/select[1]').click()
time.sleep(1)
data = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/div/div/select[1]/option[1]').click()

#Escolhendo Dia
time.sleep(1)
data = driver.find_element(By.XPATH,'//*[@id="ui-datepicker-div"]/table/tbody/tr[1]/td[1]/a').click()

#Baixando Arquivo
time.sleep(1)
data = driver.find_element(By.XPATH,'//*[@id="btnGravar"]').click()

# Importar Controle NF e Relatorio Gerado
dfControleNF = pd.read_excel('Controle de Nota Fiscal.xlsx')
dfRelGerado = pd.read_excel('rel_mtr_ger_trans_des.xlsx')
dfControleAtt = dfControleNF

for numMtr in dfControleNF['MTR Nº']:
    try:
        if numMtr is dfControleNF['Nº Nota Fiscal']:
            dfControleAtt.loc[numMtr,'Baixa MTR'] = 'X'
        else:
            dfControleAtt.loc[numMtr,'Baixa MTR'] = ''
    except:
        pass

dfControleAtt.to_excel('Controle de Nota Fiscal ATUALIZADO.xlsx')

time.sleep(25)
driver.close()
