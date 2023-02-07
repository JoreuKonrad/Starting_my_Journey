from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(
    executable_path='drivers/chromedriver',
    options=chrome_options)

driver.get('https://www.leroymerlin.com.br/porcelanato-externo-fosco-borda-reta-22x90cm-madeira-moka-artens_90439286')
try:
    element = WebDriverWait(driver, 10).until(
                       EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/div/div[1]/div[2]/div[1]/div[1]/h1')))
finally:
    print(driver.find_element(By.XPATH,'/html/body/div[9]/div/div[1]/div[2]/div[1]/div[1]/h1').text)
    driver.close()