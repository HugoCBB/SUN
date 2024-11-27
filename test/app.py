from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configuração do WebDriver
servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)
print('Conexão bem sucedida!')

# Acessar o WhatsApp Web
navegador.get("https://web.whatsapp.com")
print('Escaneie o QR Code para continuar.')

# Aguardar tempo para escanear o QR Code
time.sleep(60)  # Dê tempo suficiente para o usuário escanear o QR Code.

try:
    span = navegador.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[3]/header/header/div/span/div/span/div[1]/div/span')
    span.click()
    time.sleep(5)
except Exception as e:
    print("Erro ao localizar barra de SPAN:", e)
    
# Localizar o campo de busca para procurar o contato ou número
try:
    barra_pesquisa = navegador.find_element(By.XPATH, '//*[@id="app"]/div/div[3]/div[2]/div[1]/span/div/span/div/div[1]/div[2]/div[2]')
    barra_pesquisa.click()
    barra_pesquisa.send_keys("+55 71 99710-3182")  # Substitua pelo número desejado
    barra_pesquisa.send_keys(Keys.RETURN)
    time.sleep(5)  # Aguarde o chat carregar
except Exception as e:
    print("Erro ao localizar barra de pesquisa:", e)
    navegador.quit()