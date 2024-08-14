from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def init_driver():
    #chrome_driver_path = r"/home/stic/Área de Trabalho/chromedriver-linux64/chromedriver"  # Substitua pelo caminho real do chromedriver.exe
    
    #service = Service(chrome_driver_path)
    service = Service("/usr/bin/chromedriver")
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Executar o Chrome em modo headless (sem interface gráfica)
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def fetch_page_content_with_selenium(url):
    driver = init_driver()
    driver.get(url)
    page_content = driver.page_source
    driver.quit()
    return page_content