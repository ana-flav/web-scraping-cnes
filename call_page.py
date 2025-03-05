from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

download_path = "path_to_save_downloads"

options = webdriver.ChromeOptions()
options.add_experimental_option("prefs", {
    "download.default_directory": download_path,  
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


url = "https://datasus.saude.gov.br/transferencia-de-arquivos/"
driver.get(url)


wait = WebDriverWait(driver, 15)


fonte_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='mySelect']")))
fonte = Select(fonte_element)
fonte.select_by_visible_text("CNES - Cadastro Nacional de Estabelecimentos de Saúde")


modalidade_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='modSelect']")))
modalidade = Select(modalidade_element)
modalidade.select_by_visible_text("Dados")


tipo_arquivo_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='tipo_arquivo']")))
tipo_arquivo = Select(tipo_arquivo_element)
tipo_arquivo.select_by_visible_text("DC - Dados Complementares - A partir de Ago/2005")

ano_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='modAno']")))
ano = Select(ano_element)
ano.select_by_visible_text("2025")  


mes_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='modmes']")))
mes = Select(mes_element)

uf_element = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='moduf']")))
uf = Select(uf_element)
uf.select_by_visible_text("TO") 


botao_confirmar = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='dados_transferencia']/button")))
botao_confirmar.click()

time.sleep(5)

link_download_element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='post-1492']/div/div/section[2]/div/div[2]/div/div/div/p[2]/a")))
link_download_element.click()


link_final_download = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='arquivo_compactado']/p/a")))
link_final_download.click()

time.sleep(5)


driver.quit()
