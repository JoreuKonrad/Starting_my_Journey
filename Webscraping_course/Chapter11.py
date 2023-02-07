from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), 
    options=chrome_options)
driver.get('https://www.telhanorte.com.br/rodape-em-porcelanato-munari-acetinado-hd-frisado-14-5x90cm-caixa-c-6-pecas-branco-eliane-1426591/p?utm_source=blue&utm_medium=cpa&utm_campaign=retargetingblue')

print('Aguande...')
time.sleep(10)

print('Dados:')
#print(driver.find_element(By.ID,'content').text)
print(driver.find_element(By.XPATH,'/html/body/main/div[1]/div[2]/div[2]/div[2]/div[1]/h1').text)
print(driver.find_element(By.XPATH,'/html/body/main/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/p/ins/strong').text)

driver.close()